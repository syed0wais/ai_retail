import boto3; import json; bedrock = boto3.client('bedrock-runtime', region_name='us-east-1', aws_access_key_id='BedrockAPIKey-w0rl-at-814567590002', aws_secret_access_key='hf2PIhT+h4MqvWupmG4793AtEpBvajKkFVr/QQKf6Sa53wvcyj4LiDqTfm8='); 
try:
  response = bedrock.invoke_model(modelId='anthropic.claude-v2', body=json.dumps({'prompt': '

Human: hi

Assistant:', 'max_tokens_to_sample': 10}), contentType='application/json')
  print('SUCCESS:', response)
except Exception as e:
  print('ERROR:', e)
