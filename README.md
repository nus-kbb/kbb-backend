# kbb-backend

## Build image

`working_dir=./platform`
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

`working_dir=./platform`

```
sh init_e2e.sh
```

Backend 
http://kbb-load-balancer-531067821.ap-southeast-1.elb.amazonaws.com:8080/home