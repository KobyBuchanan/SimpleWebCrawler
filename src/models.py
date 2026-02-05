from pydantic import BaseModel, HttpUrl

class CrawlRequest(BaseModel):
    base_url: HttpUrl
    max_pages: int = 10
    max_concurrency: int = 3
