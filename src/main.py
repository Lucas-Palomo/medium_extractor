import json
import time

from src.Collector import Collector

collector = Collector()

keywords = ['bolsonaro',
            'hamilton mourão',
            'eneas carneiro',
            'trump brasil',
            'haddad',
            'lula',
            'temer',
            'dilma rousseff']

for word in keywords:
    url = "https://api.medium.com/search/posts?q={}&limit={}".format(word, 40)
    content = collector.get_content(url)
    if content is not None:
        posts = collector.collect_posts(content)
        stored_posts = []
        file = open("/home/darksrc/Documents/TCC/Conteudos/Core/files/{}.json".format(word.replace(" ", "_")), "a")
        if posts is not None:
            for post in posts:
                post_content = collector.get_content(post["href"])
                # while post_content is not None:
                    # break
                    # print("dormindo por 10 segundos")
                    # time.sleep(10)
                    # post_content = collector.get_content(post["href"])

                if post_content is not None:
                    meta_content = collector.extract_post(post_content, post["href"])
                    stored_posts.append(meta_content)
                    # print("dormindo por 3 segundos")
                    # time.sleep(3)

        file.write(json.dumps(stored_posts, ensure_ascii=False))
        file.close()
    print(word, "\n")
