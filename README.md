# kbb-backend

## Build image

`working_dir=./environment`
`docker image ls` is just to check whether your image is build with the correct ag

```
sh build.sh
docker image ls
```

### setting image tag
change the following environment variable in the file
```
cat .env
```

## Launch local environment 

`working_dir=./environment`

```
sh init_e2e.sh
```

## AWS URL  
Backend - http://kbb-load-balancer-531067821.ap-southeast-1.elb.amazonaws.com:5000/home


## SAST SonarCloud 
Backend -  https://sonarcloud.io/project/overview?id=cherrythia_kbb-backend

## SCA 
Login to debricked to view SCA result

Backend - https://debricked.com/app/en/repository/54593