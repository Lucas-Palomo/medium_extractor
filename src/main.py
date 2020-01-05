from src.Collector import Collector

collector = Collector()

keywords = ['pornografia', 'bolsonaro', 'lula', 'feminismo', 'racismo', 'machismo']

for word in keywords:
    url = "https://api.medium.com/search/posts?q={}&limit=2".format(word)
    content = collector.get_content(url)
    if content is not None:
        posts = collector.collect_posts(content)
        if posts is not None:
            for post in posts:
                post_content = collector.get_content(post["href"])
                meta_content = collector.extract_post(post_content, post["href"])
                print(meta_content)
