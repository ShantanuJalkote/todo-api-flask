# todoapi-flask-docker
ToDo Api built using Flask in Docker er

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/ShantanuJalkote/todo-api-flask.git
$ docker build -t todoapi .
```
### Run the container
Create a container from the image.
```
$ docker run todoapi
```

Now visit http://localhost:8080
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' my-container
6095273a4e9b
```
