#!/bin/bash

mysql -h127.0.0.1 -P3306 -uroot -proot kbb_db < /app/environment/sql-scripts/initDefault.sql