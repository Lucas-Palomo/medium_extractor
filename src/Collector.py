import json

import requests
from bs4 import BeautifulSoup


class Collector:

    def __init__(self):
        pass

    def get_content(self, url):
        try:
            req = requests.get(url)
            if req.status_code == 200:
                return req.content
            return None
        except Exception as e:
            print("Erro: \n\t", e)
            return None

    def collect_posts(self, content):
        soup = BeautifulSoup(content, features="lxml")
        # soup.__getattribute__("href")
        main_content = soup.find("div", {"class", "js-postListHandle"})
        if main_content is not None:
            posts = main_content.find_all("a", {"class", "link link--darken"})
            if posts is not None:
                return posts
            else:
                return None
        else:
            return None

    def extract_post(self, content, url):
        soup = BeautifulSoup(content, features="lxml")
        meta_content = {
            "url": url,
            "title": self.extract_main_title(soup),
            "autor": self.extract_autor(soup),
            "tags": self.extract_tags(soup),
            "contents": self.extract_content(soup)
        }

        # pp = pprint.PrettyPrinter()
        #
        # pp.pprint(meta_content)
        # print()

        return meta_content

    def extract_main_title(self, soup):
        return soup.find("title").text

    def extract_autor(self, soup):
        return soup.find("div", {"class", "o n"}).find("span").find("a").text

    def extract_tags(self, soup):
        list = soup.find_all("li")
        tags = []
        for item in list:
            a = item.find("a")
            if a is not None and str.__contains__(a["href"], "/tag/"):
                tags.append(a["href"].replace("/tag/", ""))
        return tags

    def extract_content(self, soup):

        contents = {
            "titles": [],
            "sub-titles": [],
            "paragraphs": []

        }

        for title in soup.find("article").findAll("h1", {"id", True}):
            contents["titles"].append(title.text)

        for sub_title in soup.find("article").findAll("h2", {"id", True}):
            contents["sub-titles"].append(sub_title.text)

        for paragraph in soup.find("article").findAll("p", {"id", True}):
            contents["paragraphs"].append(paragraph.text)

        return json.dumps(contents, ensure_ascii=False)
