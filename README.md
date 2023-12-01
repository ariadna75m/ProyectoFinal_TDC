## Introducción

La arquitectura del flujo de trabajo para la librería en línea se muestra en la Figura 1.1 y gira en torno a un motor de flujo de trabajo. Los componentes del flujo de trabajo tienen interfaces de aplicación que proporcionan medios estándar de comunicación entre estos componentes y el motor de flujo de trabajo. Todos los componentes del flujo de trabajo tienen funciones específicas que desempeñar en un flujo de trabajo.

- La Herramienta de Definición de Procesos se utiliza en la etapa de diseño para especificar el proceso. La definición del proceso contiene información sobre las tareas, sus condiciones de inicio y finalización, y reglas y dependencias para la navegación entre tareas.
- La Herramienta de Administración y Monitoreo se utiliza para gestionar usuarios, roles, políticas de seguridad y para realizar un seguimiento e informar sobre los estados del flujo de trabajo y la generación de datos.

## Workflow identificado

El flujo de trabajo lee la información de las definiciones de proceso. Esta información es utilizada por el motor para determinar los pasos que deben realizarse y presentarlos al usuario a través de una interfaz de usuario. Luego, el usuario toma la acción apropiada y notifica al motor de flujo de trabajo. Basándose en la acción del usuario, el motor determina los pasos futuros a tomar. Cuando se completan todos los pasos, el flujo de trabajo termina.

![image](https://github.com/ariadna75m/ProyectoFinal_TDC/assets/83561363/7cd53f8d-db4d-4ab1-87c2-2dbf13a7f7ed)

La librería en línea tiene un grupo de editores que suministran libros a la librería en línea cuando se realizan pedidos. La librería tiene acceso a las bases de datos de estos editores. El cliente realiza un pedido (Pedido) en la librería. La librería verifica la disponibilidad del libro con un editor accediendo a la base de datos del editor. Si el libro está disponible, la librería transfiere el pedido al editor (Pedir Libro). 

Si el libro no está disponible, la librería decide buscar a otro editor alternativo o rechazar el pedido. Al mismo tiempo, la librería verifica la información de la tarjeta de crédito proporcionada por el usuario (Autorización de Tarjeta de Crédito). Si el libro está disponible y la información de la tarjeta de crédito proporcionada por el usuario es correcta, se informa al cliente y la librería continúa procesando el pedido. Luego, el editor prepara el libro para su envío y lo envía. Luego, se notifica a la librería en línea y la librería en línea o su empresa de facturación luego procesa el pago (Procesar Pago). Hemos identificado las siguientes tareas en este flujo de trabajo.

- Tarea 1: Pedido
- Tarea 2: Autorización de Tarjeta de Crédito
- Tarea 3: Pedir Libro (editor)
- Tarea 4: Cancelar Pedido (Editor)
- Tarea 5: Enviar Pedido
- Tarea 6: Procesar Pago
- Tarea 7: Préstamo del libro

### Diagrama de máquina de estados

Un Diagrama de máquina de estados está relacionado a los autómatas, ya que se utiliza para representar y visualizar el comportamiento de un autómata o una máquina de estados finitos. Estos diagramas son una herramienta gráfica comúnmente utilizada en la teoría de autómatas y en la ingeniería de software para modelar y comprender el comportamiento de sistemas que pueden estar en diferentes estados y realizar transiciones entre esos estados en respuesta a eventos o condiciones específicas. Los diagramas de máquina de estados ayudan a representar visualmente cómo funciona un sistema o proceso en términos de sus estados y las transiciones entre ellos.

- Proceso de préstamo de libros
  
  ![image](https://github.com/ariadna75m/ProyectoFinal_TDC/assets/83561363/9ad803c9-9eb4-4b77-8e00-a2359527c003)

- Compra de libros (usuraio)

  ![image](https://github.com/ariadna75m/ProyectoFinal_TDC/assets/83561363/c211284b-deee-4872-a8ce-282c4198ed20)

- Proceso de compra

  ![image](https://github.com/ariadna75m/ProyectoFinal_TDC/assets/83561363/e033d1da-5fb3-4aa6-9daa-40b285473239)

    - Este diagrama se interpreta con los siguientes pasos
      - La Autorización de Tarjeta de Crédito no puede comenzar hasta que se inicie la Colocación del Pedido (T2 BD T1).
      - El Pedido de Libros con el editor no puede comenzar hasta que se inicie la Colocación del Pedido (T3 BD T1).
      - Si la Autorización de Tarjeta de Crédito se interrumpe, entonces el Pedido de Libros con el editor también debe interrumpirse (T2 AD T3).
      - El Pedido de Libros con el editor no puede confirmar ni interrumpir hasta que la Autorización de Tarjeta de Crédito confirme o interrumpa (T3 TD T2).
      - Enviar el Libro al Transportista no puede comenzar a ejecutarse hasta que el Pedido de Libros con el editor confirme o se interrumpa (T5 SD T3).
      - Encontrar un Transportista no puede comenzar hasta que se inicie la Colocación del Pedido (T4 BD T1).
      - Si la tarea de Encontrar un Transportista se interrumpe, entonces la tarea de Enviar el Libro al Transportista debe interrumpirse (T4 AD T5).
      - Si tanto la tarea de Encontrar un Transportista como la tarea de Enviar el Libro al Transportista confirman, entonces la tarea de Encontrar un Transportista confirma primero (T4 CD T5).
      - La Cancelación del Pedido de libros con el editor no puede comenzar a ejecutarse hasta que la tarea de Encontrar un Transportista se interrumpa (T4 BAD T6).
      - Si la tarea de Encontrar un Transportista se interrumpe, entonces la tarea de Cancelación del Pedido de libros con el editor se confirma (T6 FCAD T4).
      - La tarea de Enviar el Pedido no puede comenzar a ejecutarse hasta que la tarea de Enviar el Libro al Transportista confirme o se interrumpa (T7 SD T5).
      - La tarea de Enviar el Pedido no puede comenzar a ejecutarse hasta que la tarea de Encontrar un Transportista confirme o se interrumpa (T7 SD T4).
      - La tarea de Procesar el Pago no puede comenzar hasta que comience la tarea de Enviar el Pedido (T8 BD T7).
      - Si la tarea de Procesar el Pago se interrumpe, entonces la tarea de Enviar el Pedido también debe interrumpirse (T8 AD T7).
      - La tarea de Enviar el Pedido no puede confirmar ni interrumpir hasta que la tarea de Procesar el Pago confirme o interrumpa (T7 TD T8).

## Problema identificado

En este momento, hay dos enfoques que una empresa puede adoptar. El primer enfoque es que si la negativa del editor de cancelar el pedido es inaceptable, los términos del acuerdo comercial entre las dos partes involucradas deben modificarse. En este caso, significa que la librería en línea puede cancelar el pedido con el editor en cualquier momento de la transacción, es decir, la librería puede forzar que la tarea de Cancelar Pedido se lleve a cabo. Esto implica adoptar una estructura de tarea diferente. Esta estructura de tarea no tendrá un evento de aborto incontrolable que pueda interrumpir la tarea de cancelar el pedido durante su ejecución. La estructura actual y la estructura de tarea sugerida para Cancelar Pedido se muestran 

![image](https://github.com/ariadna75m/ProyectoFinal_TDC/assets/83561363/4486eaf6-c464-40e0-92f6-9d5941b93bf9)

El segundo enfoque consiste en aceptar la política actual de que la cancelación del pedido no puede ser forzada a ejecutarse. Esto podría resultar en pérdidas para la empresa. Con este enfoque, la dependencia FCAD entre las tareas Buscar Transportista y Cancelar Pedido no puede ser impuesta. El patrón de control y el reconocedor para el supervisor con este enfoque se muestra en la imagen.

Primer Enfoque: Modificación de Términos de Acuerdo Comercial
Situación:
Desafío: La negativa del editor a cancelar un pedido es inaceptable para la empresa.
Solución Propuesta: Modificar los términos del acuerdo comercial para permitir a la empresa cancelar pedidos con el editor en cualquier momento.
Implicaciones:
La librería en línea puede forzar la cancelación del pedido en cualquier momento durante la transacción.
Estructura de Tarea Actual vs. Estructura Sugerida:
Estructura Actual: La tarea de "Cancelar Pedido" tiene un evento de aborto incontrolable que podría interrumpir la tarea durante su ejecución.
Estructura Sugerida: Se propone una nueva estructura de tarea sin un evento de aborto incontrolable, lo que significa que no hay eventos imprevistos que puedan interrumpir la tarea de cancelar el pedido.

El primer autómata representa la estructura actual de tareas para la cancelación de un pedido. Tiene tres estados: "Buscar Transportista", "Cancelar Pedido" y "Pedido Cancelado". El autómata muestra que la tarea de "Buscar Transportista" debe completarse antes de que se pueda realizar la tarea de "Cancelar Pedido". Una vez que se completa la tarea de "Cancelar Pedido", el estado cambia a "Pedido Cancelado".

El segundo autómata muestra la estructura de tarea sugerida para la cancelación del pedido. También tiene tres estados: "Buscar Transportista", "Cancelar Pedido" y "Pedido Cancelado". Sin embargo, en este caso, no se impone una dependencia entre las tareas "Buscar Transportista" y "Cancelar Pedido". Esto significa que la tarea de "Cancelar Pedido" puede llevarse a cabo sin necesidad de completar la tarea de "Buscar Transportista". El estado cambia a "Pedido Cancelado" una vez que se completa la tarea de "Cancelar Pedido".

## Referencias
Nos guiamos de este proyecto de github, hicimos los cambios necesarios para que funcione todo perfectamente, habia algunas cosas desactualizadas, https://github.com/Nitin-0205/Library-Management-System.

