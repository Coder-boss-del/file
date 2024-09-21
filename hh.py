import requests

account_number = int(input("Enter Your Account Number\>>> "))
bank_name = str(input("Enter your Bank Name\n:"))

for bank in data["data"]:
    name = bank["name"]
    code  = bank["code"]
    # print(f"{name} {code}")

    data = {
        "bank_name": name,
        "bank_code": code,
       
    }
    print(data)


url = "https://api.paystack.co/bank"
headers = {
    "Authorization": "Bearer sk_test_b549b2f8c8dcb7c5d6711062af3a4c1447c5d71b",
    "Content-Type": "application/json"
}
reponse  = requests.get(url, headers = headers)
print(reponse.status_code)
data = reponse.json()


url = f"https://api.paystack.co/bank"
# headers = {
#     "Authorization": "Bearer sk_test_b549b2f8c8dcb7c5d6711062af3a4c1447c5d71b",
#     "Content-Type": "application/json"
# }
# reponse  = requests.get(url, headers = headers)
# print(reponse.status_code)
# data = reponse.json()