import requests

from bs4 import BeautifulSoup

import json


gmail = input("GMAIL VICTIM : ")

url = f"https://thatsthem.com/email/{gmail}"

headers = {

    "Accept": "text/html",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')


    script_tags = soup.find_all('script', type='application/ld+json')

    if script_tags:

        for script_tag in script_tags:

            json_data = script_tag.string

            if json_data:

                try:

                    parsed_data = json.loads(json_data)


                    if isinstance(parsed_data, list) and all('@type' in item and item['@type'] == 'Person' for item in parsed_data):

                        for person in parsed_data:

                            if '@id' in person:

                                del person['@id']

                            if 'url' in person:

                                del person['url']

                            if '@context' in person:

                                del person['@context']


                        print(json.dumps(parsed_data, indent=2))

                        break

                except json.JSONDecodeError as e:

                    print(f"Error decoding JSON: {e}")
    else:

        print("No <script type='application/ld+json'> tags found.")
else:

    print(f"Error: Received status code {response.status_code}")


