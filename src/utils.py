import requests


def get_ip() -> str:
    response = requests.get("https://ifconfig.io/ip")

    if response.status_code != 200:
        raise Exception("Failed to get IP address")

    return response.text.strip()


if __name__ == "__main__":
    print(get_ip())
