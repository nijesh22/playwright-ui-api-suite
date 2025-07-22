import requests

BASE_URL = "https://automationexercise.com/api"

def get_all_products():
    return requests.get(f"{BASE_URL}/productsList")

def get_product_by_id(product_id):
    return requests.get(f"{BASE_URL}/productDetails/{product_id}")