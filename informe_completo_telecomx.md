# Informe Completo: Análisis Predictivo de Evasión de Clientes - Telecom X

## **Tabla de Contenidos**

1. [Introducción](#introducción)
2. [Metodología](#metodología)
3. [Análisis Exploratorio de Datos](#análisis-exploratorio-de-datos)
4. [Preparación de Datos para Machine Learning](#preparación-de-datos-para-machine-learning)
5. [Modelado Predictivo](#modelado-predictivo)
6. [Evaluación de Modelos](#evaluación-de-modelos)
7. [Interpretación de Resultados](#interpretación-de-resultados)
8. [Conclusiones y Recomendaciones](#conclusiones-y-recomendaciones)
9. [Anexos](#anexos)

---

## **1. Introducción**

### **1.1 Contexto del Problema**

Telecom X, una empresa de telecomunicaciones, enfrenta un desafío crítico: **la alta tasa de evasión de clientes (churn)**. La pérdida de clientes representa no solo una reducción en ingresos recurrentes, sino también costos significativos asociados a la adquisición de nuevos clientes.

### **1.2 Objetivos del Análisis**

- **Identificar** los factores que influyen en la cancelación de servicios
- **Desarrollar** un modelo predictivo capaz de anticipar el churn
- **Proporcionar** recomendaciones estratégicas para reducir la evasión
- **Establecer** un framework para la implementación de estrategias de retención

### **1.3 Alcance del Proyecto**

El análisis abarca:
- Datos de 7,267 clientes de Telecom X
- Variables demográficas, de servicios y comportamiento
- Desarrollo de modelos de clasificación binaria
- Evaluación de rendimiento y interpretación de resultados

---

## **2. Metodología**

### **2.1 Enfoque General**

Se siguió una metodología estructurada que incluye:

1. **Análisis Exploratorio de Datos (EDA)**
2. **Preparación y Limpieza de Datos**
3. **Desarrollo de Modelos Predictivos**
4. **Evaluación y Comparación de Modelos**
5. **Interpretación y Recomendaciones**

### **2.2 Herramientas Utilizadas**

- **Python** como lenguaje principal
- **Pandas** para manipulación de datos
- **Scikit-learn** para modelado de Machine Learning
- **Matplotlib/Seaborn** para visualizaciones
- **SMOTE** para balanceo de clases

---

## **3. Análisis Exploratorio de Datos**

### **3.1 Descripción del Dataset**

El dataset original contenía 7,267 registros con 6 columnas principales:
- `customerID`: Identificador único del cliente
- `Churn`: Variable objetivo (Yes/No)
- `customer`: Información demográfica del cliente
- `phone`: Servicios de telefonía
- `internet`: Servicios de internet
- `account`: Información de facturación y contrato

### **3.2 Proceso de Limpieza**

#### **3.2.1 Desanidado de Columnas**
Las columnas `customer`, `phone`, `internet` y `account` contenían diccionarios anidados que fueron expandidos para obtener un total de 22 variables predictoras.

#### **3.2.2 Estandarización de Datos**
- Conversión de variables categóricas "Yes"/"No" a valores binarios (1/0)
- Conversión de variables numéricas a tipo float/int
- Manejo de valores faltantes mediante imputación

### **3.3 Hallazgos del EDA**

#### **3.3.1 Distribución de Churn**
- **Tasa de churn:** 26.5% (1,869 clientes)
- **Clientes retenidos:** 73.5% (5,398 clientes)

#### **3.3.2 Factores de Riesgo Identificados**

**Variables Categóricas:**
- **Tipo de contrato:** Contratos mensuales tienen mayor tasa de churn
- **Método de pago:** "Electronic check" asociado a mayor evasión
- **Servicio de internet:** "Fiber optic" presenta mayor riesgo
- **Género:** No hay diferencia significativa

**Variables Numéricas:**
- **Antigüedad (tenure):** Clientes nuevos (< 18 meses) tienen mayor riesgo
- **Cargos mensuales:** Clientes con cargos altos tienden a cancelar
- **Cargos totales:** Clientes con bajo total acumulado (recién llegados) son más propensos

---

## **4. Preparación de Datos para Machine Learning**

### **4.1 Encoding de Variables Categóricas**

Se aplicó **One-Hot Encoding** a todas las variables categóricas utilizando `pd.get_dummies()` con `drop_first=True` para evitar multicolinealidad.

### **4.2 Balanceo de Clases**

Se utilizó **SMOTE (Synthetic Minority Over-sampling Technique)** para balancear las clases, ya que la distribución original mostraba un desbalance significativo (26.5% vs 73.5%).

### **4.3 División Train/Test**

- **Conjunto de entrenamiento:** 70% de los datos
- **Conjunto de prueba:** 30% de los datos
- **Estratificación:** Manteniendo la proporción de clases

---

## **5. Modelado Predictivo**

### **5.1 Modelos Evaluados**

#### **5.1.1 Regresión Logística**
- **Ventajas:** Interpretabilidad, rapidez de entrenamiento
- **Desventajas:** Asume relaciones lineales
- **Preprocesamiento:** Normalización requerida

#### **5.1.2 Random Forest**
- **Ventajas:** Maneja relaciones no lineales, robusto a outliers
- **Desventajas:** Menos interpretable, mayor tiempo de entrenamiento
- **Preprocesamiento:** No requiere normalización

### **5.2 Configuración de Modelos**

```python
# Regresión Logística
logreg = LogisticRegression(max_iter=1000, random_state=42)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
```

---

## **6. Evaluación de Modelos**

### **6.1 Métricas de Evaluación**

Se utilizaron las siguientes métricas para evaluar el rendimiento:

- **Accuracy:** Proporción de predicciones correctas
- **Precision:** Proporción de predicciones positivas correctas
- **Recall:** Proporción de casos positivos identificados correctamente
- **F1-Score:** Media armónica de precision y recall
- **AUC-ROC:** Área bajo la curva ROC

### **6.2 Resultados Comparativos**

| Métrica | Regresión Logística | Random Forest |
|---------|-------------------|---------------|
| Accuracy | 83% | **86%** |
| Precision | 81% | **85%** |
| Recall | 85% | **86%** |
| F1-Score | 83% | **86%** |
| AUC-ROC | 0.89 | **0.93** |

### **6.3 Matriz de Confusión - Random Forest**

```
                Predicho
              No    Sí
Real No     1317   232
Real Sí     212   1337
```

**Interpretación:**
- **Verdaderos Positivos:** 1,337 (clientes que cancelaron y fueron predichos correctamente)
- **Verdaderos Negativos:** 1,317 (clientes que no cancelaron y fueron predichos correctamente)
- **Falsos Positivos:** 232 (clientes que no cancelaron pero fueron predichos como churn)
- **Falsos Negativos:** 212 (clientes que cancelaron pero no fueron predichos)

---

## **7. Interpretación de Resultados**

### **7.1 Importancia de Variables - Random Forest**

**Top 10 Variables Más Importantes:**

1. **customer_tenure** (13.5%): Antigüedad del cliente
2. **account_Charges.Total** (13.1%): Cargos totales acumulados
3. **account_Charges.Monthly** (12.0%): Cargos mensuales
4. **account_Contract_Two year** (5.7%): Contrato de dos años
5. **account_PaperlessBilling** (5.2%): Facturación electrónica
6. **internet_TechSupport_Yes** (4.6%): Soporte técnico de internet
7. **customer_Partner** (4.5%): Cliente con pareja
8. **internet_OnlineSecurity_Yes** (4.3%): Seguridad online
9. **account_Contract_One year** (4.1%): Contrato de un año
10. **customer_Dependents** (3.8%): Cliente con dependientes

### **7.2 Coeficientes - Regresión Logística**

**Variables con Mayor Impacto Positivo (aumentan probabilidad de churn):**
- `account_Charges.Monthly` (5.33): Cargos mensuales altos
- `account_Charges.Total` (1.41): Cargos totales
- `account_PaperlessBilling` (0.14): Facturación electrónica

### **7.3 Insights Clave**

1. **Antigüedad es el factor más importante:** Los clientes nuevos tienen mayor riesgo
2. **Cargos mensuales altos son un riesgo:** Especialmente para clientes nuevos
3. **Contratos largos protegen:** Reducen significativamente el riesgo de churn
4. **Servicios adicionales retienen:** Soporte técnico y seguridad online
5. **Factores familiares importan:** Tener pareja o dependientes reduce el riesgo

---

## **8. Conclusiones y Recomendaciones**

### **8.1 Conclusiones Principales**

1. **El modelo Random Forest es superior** con un accuracy del 86% y AUC-ROC de 0.93
2. **La antigüedad del cliente es el predictor más fuerte** de evasión
3. **Los contratos mensuales representan mayor riesgo** que los contratos largos
4. **Los cargos mensuales altos** están asociados con mayor probabilidad de churn
5. **Los servicios de soporte y seguridad** contribuyen a la retención

### **8.2 Recomendaciones Estratégicas**

#### **8.2.1 Acciones Inmediatas (0-3 meses)**

1. **Programa de Fidelización para Clientes Nuevos**
   - Implementar seguimiento personalizado en los primeros 6 meses
   - Ofrecer incentivos especiales para renovación temprana
   - Crear programa de bienvenida con beneficios exclusivos

2. **Revisión de Estructura de Precios**
   - Analizar cargos mensuales altos y su justificación
   - Considerar descuentos progresivos por antigüedad
   - Implementar planes de pago flexibles

3. **Incentivos para Contratos Largos**
   - Descuentos significativos para contratos anuales/bienales
   - Beneficios exclusivos para clientes con contratos largos
   - Penalizaciones menores por cancelación anticipada

#### **8.2.2 Acciones de Mediano Plazo (3-6 meses)**

1. **Campañas Personalizadas Basadas en Predicciones**
   - Identificar clientes en riesgo usando el modelo
   - Desarrollar estrategias específicas por segmento
   - Implementar sistema de alertas tempranas

2. **Mejora de Servicios de Soporte**
   - Promover activamente servicios de soporte técnico
   - Mejorar calidad y accesibilidad del soporte
   - Ofrecer servicios de seguridad online como valor agregado

3. **Sistema de Monitoreo Continuo**
   - Dashboard para seguimiento de métricas de churn
   - Alertas automáticas para clientes en riesgo
   - Reportes semanales de tendencias

#### **8.2.3 Acciones de Largo Plazo (6+ meses)**

1. **Integración con Sistemas CRM**
   - Incorporar predicciones en el sistema de gestión de clientes
   - Automatizar acciones de retención
   - Seguimiento de efectividad de estrategias

2. **Desarrollo de Estrategias de Upselling**
   - Identificar oportunidades de venta cruzada
   - Desarrollar productos complementarios
   - Crear programas de lealtad avanzados

### **8.3 Métricas de Éxito**

- **Reducción del 15-20%** en la tasa de churn
- **Aumento del 10-15%** en ingresos por retención
- **Mejora del 20%** en satisfacción del cliente
- **Reducción del 25%** en costos de adquisición

---

## **9. Anexos**

### **9.1 Código del Modelo**

```python
# Código completo del pipeline de Machine Learning
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import pickle

# Cargar datos
data = pd.read_csv('telecomx_tratado.csv')

# Preparar datos
X = data.drop(['customerID', 'Churn'], axis=1)
y = data['Churn'].map({'Yes': 1, 'No': 0})

# Balancear clases
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X, y)

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X_res, y_res, test_size=0.3, random_state=42, stratify=y_res
)

# Entrenar modelo
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Evaluar modelo
y_pred = rf.predict(X_test)
print(classification_report(y_test, y_pred))

# Guardar modelo
with open('random_forest_telecomx.pkl', 'wb') as f:
    pickle.dump(rf, f)
```

### **9.2 Glosario de Términos**

- **Churn:** Cancelación de servicios por parte del cliente
- **Accuracy:** Precisión general del modelo
- **Precision:** Proporción de predicciones positivas correctas
- **Recall:** Sensibilidad del modelo
- **AUC-ROC:** Área bajo la curva ROC
- **SMOTE:** Técnica de sobremuestreo sintético
- **One-Hot Encoding:** Codificación de variables categóricas

---

**Este informe proporciona una base sólida para la implementación de estrategias de retención de clientes en Telecom X, basadas en evidencia empírica y análisis predictivo avanzado.** 