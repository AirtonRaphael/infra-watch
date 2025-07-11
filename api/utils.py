import requests


def is_valid_url(url: str) -> bool:
    try:
        req = requests.get(url)

        return req.ok
    except ValueError as error:
        print(error)
        return False
