import requests

# url = "https://api.paystack.co/bank/resolve?account_number=0001234567&bank_code=058"

url = "https://api.paystack.co/bank"
headers = {
    "Authorization": "Bearer sk_test_b549b2f8c8dcb7c5d6711062af3a4c1447c5d71b",
    "Content-Type": "application/json"
}
reponse  = requests.get(url, headers = headers)
print(reponse.status_code)
print(reponse.json())
