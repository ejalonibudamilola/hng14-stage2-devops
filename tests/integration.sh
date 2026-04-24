#!/bin/bash
set -e

timeout 120 bash -c '
until curl -sf http://localhost:8021/health; do
  sleep 3
done
'

curl -X POST http://localhost:8021/jobs
curl -sf http://localhost:8021/health