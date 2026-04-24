#!/bin/bash
set -e

timeout 60 bash -c '
until curl -f http://localhost:8021/health; do
  sleep 2
done
'

curl -X POST http://localhost:8021/jobs
curl -f http://localhost:8021/health