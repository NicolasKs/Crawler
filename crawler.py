import requests
from bs4 import BeautifulSoup


def init_crawler():
    starting_url = 'http://register.start.bg/'
    queue = [starting_url]

    while queue:
        current_url = queue.pop(0)
        print(current_url)
        urls = get_urls(current_url)
        if urls:
            queue.extend(urls)


def get_urls(current_url):
    urls = []
    response = get_response(current_url)
    if response:
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            checked_link = check_links(current_url, link.get('href'))
            if checked_link:
                urls.append(checked_link)

        return urls


def check_links(current_url, current_link):
    if not current_link:
        return None
    if current_link.startswith('http'):
        return current_link
    if current_link.startswith('link'):
        return current_url + current_link


def get_response(current_url):
    # If we cant establish a connection within 5 sec we don't touch that link
    try:
        response = requests.get(current_url, timeout=5)
    except Exception:
        return None
    return response


def main():

    init_crawler()


if __name__ == '__main__':
    main()
