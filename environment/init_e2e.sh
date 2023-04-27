#!/bin/bash

export localhost="mysqldb:3306"
export db_user="root"
export db_password="root"

docker-compose up -d backend
docker-compose up -d adminer
sleep 20
docker-compose up initmysqldb
docker exec kbb-db sh environment/sql-scripts/sqlAddDefaultData.sh