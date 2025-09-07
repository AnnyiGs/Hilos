# Hilos (Ejemplo de uso de hilos para la actualización de horas)

Este proyecto contiene un ejemplo de cómo se utilizan hilos en la aplicacion de MovilOil para  el registro de los distribuidores.

Este proyecto demuestra el uso de hilos (threads) en Python para actualizar la hora de diferentes países, específicamente México y China.

## Descripción

En este ejemplo, cada hilo se encarga de obtener y actualizar la hora de un país:

- **Hilo de México:** Actualiza la hora local de México.
- **Hilo de China:** Actualiza la hora local de China.

El sistema está diseñado para ser tolerante a fallas. Si el hilo encargado de actualizar la hora de México falla o deja de funcionar, el sistema sigue operando normalmente utilizando la hora de China.

## Importancia de la hora de China

La hora de China es la más importante en este sistema, ya que la empresa es de nacionalidad china. Por esta razón, en el registro general del sistema siempre se guarda la hora de China, asegurando así la consistencia y confiabilidad de los registros, incluso si el hilo de México presenta fallas.

## Resumen

Este enfoque permite que el sistema sea robusto y continúe funcionando correctamente, priorizando la información más relevante para la empresa (la hora de China), y demostrando cómo los hilos pueden ser utilizados para manejar tareas concurrentes y tolerancia a fallos en aplicaciones reales.





