from sagemaker.model_monitor import DefaultModelMonitor
from sagemaker.model_monitor.dataset_format import DatasetFormat

# Configuramos el monitor de datos
my_monitor = DefaultModelMonitor(
    role='AmazonSageMaker-ExecutionRole',
    instance_count=1,
    instance_type='ml.m5.large',
    volume_size_in_gb=20,
    max_runtime_in_seconds=3600,
)

# Creamos una programación para que corra cada hora o día
my_monitor.create_monitoring_schedule(
    monitor_schedule_name="DeteccionDeDriftDiaria",
    endpoint_input="tu-endpoint-de-produccion",
    output_s3_uri="s3://tu-bucket-mlops/monitoring/reports",
    statistics=my_monitor.baseline_statistics(),
    constraints=my_monitor.suggested_constraints(),
    schedule_cron_expression="cron(0 0 * * ? *)", # Corre cada medianoche
    enable_cloudwatch_metrics=True
)