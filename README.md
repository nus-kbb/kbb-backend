# kbb-backend

## Build image

`docker image ls` is just to check whether your image is build with the correct ag

```
sh platform/build.sh
docker image ls
```

### setting image tag
change the following environment variable in the file
```
cat .env
```

## Launch local environment 

```
sh platform/init_e2e.sh
```