import requests
# import json


def fetch_price(api_key):
    endpoint_url = "https://api.metalpriceapi.com/v1/latest?api_key={}&base=INR&currencies=XAU".format(
        api_key
    )
    response = requests.get(endpoint_url)
    response_json = response.json()
    status = response_json["success"]
    # price_oz = response_json["rates"]["INRXAU"]
    price_gm = response_json["rates"]["INRXAU"] / 31.1035
    return {"status": status, "price": price_gm}


print(fetch_price(api_key=""))
