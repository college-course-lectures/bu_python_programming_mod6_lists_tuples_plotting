import math
import random
import uuid
import requests
"""
Author: Professor Lewis
Date: August 25, 2025
Module demonstrates the use of Python functions and
Azure AI Translator
"""
PI = math.pi

AZURE_TRANSLATOR_KEY = "ADD YOUR KEY HERE"
AZURE_TRANSLATOR_ENDPOINT = "https://api.cognitive.microsofttranslator.com"
AZURE_TRANSLATOR_REGION = "ADD YOUR REGION HERE"

def greet_user():
    print("Hello! Welcome to the Functions Demonstration.")

def compute_circle_area(radius):
    area = PI * (radius ** 2) # radius * radius
    return area

def area_flow():
    while True:
        text = input("Enter radius: ")
        try:
            radius = float(text)
            if radius < 0:
                print("Radius must be 0 or greater.  Try again.")
                continue
            break
        except ValueError:
            print("Please enter a number (e.g., 7)")
    area = compute_circle_area(radius)
    print(f"Area = {area:.4f} (using PI = {PI})")

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def roll_dice_flow():
    total = roll_dice()
    print(f"You rolled a total of {total}!")

def lambda_map_flow():
    nums = [1,2,3,4]
    print("List: ", nums)

    number = input("Add what number to each? (example, 7):")
    try:
        n = float(number)
    except ValueError:
        print("Not a number.  Using 1.")
        n= 1.0
    result = list(map(lambda x: x + n, nums)) # f(x)
    print("Original: ", nums)
    print(f"Added {n} to each -> ", result)

def future_feature():
    pass





def translate_text_azure(text, to_lang="es"):

    key = AZURE_TRANSLATOR_KEY
    endpoint = AZURE_TRANSLATOR_ENDPOINT
    region = AZURE_TRANSLATOR_REGION

    if not (key and endpoint and region):
        return "[Azure not configured: set AZURE_TRANSLATOR_KEY/ENDPOINT/REGION constants]"

    path = '/translate'
    url = endpoint + path

    params = {"api-version": "3.0", "to": to_lang}

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Ocp-Apim-Subscription-Region": region,
        "Content-type": "application/json",
        "X-ClientTraceId": str(uuid.uuid4()),
    }
    body = [{"Text": text}]

    try:
        resp = requests.post(url, params=params, headers=headers, json=body, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return data[0]["translations"][0]["text"]

    except requests.exceptions.HTTPError as e:
        # include status for quick debugging
        return f"[HTTP {resp.status_code} error: {resp.text[:200]}]"
    except Exception as e:
        return f"[Translator error: {e}]"

def translate_flow():
    text = input("Enter text to translate: ")
    lang = input("Target language code (e.g., es, fr, de): ").strip() or "es"
    print("Translation:", translate_text_azure(text, lang))

