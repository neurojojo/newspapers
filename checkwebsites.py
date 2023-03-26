import requests
from bs4 import BeautifulSoup

url = "https://www.tuscaloosanews.com/"  # Replace with the URL you want to check

try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()

        text_fields = soup.find_all('div')  # Select relevant HTML tags
        all_text = []
        for field in text_fields:
            all_text.append(field.get_text())

        with open('tmp.txt','w+') as f:
            f.write( soup.prettify() )
        with open('tmp2.txt','w+') as f:
            [ f.write( f'{line}\n' ) for line in all_text ]

    else:
        print(f"The website {url} does not exist.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")