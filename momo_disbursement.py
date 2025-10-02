import requests
import base64
import json

# === CONFIG ===
SUBSCRIPTION_KEY = "11c97b4783de46078f7c334917583e0e"  # Your disbursement primary key
API_USER_ID = "b4d66d9f-6519-4123-93f0-bd5b9e43b7c9"  # The X-Reference-Id you used
API_KEY = "8e6322741c4d406c8805a591aa2d9e31"  # The API key you generated
ENVIRONMENT = "sandbox"  # keep sandbox for testing

# === BASE URL ===
BASE_URL = "https://sandbox.momodeveloper.mtn.com"

# === GET ACCESS TOKEN ===
auth = f"{API_USER_ID}:{API_KEY}"
auth_bytes = auth.encode("utf-8")
auth_b64 = base64.b64encode(auth_bytes).decode("utf-8")

headers = {
    "Authorization": f"Basic {auth_b64}",
    "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {"grant_type": "client_credentials"}

print("🔑 Getting Access Token...")
r = requests.post(f"{BASE_URL}/disbursement/token/", headers=headers, data=data)
print(r.status_code, r.text)
token = r.json()["access_token"]

# === CHECK BALANCE ===
headers_balance = {
    "Authorization": f"Bearer {token}",
    "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
    "X-Target-Environment": ENVIRONMENT
}

print("\n💰 Checking Balance...")
r = requests.get(f"{BASE_URL}/disbursement/v1_0/account/balance", headers=headers_balance)
print(r.status_code, r.text)

# === SEND DISBURSEMENT ===
headers_disburse = {
    "Authorization": f"Bearer {token}",
    "Ocp-Apim-Subscription-Key": SUBSCRIPTION_KEY,
    "X-Target-Environment": ENVIRONMENT,
    "Content-Type": "application/json",
    "X-Reference-Id": "b2b22233-4f67-4c92-a9ff-48d82f13d888"  # any UUID for the transaction
}

payload = {
    "amount": "1000",
    "currency": "EUR",
    "externalId": "123456789",
    "payee": {
        "partyIdType": "MSISDN",
        "partyId": "46733123453"
    },
    "payerMessage": "Disbursement test",
    "payeeNote": "Here is your money"
}

print("\n💸 Sending Disbursement...")
r = requests.post(f"{BASE_URL}/disbursement/v1_0/transfer", headers=headers_disburse, json=payload)
print(r.status_code, r.text)

# === CHECK TRANSFER STATUS ===
print("\n📦 Checking Transfer Status...")
r = requests.get(f"{BASE_URL}/disbursement/v1_0/transfer/b2b22233-4f67-4c92-a9ff-48d82f13d888",
                 headers=headers_balance)
print(r.status_code, r.text)
