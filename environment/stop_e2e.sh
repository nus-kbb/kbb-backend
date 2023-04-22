#!/bin/bash
docker stop $(docker ps | awk '/kbb/{print $1}')
docker rm $(docker ps -a | awk '/kbb/{print $1}')