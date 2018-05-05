# Docker Basics

This set of exercises will help you get familiar with the Docker workflow.

## Exercise A: Pull Image from Docker Hub

> [DockerHub](https://hub.docker.com) is a public [registry](https://docs.docker.com/registry/) where you can find and download Docker images. This is where you will find official Docker images for Linux distributions, databases, and Python.

***Tip:** Check out [Project Jupyter on DockerHub](https://hub.docker.com/r/jupyterhub) for lots of great pre-built Docker images!*

1. We will start by pulling an image from DockerHub to our local machine using the [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/) command. We will use this image for the rest of tutorial:

```command
docker pull python:3.6.5-alpine3.7
```

2. We can take a look at all images on our machine using the [`docker images`](https://docs.docker.com/engine/reference/commandline/images/) command:

```console
REPOSITORY                                TAG                 IMAGE ID            CREATED             SIZE
python                                    3.6.5-alpine3.7     27e79c0fa4d2        13 days ago         87.4MB
```

## Exercise B: Create Container

> We can create containers from an image. Think of images like a cookiecutter.

1. Taking a look at the [Dockerfile](https://github.com/docker-library/python/blob/b99b66406ebe728fb4da64548066ad0be6582e08/3.6/alpine3.7/Dockerfile) for the image we pulled, it will run `python3` when a container is created.

```command
$ docker run -it python:3.6.5-alpine3.7
Python 3.6.5 (default, Apr  4 2018, 23:11:43)
[GCC 6.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

***Tip:** `docker run` has lots of [options](https://docs.docker.com/engine/reference/commandline/run/#options)*

2. We are at the Python shell prompt inside of the container. Use `Ctrl + P + Q` to dettach from the container and return to your prompt.

## Exercise C: Stop Container

> Dettacing from the container means it is still running in the background.

1. We can take a look at all running container using the [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps) command:

```console
CONTAINER ID        IMAGE                    COMMAND             CREATED             STATUS              PORTS               NAMES
8d5d1420dd97        python:3.6.5-alpine3.7   "python3"           20 minutes ago      Up 20 minutes                           quirky_rosalind
```

***Tip:** Use `docker ps -a` to view all stopped containers. Containers stop when the process we are running inside of the container is exited (or killed).*

2. Use [`docker stop`](https://docs.docker.com/engine/reference/commandline/stop) with your container name to stop the container.

```console
$ docker stop quirky_rosalind
quirky_rosalind
```

***Tip:** We can use both the [container-name] or [container-id] to refer to containers.*

3. Confirm this container has stopped using `docker ps -a`.

## Exercise D: Delete Container

1. We can delete stopped container using the `docker rm` command:

```console
$ docker rm quirky_rosalind
quirky_rosalind
```

2. Confirm this container is not listed when we do a `docker ps -a`.

## Exercise E: Shell into container

> In Exercise 2, we created a container which ran the `python3` shell after it launched. This default command was set in the `Dockerfile` of the image we pulled.

1. We can override the default container launch command by passing in parameters when we create a container using [`docker run`](https://docs.docker.com/engine/reference/commandline/run):

```console
$ docker run -it python:3.6.5-alpine3.7 /bin/sh
/ #
```

We are now inside the shell of the container.

***Tip:** If your imagine contains the bash shell, you can get to that prompt using `/bin/bash`*

***Tip:** Alpine is a lightweight Docker image sans frills*

## Exercise F: Hello World Dockerfile

> A [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) is a file that contains commands that are used to build a Docker image. We can write a `Dockerfile` to create custom images that contain only the things we want.

1. Create a python file that prints "Hello World" and save it as `hello_world.py`:

```python
# hello_world.py

print('Hello World!')
```

2. In the same folder, create a `Dockerfile` with the following contents:

```Dockerfile
# Dockerfile

# Use latest Python runtime as base image
FROM python:3.6.5-alpine3.7

# Set the working directory to /app and copy current dir
WORKDIR /app
COPY . /app

# Run hello_world.py when the container launches
CMD ["python", "hello_world.py"]
```

3. We can use `docker build -t hello-world .` to build an image from a `Dockerfile` located in the current directory with the tag, `hello-world`.

```console
$ docker build -t hello-world .
Sending build context to Docker daemon  3.072kB
Step 1/4 : FROM python:3.6.5-alpine3.7
 ---> 27e79c0fa4d2
Step 2/4 : WORKDIR /app
Removing intermediate container f9582523a722
 ---> 9045b5cfcbc1
Step 3/4 : COPY . /app
 ---> 5c1019a0993b
Step 4/4 : CMD ["python", "hello_world.py"]
 ---> Running in 6c013d2d0fe8
Removing intermediate container 6c013d2d0fe8
 ---> 0aabeeb989a8
Successfully built 0aabeeb989a8
Successfully tagged hello-world:latest
```

4. Use this image to create a new container using `docker run hello`. You should see a `Hello World` message printed to the console.

5. Take a look at all stopped containers using `docker ps -a`. Note the `container-name` or `container-id` of the image.

6. Restart the image using `docker start -ia [container-name / container-id]`. You should see `Hello World` printed to the console once again.

***Tip:** `-i` attaches STDIN and `-a` attaches STDOUT/STDERR to terminal*

## Exercise G: Delete Image

> Confirm you do not need a Docker image anymore before you delete it from your machine

1. Let's pull a [BusyBox](https://en.wikipedia.org/wiki/BusyBox) image from DockerHub. BusyBox is an executible that contains stripped down Unix tools:

```console
docker pull busybox
```

2. Confirm image has been pulled using `docker images`

3. Delete busybox image:

```console
docker rmi busybox
```

4. Confirm image has been deleted using `docker images`
