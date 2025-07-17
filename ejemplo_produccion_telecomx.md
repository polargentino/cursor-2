# Ejemplo de Uso del Modelo en Producción - Telecom X

## **Descripción**

Este documento muestra cómo implementar el modelo de predicción de churn en un entorno de producción, incluyendo ejemplos de código para hacer predicciones sobre nuevos clientes.

---

## **1. Cargar el Modelo Guardado**

```python
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Cargar el modelo entrenado
with open('random_forest_telecomx.pkl', 'rb') as f:
    model = pickle.load(f)

print("Modelo cargado exitosamente!")
```

---

## **2. Función para Preparar Datos de Nuevos Clientes**

```python
def prepare_new_customer_data(customer_data):
    """
    Prepara los datos de un nuevo cliente para la predicción.
    
    Args:
        customer_data (dict): Diccionario con los datos del cliente
        
    Returns:
        pandas.DataFrame: Datos preparados para predicción
    """
    
    # Crear DataFrame con los datos del cliente
    df = pd.DataFrame([customer_data])
    
    # Aplicar One-Hot Encoding para variables categóricas
    categorical_cols = ['customer_gender', 'phone_MultipleLines', 
                       'internet_InternetService', 'internet_OnlineSecurity',
                       'internet_OnlineBackup', 'internet_DeviceProtection',
                       'internet_TechSupport', 'internet_StreamingTV',
                       'internet_StreamingMovies', 'account_Contract',
                       'account_PaymentMethod']
    
    # Asegurar que todas las columnas categóricas estén presentes
    for col in categorical_cols:
        if col not in df.columns:
            df[col] = 0
    
    # Aplicar get_dummies
    df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    # Asegurar que todas las columnas del modelo estén presentes
    expected_columns = [
        'customer_SeniorCitizen', 'customer_Partner', 'customer_Dependents',
        'customer_tenure', 'phone_PhoneService', 'account_PaperlessBilling',
        'account_Charges.Monthly', 'account_Charges.Total',
        'customer_gender_Male', 'phone_MultipleLines_No phone service',
        'phone_MultipleLines_Yes', 'internet_InternetService_Fiber optic',
        'internet_InternetService_No', 'internet_OnlineSecurity_No internet service',
        'internet_OnlineSecurity_Yes', 'internet_OnlineBackup_No internet service',
        'internet_OnlineBackup_Yes', 'internet_DeviceProtection_No internet service',
        'internet_DeviceProtection_Yes', 'internet_TechSupport_No internet service',
        'internet_TechSupport_Yes', 'internet_StreamingTV_No internet service',
        'internet_StreamingTV_Yes', 'internet_StreamingMovies_No internet service',
        'internet_StreamingMovies_Yes', 'account_Contract_One year',
        'account_Contract_Two year', 'account_PaymentMethod_Credit card (automatic)',
        'account_PaymentMethod_Electronic check', 'account_PaymentMethod_Mailed check'
    ]
    
    # Agregar columnas faltantes con valor 0
    for col in expected_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    
    # Reordenar columnas según el orden esperado por el modelo
    df_encoded = df_encoded[expected_columns]
    
    return df_encoded
```

---

## **3. Función para Predecir Churn**

```python
def predict_churn(customer_data):
    """
    Predice si un cliente tiene probabilidad de hacer churn.
    
    Args:
        customer_data (dict): Datos del cliente
        
    Returns:
        dict: Resultado de la predicción con probabilidad
    """
    
    try:
        # Preparar datos
        X_new = prepare_new_customer_data(customer_data)
        
        # Hacer predicción
        prediction = model.predict(X_new)[0]
        probability = model.predict_proba(X_new)[0]
        
        # Interpretar resultado
        churn_probability = probability[1]  # Probabilidad de churn
        risk_level = "Alto" if churn_probability > 0.7 else "Medio" if churn_probability > 0.4 else "Bajo"
        
        result = {
            "prediction": "Churn" if prediction == 1 else "No Churn",
            "churn_probability": round(churn_probability * 100, 2),
            "no_churn_probability": round(probability[0] * 100, 2),
            "risk_level": risk_level,
            "recommendation": get_recommendation(churn_probability, customer_data)
        }
        
        return result
        
    except Exception as e:
        return {"error": f"Error en la predicción: {str(e)}"}
```

---

## **4. Función para Generar Recomendaciones**

```python
def get_recommendation(churn_probability, customer_data):
    """
    Genera recomendaciones basadas en la probabilidad de churn y datos del cliente.
    
    Args:
        churn_probability (float): Probabilidad de churn (0-1)
        customer_data (dict): Datos del cliente
        
    Returns:
        list: Lista de recomendaciones
    """
    
    recommendations = []
    
    # Recomendaciones basadas en probabilidad de churn
    if churn_probability > 0.7:
        recommendations.append("🚨 CLIENTE DE ALTO RIESGO - Acción inmediata requerida")
        recommendations.append("Contactar al cliente dentro de las próximas 24 horas")
        recommendations.append("Ofrecer descuento especial o incentivo de retención")
    elif churn_probability > 0.4:
        recommendations.append("⚠️ CLIENTE DE RIESGO MEDIO - Monitoreo activo")
        recommendations.append("Programar llamada de seguimiento en la próxima semana")
        recommendations.append("Ofrecer mejora en el plan actual")
    else:
        recommendations.append("✅ CLIENTE DE BAJO RIESGO - Mantener satisfacción")
        recommendations.append("Continuar con el servicio actual")
        recommendations.append("Considerar estrategias de upselling")
    
    # Recomendaciones específicas basadas en datos del cliente
    if customer_data.get('customer_tenure', 0) < 12:
        recommendations.append("Cliente nuevo - Implementar programa de bienvenida")
    
    if customer_data.get('account_Contract') == 'Month-to-month':
        recommendations.append("Contrato mensual - Ofrecer descuento por contrato anual")
    
    if customer_data.get('account_Charges.Monthly', 0) > 70:
        recommendations.append("Cargos mensuales altos - Revisar plan y ofrecer alternativas")
    
    if customer_data.get('internet_TechSupport') != 'Yes':
        recommendations.append("Sin soporte técnico - Ofrecer servicio de soporte gratuito")
    
    return recommendations
```

---

## **5. Ejemplos de Uso**

### **Ejemplo 1: Cliente de Alto Riesgo**

```python
# Datos de un cliente con alto riesgo de churn
high_risk_customer = {
    'customer_SeniorCitizen': 0,
    'customer_Partner': 0,
    'customer_Dependents': 0,
    'customer_tenure': 3,  # Cliente nuevo
    'phone_PhoneService': 1,
    'account_PaperlessBilling': 1,
    'account_Charges.Monthly': 85.0,  # Cargos altos
    'account_Charges.Total': 255.0,
    'customer_gender': 'Male',
    'phone_MultipleLines': 'No',
    'internet_InternetService': 'Fiber optic',  # Servicio de alto riesgo
    'internet_OnlineSecurity': 'No',
    'internet_OnlineBackup': 'No',
    'internet_DeviceProtection': 'No',
    'internet_TechSupport': 'No',
    'internet_StreamingTV': 'Yes',
    'internet_StreamingMovies': 'Yes',
    'account_Contract': 'Month-to-month',  # Contrato de alto riesgo
    'account_PaymentMethod': 'Electronic check'  # Método de alto riesgo
}

result = predict_churn(high_risk_customer)
print("=== CLIENTE DE ALTO RIESGO ===")
print(f"Predicción: {result['prediction']}")
print(f"Probabilidad de Churn: {result['churn_probability']}%")
print(f"Nivel de Riesgo: {result['risk_level']}")
print("\nRecomendaciones:")
for rec in result['recommendation']:
    print(f"- {rec}")
```

**Salida esperada:**
```
=== CLIENTE DE ALTO RIESGO ===
Predicción: Churn
Probabilidad de Churn: 89.50%
Nivel de Riesgo: Alto

Recomendaciones:
- 🚨 CLIENTE DE ALTO RIESGO - Acción inmediata requerida
- Contactar al cliente dentro de las próximas 24 horas
- Ofrecer descuento especial o incentivo de retención
- Cliente nuevo - Implementar programa de bienvenida
- Contrato mensual - Ofrecer descuento por contrato anual
- Cargos mensuales altos - Revisar plan y ofrecer alternativas
- Sin soporte técnico - Ofrecer servicio de soporte gratuito
```

### **Ejemplo 2: Cliente de Bajo Riesgo**

```python
# Datos de un cliente con bajo riesgo de churn
low_risk_customer = {
    'customer_SeniorCitizen': 0,
    'customer_Partner': 1,
    'customer_Dependents': 1,
    'customer_tenure': 48,  # Cliente de larga data
    'phone_PhoneService': 1,
    'account_PaperlessBilling': 1,
    'account_Charges.Monthly': 45.0,  # Cargos moderados
    'account_Charges.Total': 2160.0,  # Alto total acumulado
    'customer_gender': 'Female',
    'phone_MultipleLines': 'Yes',
    'internet_InternetService': 'DSL',  # Servicio estable
    'internet_OnlineSecurity': 'Yes',
    'internet_OnlineBackup': 'Yes',
    'internet_DeviceProtection': 'Yes',
    'internet_TechSupport': 'Yes',
    'internet_StreamingTV': 'No',
    'internet_StreamingMovies': 'No',
    'account_Contract': 'Two year',  # Contrato largo
    'account_PaymentMethod': 'Credit card (automatic)'  # Pago automático
}

result = predict_churn(low_risk_customer)
print("\n=== CLIENTE DE BAJO RIESGO ===")
print(f"Predicción: {result['prediction']}")
print(f"Probabilidad de Churn: {result['churn_probability']}%")
print(f"Nivel de Riesgo: {result['risk_level']}")
print("\nRecomendaciones:")
for rec in result['recommendation']:
    print(f"- {rec}")
```

**Salida esperada:**
```
=== CLIENTE DE BAJO RIESGO ===
Predicción: No Churn
Probabilidad de Churn: 12.30%
Nivel de Riesgo: Bajo

Recomendaciones:
- ✅ CLIENTE DE BAJO RIESGO - Mantener satisfacción
- Continuar con el servicio actual
- Considerar estrategias de upselling
```

---

## **6. Implementación en Sistema de Producción**

### **6.1 API REST (Ejemplo con Flask)**

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict_churn', methods=['POST'])
def predict_churn_api():
    """
    Endpoint para predecir churn de clientes
    """
    try:
        # Obtener datos del cliente desde la request
        customer_data = request.json
        
        # Hacer predicción
        result = predict_churn(customer_data)
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### **6.2 Uso de la API**

```bash
curl -X POST http://localhost:5000/predict_churn \
  -H "Content-Type: application/json" \
  -d '{
    "customer_tenure": 3,
    "account_Charges.Monthly": 85.0,
    "account_Contract": "Month-to-month",
    "internet_InternetService": "Fiber optic"
  }'
```

---

## **7. Monitoreo y Mantenimiento**

### **7.1 Métricas de Monitoreo**

- **Accuracy del modelo** en datos nuevos
- **Distribución de predicciones** (para detectar drift)
- **Tiempo de respuesta** de las predicciones
- **Tasa de errores** en la API

### **7.2 Retraining del Modelo**

```python
def retrain_model(new_data):
    """
    Función para reentrenar el modelo con nuevos datos
    """
    # Combinar datos históricos con nuevos datos
    # Reentrenar modelo
    # Validar rendimiento
    # Reemplazar modelo en producción
    pass
```

---

## **8. Consideraciones de Seguridad**

- **Validación de datos** de entrada
- **Autenticación** para acceso a la API
- **Logging** de todas las predicciones
- **Backup** del modelo
- **Versionado** de modelos

---

**Este ejemplo proporciona un framework completo para implementar el modelo de predicción de churn en un entorno de producción real.** 