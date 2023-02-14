# todoapi-flask-docker
ToDo Api built using Flask and containerized using Docker.

### To Run the flask Api
```
$ git clone https://github.com/ShantanuJalkote/todo-api-flask.git
$ flask run
```

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/ShantanuJalkote/todo-api-flask.git
$ cd todo-api-flask
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
