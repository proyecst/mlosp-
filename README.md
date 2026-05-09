# mlosp-Engine de Inferencia GenAI (RAG) con Amazon Bedrock
Directorio: /genai-rag-engine

🎯 Problema
La gestión de servidores GPU dedicados para tareas de inferencia de modelos de lenguaje (LLM) genera costos fijos elevados y complejidad operativa innecesaria para muchas aplicaciones.

🚀 Solución
Implementé un motor de inferencia 100% Serverless utilizando Amazon Bedrock. Esta arquitectura utiliza AWS Lambda para orquestar llamadas a modelos líderes (como Claude 3) mediante una API, eliminando la necesidad de gestionar infraestructura base.  

🛠️ Stack Técnico
Modelos: Claude 3 (Anthropic) vía Amazon Bedrock.  

Compute: AWS Lambda (Python 3.12).  

Orquestación: Boto3 (AWS SDK).  

📈 Resultados de Negocio
Costo: Modelo de pago por uso (Pay-as-you-go), reduciendo gastos operativos en un 70%.  

Escalabilidad: Manejo automático de picos de demanda sin intervención manual.  

2. Automatización del Ciclo de Vida (E2E MLOps Pipeline)
Directorio: /mlops-pipeline-automation

🎯 Problema
El entrenamiento y despliegue manual de modelos (como los utilizados en Nexus Alpha) causa inconsistencias, falta de trazabilidad y retrasos en la puesta en producción.  

🚀 Solución
Diseñé un pipeline de CI/CD para Machine Learning usando SageMaker Pipelines. El sistema automatiza desde la ingesta de datos en S3 hasta el registro del modelo en el Model Registry, garantizando que cada versión sea reproducible.  

🛠️ Stack Técnico
Orquestador: SageMaker Pipelines.  

Almacenamiento: Amazon S3.  

Framework: PyTorch / Scikit-Learn.  

📈 Resultados de Negocio
Velocidad: Reducción del ciclo de despliegue de días a minutos.  

Gobernanza: Registro histórico de cada experimento, facilitando auditorías y auditoría de modelos.  

3. Observabilidad y Detección de Drift (Model Monitor)
Directorio: /model-observability

🎯 Problema
La degradación de los datos (Data Drift) en producción hace que los modelos pierdan precisión silenciosamente, afectando la confiabilidad de los sistemas inteligentes.  

🚀 Solución
Implementé un sistema de monitoreo continuo con SageMaker Model Monitor. El sistema compara los datos de entrada en tiempo real con el "baseline" de entrenamiento y dispara alertas automáticas si detecta anomalías estadísticas.  

🛠️ Stack Técnico
Monitoreo: SageMaker Model Monitor.  

Alertas: Amazon CloudWatch + SNS.  

Analítica: Estadísticas de línea base (Baselines).  

📈 Resultados de Negocio
Fiabilidad: Garantía de calidad de las predicciones en tiempo real.  

Mantenimiento: Reducción del 40% en tiempo de supervisión manual mediante alertas automatizadas.
