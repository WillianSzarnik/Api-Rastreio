import requests

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Apikey 33vtyX4j9eJSzdnb7G5gUnxsNJnyKypV3Ilnl3HkzgY'
}

payload = {"code": "AA361812099BR"}
response = requests.post('https://api-labs.wonca.com.br/wonca.labs.v1.LabsService/Track',
                        headers=headers,
                        json=payload)
print(response.json())