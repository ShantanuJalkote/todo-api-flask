# todoapi-flask-docker
ToDo Api built using Flask and containerized using Docker.

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
