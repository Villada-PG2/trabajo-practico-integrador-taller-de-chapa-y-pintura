# Dominio Taller de Chapa y Pintura

En nuestra ciudad, un taller de chapa y pintura desarrolla su actividad atendiendo
clientes particulares o a asegurados en algunas compañías aseguradoras con las cuales
tiene convenio. La empresa tiene una gran infraestructura y modernos equipos de pintura
para asegurar la calidad de los trabajos realizados.


Entre algunas de sus políticas cabe destacar las siguientes:
● La Atención del Cliente para realizar efectivamente los arreglos, se realiza a través
de turnos únicamente y está a cargo del coordinador del taller.
● El taller posee convenios con Compañías de Seguro, los clientes asegurados en
dichas compañías pueden utilizar los servicios correspondientes en este taller.
● El Cliente debe dejar las llaves y la documentación del vehículo completa y en orden
para la realización del arreglo.


Cada vez que un cliente concurre para consultar por un arreglo es atendido por el
coordinador del taller quien se interioriza del trabajo que el cliente necesita y evalúa si es
necesario usar repuestos en el arreglo (por ejemplo paragolpes, cristales, etc.).
Luego prepara un presupuesto para el cliente donde se detallan los datos del cliente,
un teléfono de contacto, los datos del vehículo (patente, marca, modelo, color, etc.), la
descripción de los arreglos que se realizarán y un detalle de los repuestos que se usarán,
además de la duración del trabajo. Para ello el coordinador del taller consulta una lista de
precios de los repuestos, que se mantiene actualizada. Los presupuestos tienen hasta 30
días de vigencia.


Si el cliente está asegurado en alguna de las compañías de seguro con las que
trabaja la empresa, en el presupuesto también se detalla el nombre de la aseguradora y el
número de la póliza de seguro.


En el caso de un asegurado, el cliente deberá gestionar que su aseguradora autorice
el presupuesto. Es decir que queda a cargo del Cliente gestionar la autorización del
presupuesto personalmente con su Compañía de Seguro.


Para que un cliente pueda realizar el arreglo ya presupuestado, debe solicitar un
turno para el vehículo. Sea que lo haga por teléfono o personalmente, lo atiende el
coordinador del taller quien solicita al cliente el número de presupuesto realizado.


Posteriormente, consulta los trabajos que se están realizando y determina la fecha en la
cual puede ingresar el nuevo vehículo. El turno asignado se registra en una planilla Excel.
Cuando el cliente lleva el vehículo para la reparación, lo atiende el coordinador de
taller, quien verifica el turno otorgado y recibe la documentación y las llaves del vehículo.
Cuando el vehículo entra a taller, se asigna el trabajo a alguno de los empleados de
taller, responsable de realizar los arreglos.


En cualquier momento previo a llevar el vehículo, el cliente puede cancelar el turno
solicitado.


Para el caso de vehículos asegurados, el coordinador solicita al cliente la
autorización emitida por la compañía de seguros.
Una vez terminado el arreglo, cuando el cliente se presenta a retirar el vehículo, lo
atiende el coordinador del taller, quien le muestra el trabajo realizado. Por otra parte,
informa al Auxiliar Administrativo que prepare la factura por el arreglo.


El Auxiliar Administrativo confecciona la factura y procede a cobrarla si el cliente es
particular. Los pagos son en efectivo o con tarjeta de débito únicamente. Esta factura debe
cumplir con la reglamentación vigente de facturación. Para el caso de pago con tarjeta de
débito existe previamente un acuerdo con las entidades bancarias para operar con esta
modalidad. Una vez acordado esto se obtiene un equipo denominado POSNET con el cual
puede realizarse el cobro con tarjeta de débito que presente el cliente.


Cada vez que sea necesario efectuar al cobro con tarjeta de débito, se pasa la
tarjeta del cliente por el POSNET, se solicita el ingreso de clave al cliente y se espera la
autorización de la entidad crediticia, generando el cupón por el cobro respectivo.


Si el cliente es un asegurado, la factura se emite a nombre de la compañía de
seguro, y el cliente la firma pero no debe pagarla en el taller. En estos casos, luego de la
conformidad del cliente la factura queda archivada para rendirla en forma posterior a la
compañía de seguros.


Finalizado el trámite de facturación, se entrega el vehículo al cliente, devolviendo la
documentación del auto y las llaves, y se dan por terminados los servicios del taller
Al finalizar el día en Administración se emite el listado de ingresos en caja y
semanalmente se envía a cada compañía de seguro las facturas que deben pagarse.


## Objetivo:
Digitalizar y optimizar la gestión del taller


## Entradas:
- Datos Cliente y Vehiculo
- Lista de precios de repuestos 
- Solicitud de turnos 
- Autorizaciones de la compañía de seguros
- Confirmaciones de pago (POSNET)


## Salidas:
- Presupuestos detallados 
- Turnos asignados 
- Cupones de pago 
- Facturas reglamentarias 
- Listado diario de ingresos en caja 
- Listado semanal de facturas para compañías de seguro


## Alcance:
1. Gestión de Clientes y Presupuestos
- 1.1 El sistema debe permitir el registro de los datos del cliente (nombre, teléfono de contacto) y los datos del vehículo (patente, marca, modelo, color).
- 1.2 Debe permitir consultar una lista de precios de repuestos actualizada.
- 1.3 El sistema debe generar un presupuesto detallando los arreglos a realizar, los repuestos necesarios y la duración del trabajo.
- 1.4 En caso de clientes asegurados, el sistema debe incluir en el presupuesto el nombre de la aseguradora y el número de la póliza de seguro.
- 1.5 Debe llevar el control de la vigencia de los presupuestos (hasta 30 días).


2. Gestión de Turnos y Disponibilidad
- 2.1 El sistema debe permitir el registro de la solicitud de turnos vinculada a un número de presupuesto aprobado.
- 2.2 Debe permitir al coordinador visualizar los trabajos en curso para determinar y asignar la fecha de ingreso del nuevo vehículo.
- 2.3 El sistema debe permitir la cancelación del turno solicitado en cualquier momento previo a llevar el vehículo.


3. Operaciones de Taller y Ejecución
- 3.1 El sistema debe registrar el ingreso del vehículo, confirmando la recepción del turno, la documentación, las llaves y (si corresponde) la autorización del seguro.
- 3.2 Debe permitir asignar el trabajo de reparación a uno de los empleados del taller.
- 3.3 El sistema debe permitir registrar la finalización del arreglo para habilitar la etapa de facturación y retiro.


4. Facturación, Pagos y Reportes
- 4.1 El sistema debe emitir facturas cumpliendo con la reglamentación vigente, diferenciando si son para clientes particulares o a nombre de compañías de seguros.
- 4.2 Debe registrar la modalidad de cobro para particulares (efectivo o débito con generación de cupón).
- 4.3 El sistema debe permitir el archivado de facturas firmadas por clientes asegurados para su posterior rendición.
- 4.4 Debe generar un listado diario de ingresos en caja al finalizar el día.
- 4.5 El sistema debe generar semanalmente un reporte con las facturas agrupadas que deben enviarse a cada compañía de seguro para su cobro.


## Límite:
- La gestión interna de las compañías de seguros para aprobar o rechazar los presupuestos.
- La validación crediticia y conexión directa con las entidades bancarias (se delega al equipo POSNET).
- El cumplimiento normativo externo de AFIP (el sistema solo genera la factura según la reglamentación vigente).


## Entorno:
- Clientes (Particulares y Asegurados)
- Coordinador del taller
- Auxiliar Administrativo
- Empleados del taller
- Compañías de Seguros


## Reglas de negocio:
- Atención mediante turnos: La atención para realizar los arreglos se realiza únicamente a través de turnos previos.
- Vigencia del presupuesto: Los presupuestos emitidos tienen una validez máxima de 30 días.
- Requisitos de ingreso: El cliente debe dejar las llaves y la documentación completa y en orden para que el vehículo ingrese al taller.
- Responsabilidad de autorización: Queda a cargo exclusivo del cliente asegurado gestionar la autorización del presupuesto con su compañía de seguros.
- Formas de pago para particulares: Solo se aceptan pagos en efectivo o con tarjeta de débito.
- Cobro a asegurados: Los clientes asegurados no pagan el arreglo en el taller, únicamente firman la factura en señal de conformidad.


## R.N.F.:
- Reglamentación legal: Las facturas emitidas por el sistema deben cumplir estrictamente con la reglamentación de facturación vigente.
- Integración de Hardware: El sistema debe contemplar el registro de operaciones aprobadas por equipos POSNET externos.
- Soporte de planillas: Capacidad para migrar o reemplazar la gestión actual de turnos basada en planillas Excel.

