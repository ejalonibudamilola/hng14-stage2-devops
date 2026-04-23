import redis
import time
import os
import signal
import sys

r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))


def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")


def shutdown(sig, frame):
    print("Shutting down worker...")
    sys.exit(0)


signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)


while True:
    try:
        job = r.brpop("job", timeout=5)
        if job:
            _, job_id = job
            process_job(job_id.decode())
    except Exception as e:
        print(f"Worker error: {e}")
