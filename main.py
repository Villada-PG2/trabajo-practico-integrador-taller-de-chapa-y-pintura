from datetime import datetime, timedelta
from modelos import (
    Aseguradora, Cliente, Vehiculo, Repuesto, DetalleRepuesto,
    Presupuesto, Turno, Empleado, Trabajo, Factura, Pago
)

if __name__ == "__main__":
    print("=== CASO 1: CLIENTE PARTICULAR CON PAGO EN DÉBITO ===")
    
    # 1. Crear Cliente y Vehículo
    cliente1 = Cliente(nombre="Carlos Pérez", telefono="3511234567", esAsegurado=False)
    auto1 = Vehiculo(patente="AF123JK", marca="Toyota", modelo="Corolla", color="Gris", cliente=cliente1)


    paragolpes = Repuesto(nombre="Paragolpes Delantero", precioActual=85000.0)
    optica = Repuesto(nombre="Óptica Izquierda", precioActual=42000.0)

    detalle1 = DetalleRepuesto(repuesto=paragolpes, cantidad=1)
    detalle2 = DetalleRepuesto(repuesto=optica, cantidad=1)

    presupuesto1 = Presupuesto(
        numero=1001,
        duracionEstimadaDias=3,
        descripcionArreglos="Enderezado y pintura de frente",
        vehiculo=auto1,
        detalles=[detalle1, detalle2]
    )
    presupuesto1.calcularMontoTotal()
    print(f"Presupuesto N°{presupuesto1.numero} generado. Total: ${presupuesto1.montoTotal:.2f}")


    fechaTurno = datetime.now() + timedelta(days=2)
    turno1 = Turno(fechaHora=fechaTurno, presupuesto=presupuesto1)
    turno1.confirmarIngreso()


    empleado1 = Empleado(nombre="Mario Rossi", legajo="EMP-042")
    trabajo1 = Trabajo(
        llavesEntregadas=True,
        documentacionEntregada=True,
        turno=turno1
    )
    empleado1.asignarTrabajo(trabajo1)
    trabajo1.iniciarReparacion()
    trabajo1.finalizarTrabajo()
    print(f"Estado del trabajo: {trabajo1.estadoReparacion} por {trabajo1.empleado.nombre}")


    factura1 = Factura(
        numero=5001,
        montoTotal=presupuesto1.montoTotal,
        tipoCliente="Particular",
        trabajo=trabajo1
    )
    print(factura1.generarFactura())

    pago1 = Pago(
        monto=factura1.montoTotal,
        metodoPago="Debito",
        nroCuponPosnet="POS-987654",
        factura=factura1
    )
    if pago1.procesarPago():
        print(pago1.emitirComprobante())

    print("\n" + "="*50 + "\n")

    print("=== CASO 2: CLIENTE ASEGURADO CON FIRMA DE CONFORMIDAD ===")


    sancor = Aseguradora(nombre="Sancor Seguros", numeroConvenio="CNV-8821")
    cliente2 = Cliente(nombre="Ana Gómez", telefono="3519876543", esAsegurado=True)
    auto2 = Vehiculo(patente="AE987ZA", marca="Ford", modelo="Focus", color="Blanco", cliente=cliente2)


    puerta = Repuesto(nombre="Puerta Trasera Izquierda", precioActual=120000.0)
    detalleAsegurado = DetalleRepuesto(repuesto=puerta, cantidad=1)

    presupuesto2 = Presupuesto(
        numero=1002,
        duracionEstimadaDias=5,
        descripcionArreglos="Cambio y pintura de puerta trasera",
        vehiculo=auto2,
        detalles=[detalleAsegurado],
        aseguradora=sancor
    )
    presupuesto2.calcularMontoTotal()


    turno2 = Turno(fechaHora=datetime.now() + timedelta(days=1), presupuesto=presupuesto2)
    trabajo2 = Trabajo(llavesEntregadas=True, documentacionEntregada=True, turno=turno2)
    trabajo2.finalizarTrabajo()


    facturaAseguradora = Factura(
        numero=5002,
        montoTotal=presupuesto2.montoTotal,
        tipoCliente="Asegurado",
        trabajo=trabajo2
    )
    facturaAseguradora.registrarFirmaAsegurado()
    print(facturaAseguradora.generarFactura())
    print(f"Firma de conformidad registrada en factura: {facturaAseguradora.firmaAsegurado}")
    print("Factura archivada para rendición semanal a la compañía aseguradora.")