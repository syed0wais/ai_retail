import boto3, json, os

for region in ['us-east-1', 'us-west-2', 'eu-central-1', 'eu-north-1']:
    try:
        client = boto3.client('bedrock', region_name=region)
        models = client.list_foundation_models(byOutputModality='TEXT')['modelSummaries']
        runtime = boto3.client('bedrock-runtime', region_name=region)
        for m in models:
            m_id = m['modelId']
            if 'anthropic' not in m_id and 'amazon' not in m_id and 'meta' not in m_id: continue
            try:
                # payload format changes, let's just use amazon titan for a quick test if it's there
                if 'titan' in m_id:
                    res = runtime.invoke_model(modelId=m_id, body=json.dumps({"inputText": "hi"}), contentType='application/json')
                    print(f"SUCCESS: {m_id} in {region}")
                    break
                elif 'claude-3' in m_id:
                    payload={'anthropic_version': 'bedrock-2023-05-31', 'max_tokens': 10, 'messages': [{'role': 'user', 'content': [{'type': 'text', 'text': 'hi'}]}]}
                    res = runtime.invoke_model(modelId=m_id, body=json.dumps(payload), contentType='application/json')
                    print(f"SUCCESS: {m_id} in {region}")
                    break
            except Exception as e:
                pass
    except Exception:
        pass
