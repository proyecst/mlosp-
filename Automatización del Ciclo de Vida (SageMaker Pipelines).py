from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import TrainingStep
from sagemaker.estimator import Estimator
from sagemaker.inputs import TrainingInput

# Definimos el contenedor (Docker) para el entrenamiento
estimator = Estimator(
    image_uri='763104351884.dkr.ecr.us-east-1.amazonaws.com/pytorch-training:2.0-cpu-py310',
    role='AmazonSageMaker-ExecutionRole',
    instance_count=1,
    instance_type='ml.m5.xlarge', # Uso eficiente de costos
    output_path='s3://tu-bucket-mlops/output'
)

# Paso de Entrenamiento
step_train = TrainingStep(
    name="EntrenamientoNexusAlpha",
    estimator=estimator,
    inputs={
        "train": TrainingInput(s3_data="s3://tu-bucket-mlops/data/train.csv", content_type="text/csv")
    }
)

# Creación del Pipeline de MLOps
pipeline = Pipeline(
    name="EndToEndPipeline",
    steps=[step_train]
)

# Guardar y ejecutar
pipeline.upsert(role_arn='arn:aws:iam::123456789:role/service-role/AmazonSageMaker-ExecutionRole')
pipeline.start()