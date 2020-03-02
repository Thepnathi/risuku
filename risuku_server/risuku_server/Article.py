class Article:
    def __init__(self, **article: dict):
        self.source: dict = article["source"]
        self.author: str = article["author"]
        self.title: str = article["title"]
        self.description: str = article["description"]
        self.url: str = article["url"]
        self.urlToImage: str = article["urlToImage"]
        self.publishedAt: str = article["publishedAt"]
        self.content: str = article["content"]

    def contentLength(self) -> Union[int,None]:
        return len(self.content)


thisdict: dict =	{
  "source": {"id": 123, "name": "Business Insider"},
  "author": "",
  "title": "",
  "description": "",
  "url": "",
  "urlToImage": "",
  "publishedAt": "",
  "content": ""
}
