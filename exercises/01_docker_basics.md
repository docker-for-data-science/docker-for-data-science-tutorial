# Docker Basics

This set of exercises will help you get familiar with the Docker workflow.

# Exercise 1: Pull Image from Docker Hub

*DockerHub is a public [registry](https://docs.docker.com/registry/) where you can find and download Docker images. This is where you will find official Docker images for Linux distributions, databases, and Python.*

> **Tip:** Check out [Project Jupyter on DockerHub](https://hub.docker.com/r/jupyterhub) fr lots of great pre-built Docker images!.

* We will start by pulling an image from DockerHub to our local machine using the [`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/) command. We will use this image for the rest of tutorial:

```command
docker pull python:3.6.5-alpine3.7
```

* We can take a look at all images on our machine using the [`docker images`](https://docs.docker.com/engine/reference/commandline/images/) command:

```console
REPOSITORY                                TAG                 IMAGE ID            CREATED             SIZE
python                                    3.6.5-alpine3.7     27e79c0fa4d2        13 days ago         87.4MB
```

## Exercise 2: Create Container

*We can create containers from an image. Think of images like a cookiecutter.*

* Taking a look at the [Dockerfile](https://github.com/docker-library/python/blob/b99b66406ebe728fb4da64548066ad0be6582e08/3.6/alpine3.7/Dockerfile) for the image we pulled, it will run `python3` when a container is created.

```command
$ docker run -it python:3.6.5-alpine3.7
Python 3.6.5 (default, Apr  4 2018, 23:11:43)
[GCC 6.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

> **Tip:** `docker run` has lots of [options](https://docs.docker.com/engine/reference/commandline/run/#options)

* We are at the Python shell prompt inside of the container. Use `Ctrl + P + Q` to dettach from the container and return to your prompt.

## Exercise 3: Stop Container

*Dettacing from the container means it is still running in the background.*

* We can take a look at all running container using the [`docker ps`](https://docs.docker.com/engine/reference/commandline/ps) command:

```console
CONTAINER ID        IMAGE                    COMMAND             CREATED             STATUS              PORTS               NAMES
8d5d1420dd97        python:3.6.5-alpine3.7   "python3"           20 minutes ago      Up 20 minutes                           quirky_rosalind
```

> **Tip:** Use `docker ps -a` to view all stopped containers. Containers stop when the process we are running inside of the container is exited (or killed).

* Use [`docker stop`](https://docs.docker.com/engine/reference/commandline/stop) with your container name to stop the container.

```console
$ docker stop quirky_rosalind
quirky_rosalind
```

> **Tip:** We can use both the [container-name] or [container-id] to refer to containers.

* Confirm this container has stopped using `docker ps -a`.

## Exercise 4: Delete Container

* We can delete stopped container using the `docker rm` command:

```console
$ docker rm quirky_rosalind
quirky_rosalind
```

* Confirm this container is not listed when we do a `docker ps -a`.

## Exercise 5: Shell into container

*In Exercise 2, we created a container which ran the `python3` shell after it launched. This default command was set in the `Dockerfile` of the image we pulled.*

* We can override the default container launch command by passing in parameters when we create a container using [`docker run`](https://docs.docker.com/engine/reference/commandline/run):

```console
$ docker run -it python:3.6.5-alpine3.7 /bin/sh
/ #
```

We are now inside the shell of the container.

> **Tip:** If your imagine contains the bash shell, you can get to that prompt using `/bin/bash`

> **Tip:** Alpine is a lightweight Docker image sans frills

## Exercise 6: Hello World Dockerfile

* Hello World Dockerfile
    * Students will create from scratch

## Exercise 7: Delete Image

*Confirm you do not need a Docker image anymore before you delete it from your machine*

* Let's pull a [BusyBox](https://en.wikipedia.org/wiki/BusyBox) image from DockerHub. BusyBox is an executible that contains stripped down Unix tools:

```console
docker pull busybox
```

* Confirm image has been pulled using `docker images`

* Delete busybox image:

```console
docker rmi busybox
```

* Confirm image has been deleted using `docker images`
