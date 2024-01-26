from bs4 import BeautifulSoup
import requests


def extract_article_links(url):
    """
    Extracts article links from main link
    :param url: String containing url to The Himalayan Times
    :return: list of links to article
    """
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    # Finds first 3 divs containing article links which are in class: 'alith_post_except'
    article_divs = soup.find_all('div', attrs={'class': 'alith_post_except'})[:3]

    # Extracting links for articles
    links = []
    for div in article_divs:
        anchor = div.find('a', href=True)
        if anchor:
            link = anchor['href']
            links.append(link)

    return links


def extract_article_text(article_url):
    """
    Extracts text from an article
    :param article_url: String containing url to article
    :return: list of sentences found in the article
    """
    art_text = requests.get(article_url).text
    a1 = BeautifulSoup(art_text, 'html.parser')

    # Find all the <p> tags inside the dropcap.column-1 class
    paragraphs = a1.select('.dropcap.column-1 p')

    # Extract and print the text inside each <p> tag
    news_article = []
    for paragraph in paragraphs:
        news_article.append(paragraph.get_text(strip=True))

    return news_article
