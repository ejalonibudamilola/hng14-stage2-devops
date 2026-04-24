# FIXES.md



## 1. API — Redis Hardcoded Connection

File: api/main.py
Line: 7

Problem:
Redis connection was hardcoded to `localhost:6379`, which will fail inside Docker containers because services communicate via service names.

Original Code:
```python
r = redis.Redis(host="localhost", port=6379, db=0)
```

Updated Code:
```python
import os
r = redis.from_url(os.getenv("REDIS_URL"))
```



## 2. API — Missing Health Check Endpoint

File: api/main.py

Problem:
No `/health` endpoint for Docker health checks.

Updated Code:
```python
@app.get("/health")
def health():
    return {"status": "ok"}
```



## 3. WORKER — Redis Hardcoded Connection

File: worker/worker.py
Line: 6

Problem:
Worker connects to Redis using localhost, which fails in containerized environments.

Original Code:
```python
r = redis.Redis(host="localhost", port=6379, db=0)
```

Updated Code:
```python
import os
r = redis.from_url(os.getenv("REDIS_URL"))
```



## 4. WORKER — No Error Handling in Infinite Loop

File: worker/worker.py
Line: 14

Problem:
Worker loop crashes completely if any job processing fails.

Original Code:
```python
while True:
    job = r.brpop("job", timeout=5)
    if job:
        _, job_id = job
        process_job(job_id.decode())
```

Updated Code:
```python
while True:
    try:
        job = r.brpop("job", timeout=5)
        if job:
            _, job_id = job
            process_job(job_id.decode())
    except Exception as e:
        print(f"Worker error: {e}")
```



## 5. FRONTEND — Hardcoded API URL

File: frontend/app.js
Line: 6

Problem:
Frontend directly calls `localhost:8000`, which fails in Docker networking.

Original Code:
```javascript
const API_URL = "http://localhost:8000";
```

Updated Code:
```javascript
const API_URL = process.env.API_URL;
```



## 6. FRONTEND — No Health Endpoint

File: frontend/app.js

Problem:
No health check route for container monitoring.

Updated Code:
```javascript
app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});
```



## 7. PROJECT — .env File Committed

File: api/.env

Problem:
Sensitive `.env` file committed to repository, violating best practices and task rules.

Fix:
- Removed `.env` from repository
- Created `.env.example`:

```env
REDIS_URL=redis://redis:6379
API_URL=http://api:8000
```



## 8. WORKER — No Graceful Shutdown

File: worker/worker.py

Problem:
Worker does not handle termination signals, causing abrupt shutdowns.

Updated Code:
```python
import signal
import sys

def shutdown(sig, frame):
    print("Shutting down worker...")
    sys.exit(0)

signal.signal(signal.SIGTERM, shutdown)
signal.signal(signal.SIGINT, shutdown)
```



## 9. GENERAL — Hardcoded Configuration

File: Multiple files

Problem:
Application relies on hardcoded values instead of environment variables.

Original Code Example:
```python
"http://localhost:8000"
```

Updated Code Example:
```python
os.getenv("API_URL")
```



# SUMMARY

All services were updated to:
- Use environment variables instead of hardcoded values
- Support container networking
- Include health checks
- Improve stability and error handling
- Remove sensitive configuration from repository

- Added multi-stage Dockerfiles
- Added named non-root users
- Added healthchecks - Added restart policies
- Added env_file configuration
- Added Trivy security scan
- Added SARIF upload
- Added coverage artifact upload
- Added integration script
- Added rolling deployment


