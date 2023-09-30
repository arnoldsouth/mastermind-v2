import requests

API_URL = "https://www.random.org/integers/?num={}&min={}&max={}&col={}&base={}&format={}&rnd={}"

params = {
    "num": 4,
    "min": 0,
    "max": 7,
    "col": 1,
    "base": 10,
    "format": "plain",
    "rnd": "new",
}


def generate_combination():
    response = requests.get(API_URL, params=params)
    data = response.text.split()
    # print(f"data: {data}")

    combination = [int(num) for num in data]
    print(f"combination: {combination}")  # [0, 1, 2, 3]

    return combination
