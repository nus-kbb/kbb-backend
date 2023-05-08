#!/bin/bash

docker pull owasp/zap2docker-weekly
docker run -t owasp/zap2docker-weekly zap-baseline.py -t http://$(ip -f inet -o addr show docker0 | awk '{print $4}' | cut -d '/' -f 1):3000
# docker run -i owasp/zap2docker-stable zap-baseline.py -t "http://localhost:8080" -l PASS > zap_baseline_report.html

echo $? > /dev/null