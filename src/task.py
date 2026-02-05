from crawl import crawl_site_async
from storage import set_status, set_result, set_error

async def run_crawl_job(job_id, url, max_pages, max_concurrency):
    try:
        set_status(job_id, "Running")
        result = await crawl_site_async(
            base_url=url,
            max_pages=max_pages,
            max_concurrency=max_concurrency
        )
        set_result(job_id, result)
    except Exception as e:
        set_error(job_id, str(e))
