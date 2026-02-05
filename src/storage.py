import uuid

jobs = {}

def create_job():
    job_id = str(uuid.uuid4())
    jobs[job_id] = {
        "status": "Pending",
        "result": None,
        "error": None,
    }
    return job_id

def set_status(job_id, status):
    jobs[job_id]["status"] = status

def set_result(job_id, result):
    jobs[job_id]["result"] = result
    jobs[job_id]["status"] = "Completed"

def set_error(job_id, error):
    jobs[job_id]["error"] = error
    jobs[job_id]["status"] = "Failed"

def get_job(job_id):
    return jobs.get(job_id)
