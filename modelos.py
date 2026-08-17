from datetime import datetime, timedelta
from typing import Optional, List
from pydantic import BaseModel, Field, field_validator, model_validator


class Aseguradora(BaseModel):
    nombre: str = Field(..., description="Nombre de la compañía aseguradora")
    numeroConvenio: str = Field(..., description="Número de convenio con el taller")

    def validarPoliza(self, numeroPoliza: str):
        return bool(numeroPoliza and len(numeroPoliza.strip()) > 0)


class Cliente(BaseModel):
    nombre: str = Field(..., description="Nombre completo del cliente")
    telefono: str = Field(..., description="Teléfono de contacto")
    esAsegurado: bool = Field(default=False, description="Indica si atiende por compañía de seguros")

    def registrarCliente(self):
        return f"Cliente {self.nombre} registrado con éxito."

    def modificarDatos(self, nuevoTelefono: str):
        self.telefono = nuevoTelefono


class Vehiculo(BaseModel):
    patente: str = Field(..., description="Patente o dominio del vehículo")
    marca: str = Field(..., description="Marca del vehículo")
    modelo: str = Field(..., description="Modelo del vehículo")
    color: str = Field(..., description="Color del vehículo")
    cliente: Cliente = Field(..., description="Cliente dueño del vehículo")

    def registrarVehiculo(self):
        return f"Vehículo {self.patente} registrado a nombre de {self.cliente.nombre}."


class Repuesto(BaseModel):
    nombre: str = Field(..., description="Nombre del repuesto")
    precioActual: float = Field(..., description="Precio unitario actualizado")

    @field_validator("precioActual")
    @classmethod
    def validarPrecio(cls, value: float):
        if value < 0:
            raise ValueError("El precio del repuesto no puede ser negativo.")
        return value

    def actualizarPrecio(self, nuevoPrecio: float):
        if nuevoPrecio < 0:
            raise ValueError("El nuevo precio no puede ser negativo.")
        self.precioActual = nuevoPrecio


class DetalleRepuesto(BaseModel):
    repuesto: Repuesto = Field(..., description="Instancia del repuesto solicitado")
    cantidad: int = Field(..., description="Cantidad a utilizar")
    subtotal: float = Field(default=0.0, description="Subtotal calculado")

    @field_validator("cantidad")
    @classmethod
    def validarCantidad(cls, value: int):
        if value <= 0:
            raise ValueError("La cantidad de repuestos debe ser mayor a 0.")
        return value

    def calcularSubtotal(self):
        self.subtotal = self.repuesto.precioActual * self.cantidad
        return self.subtotal


class Presupuesto(BaseModel):
    numero: int = Field(..., description="Número único de presupuesto")
    fechaEmision: datetime = Field(default_factory=datetime.now, description="Fecha de emisión del presupuesto")
    duracionEstimadaDias: int = Field(..., description="Duración estimada del trabajo en días")
    descripcionArreglos: str = Field(..., description="Detalle de los trabajos a realizar")
    montoTotal: float = Field(default=0.0, description="Monto total del presupuesto")
    vehiculo: Vehiculo = Field(..., description="Vehículo presupuestado")
    detalles: List[DetalleRepuesto] = Field(default_factory=list, description="Lista de repuestos involucrados")
    aseguradora: Optional[Aseguradora] = Field(default=None, description="Aseguradora vinculada si aplica")

    def calcularMontoTotal(self):
        self.montoTotal = sum(detalle.calcularSubtotal() for detalle in self.detalles)
        return self.montoTotal

    def verificarVigencia(self):
        fechaLimite = self.fechaEmision + timedelta(days=30)
        return datetime.now() <= fechaLimite

    def generarPDF(self):
        return f"PDF Presupuesto #{self.numero} generado para vehículo patente {self.vehiculo.patente}."


class Turno(BaseModel):
    fechaHora: datetime = Field(..., description="Fecha y hora asignada para el turno")
    estado: str = Field(default="Pendiente", description="Estado del turno (Pendiente, Confirmado, Cancelado)")
    presupuesto: Presupuesto = Field(..., description="Presupuesto que origina el turno")

    @model_validator(mode="after")
    def verificarVigenciaPresupuesto(self):
        if not self.presupuesto.verificarVigencia():
            raise ValueError("No se puede solicitar turno: El presupuesto ha superado sus 30 días de vigencia.")
        return self

    def solicitarTurno(self):
        self.estado = "Pendiente"

    def cancelarTurno(self):
        self.estado = "Cancelado"

    def confirmarIngreso(self):
        self.estado = "Confirmado"


class Empleado(BaseModel):
    nombre: str = Field(..., description="Nombre del empleado de taller")
    legajo: str = Field(..., description="Número de legajo")

    def asignarTrabajo(self, trabajo: "Trabajo"):
        trabajo.empleado = self


class Trabajo(BaseModel):
    fechaIngreso: datetime = Field(default_factory=datetime.now, description="Fecha de ingreso del auto a taller")
    llavesEntregadas: bool = Field(..., description="Confirmación de entrega de llaves")
    documentacionEntregada: bool = Field(..., description="Confirmación de entrega de documentación")
    estadoReparacion: str = Field(default="En Proceso", description="Estado de avance (En Proceso, Finalizado)")
    turno: Turno = Field(..., description="Turno de origen")
    empleado: Optional[Empleado] = Field(default=None, description="Empleado responsable asignado")

    @model_validator(mode="after")
    def verificarDocumentacionYLlaves(self):
        if not (self.llavesEntregadas and self.documentacionEntregada):
            raise ValueError("El cliente debe dejar obligatoriamente las llaves y la documentación completa.")
        return self

    def iniciarReparacion(self):
        self.estadoReparacion = "En Proceso"

    def actualizarEstado(self, nuevoEstado: str):
        self.estadoReparacion = nuevoEstado

    def finalizarTrabajo(self):
        self.estadoReparacion = "Finalizado"


class Factura(BaseModel):
    numero: int = Field(..., description="Número de factura emitida")
    fechaEmision: datetime = Field(default_factory=datetime.now, description="Fecha de emisión")
    montoTotal: float = Field(..., description="Monto total facturado")
    tipoCliente: str = Field(..., description="Tipo de cliente (Particular / Asegurado)")
    firmaAsegurado: bool = Field(default=False, description="Conformidad del cliente asegurado")
    trabajo: Trabajo = Field(..., description="Trabajo finalizado origen de la factura")

    def generarFactura(self):
        return f"Factura N° {self.numero} emitida por un monto de ${self.montoTotal:.2f} ({self.tipoCliente})"

    def registrarFirmaAsegurado(self):
        if self.tipoCliente == "Asegurado":
            self.firmaAsegurado = True


class Pago(BaseModel):
    fecha: datetime = Field(default_factory=datetime.now, description="Fecha y hora de procesamiento del pago")
    monto: float = Field(..., description="Monto abonado")
    metodoPago: str = Field(..., description="Método utilizado (Efectivo / Debito)")
    nroCuponPosnet: Optional[str] = Field(default=None, description="Cupón si se opera con Tarjeta de Débito")
    factura: Factura = Field(..., description="Factura abonada")

    @field_validator("metodoPago")
    @classmethod
    def validarMetodoPago(cls, value: str):
        if value not in ["Efectivo", "Debito"]:
            raise ValueError("Las formas de pago aceptadas son únicamente 'Efectivo' o 'Debito'.")
        return value

    @model_validator(mode="after")
    def validarTransaccionPosnet(self):
        if self.metodoPago == "Debito" and not self.nroCuponPosnet:
            raise ValueError("Para pagos con débito es obligatorio registrar el número de cupón del POSNET.")
        return self

    def procesarPago(self):
        return self.monto >= self.factura.montoTotal

    def emitirComprobante(self):
        return f"Comprobante de pago generado por ${self.monto:.2f} mediante {self.metodoPago}."