#!/bin/bash

export localhost="mysqldb:3306"
export db_user="root"
export db_pass="root"

docker-compose up -d
sleep 10
docker-compose up initmysqldb