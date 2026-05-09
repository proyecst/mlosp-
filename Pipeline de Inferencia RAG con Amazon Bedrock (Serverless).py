import json
import boto3

# Inicializamos el cliente de Bedrock
bedrock = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

def lambda_handler(event, context):
    """
    Lambda que actúa como el motor de inferencia para una arquitectura RAG.
    """
    body = json.loads(event['body'])
    user_prompt = body.get('prompt')

    # Configuración para Claude 3 (Anthropic) en Bedrock
    payload = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": f"Basado en el contexto del vector store, responde: {user_prompt}"
            }
        ]
    }

    response = bedrock.invoke_model(
        body=json.dumps(payload),
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response.get('body').read())
    
    return {
        'statusCode': 200,
        'body': json.dumps({'respuesta': response_body['content'][0]['text']})
    }