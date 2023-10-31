
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



## Step 2: Do the next thing

{% comment %} 
Rinse and repeat, adding steps and tasks until the tutorial is complete 
{% endcomment %}

## Next steps

{% comment %} 
Provide a quick recap of what has been accomplished in the quick start as a means of transitioning to next steps. Include 2-3 actionable next steps that the user take after completing the quickstart. Always link to conceptual content on the feature or product. You can also link off to other related information on docs.github.com or in GitHub Skills. 
{% endcomment %}
