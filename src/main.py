from fastapi import FastAPI, BackgroundTasks, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from models import CrawlRequest
from storage import create_job, get_job
from task import run_crawl_job

import csv_report as csv_report



app = FastAPI(title="WebCrawler")

app.mount("/static",StaticFiles(directory="src/static"),name="static")
templates = Jinja2Templates(directory="src/templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/crawl")
async def start_crawl(request: CrawlRequest, background_task: BackgroundTasks):
    job_id = create_job()
    
    background_task.add_task(
        run_crawl_job,
        job_id,
        str(request.base_url),
        request.max_pages,
        request.max_concurrency
    )

    return {
        "job_id": job_id,
        "status": "Started"
    }

@app.get("/crawl/{job_id}")
async def get_crawl_status(job_id: str):
    job = get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job


@app.get("/feed", response_class=HTMLResponse)
async def feedpage(request: Request):
    return templates.TemplateResponse(
        "feed.html",
        {"request": request}
    )

@app.get("/settings", response_class=HTMLResponse)
async def settingspage(request: Request):
    return templates.TemplateResponse(
        "settings.html",
        {"request": request}
    )

@app.get("/about", response_class=HTMLResponse)
async def aboutpage(request: Request):
    return templates.TemplateResponse(
        "about.html",
        {"request": request}
    )



    




