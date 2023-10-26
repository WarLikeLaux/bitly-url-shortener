import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv

BASE_URL = "https://api-ssl.bitly.com"
SHORTEN_LINK_URL = f"{BASE_URL}/v4/bitlinks"


def is_bitlink(token, url):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    url = f"{BASE_URL}/v4/bitlinks/{get_url_without_scheme(url)}"
    response = requests.get(url, headers=headers)
    return response.ok


def get_url_without_scheme(url):
    parsed_url = urlparse(url)
    return f"{parsed_url.netloc}{parsed_url.path}"


def shorten_link(token, url):
    payload = {
        'long_url': f"{url}"
    }
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.post(SHORTEN_LINK_URL, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def count_clicks(token, link):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    link_without_scheme = get_url_without_scheme(link)
    url = f"{BASE_URL}/v4/bitlinks/{link_without_scheme}/clicks/summary"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "link",
        help=(
            "unshortened link to shorten it or enter a shortened link"
            " to see the number of clicks it has received"
        )
    )
    bitly_access_token = os.environ['BITLY_ACCESS_TOKEN']
    link = parser.parse_args().link
    try:
        if is_bitlink(bitly_access_token, link):
            bitlink_count_clicks = count_clicks(bitly_access_token, link)
            print('Count of clicks by bitlink:', bitlink_count_clicks)
        else:
            bitlink = shorten_link(bitly_access_token, link)
            print('Bitlink:', bitlink)
    except requests.exceptions.HTTPError as error:
        print(f'An HTTP error occurred: {error}')
    except requests.exceptions.RequestException as error:
        print(f"A request error occurred: {error}")


if __name__ == '__main__':
    main()
