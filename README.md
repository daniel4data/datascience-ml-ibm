# Reto de Clustering - Segmentación de empleados

## 🎯 Objetivo
Aplicar técnicas de aprendizaje no supervisado (K-Means) para segmentar a los empleados según sus características y analizar la tasa de deserción (`Attrition_rate`) por grupo.
En este reto, la tarea es agrupar a los empleados y brindar una interpretación de los grupos obtenidos, tomando como una de las var iables más relevantes para la descripción de los resultados la ratio de deserción (Attrition_rate). 

## 📊 Pasos realizados
1. Limpieza de datos e imputación de valores faltantes.
2. Codificación de variables categóricas con OneHotEncoder.
3. Escalado de variables numéricas con StandardScaler.
4. Aplicación de K-Means para segmentar empleados.
5. Determinación del número óptimo de clusters con métodos Elbow y Silhouette.
6. Interpretación de resultados y visualización.

## 🧠 Conclusión
A través de un análisis de segmentación usando K-Means (con k = 4), agrupamos empleados según múltiples características con la finalidad de explorar diferencias en la tasa de deserción entre grupos
Los resultados muestran que, aunque la variación entre tasas promedio de deserción por grupo es moderada (entre 18.3% y 19.9%), es posible identificar patrones:
* El grupo 2, que presentó el mayor sueldo promedio, también mostró la mayor tasa de deserción. Esto sugiere que el salario por sí solo no asegura que el individuo no deserte
* El grupo 3, con sueldos moderados y más años de servicio, presentó la menor tasa de deserción. Es posible que exista una mayor fidelidad asociada a la antigüedad o a otros factores no financieros como el balance vida-trabajo