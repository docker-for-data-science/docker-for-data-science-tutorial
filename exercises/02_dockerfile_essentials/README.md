# Dockerfile Essentials

This set of exercises will help you get familiar with Dockerfiles.

## Exercise A: Hello World Dockerfile

> A [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) is a file that contains commands that are used to build a Docker image. We can write a `Dockerfile` to create custom images that contain only the things we want.

1. Create a directory on your local machine for this workflow.

```console
$ mkdir self-contained-container && cd self-contained-container
```

2. Create a python file that prints "Hello World" and save it as `hello_world.py`:

```python
# hello_world.py

print('Hello World!')
```

3. In the same folder, create a `Dockerfile` (filename `Dockerfile`) with the following contents:

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

4. We can use `docker build -t hello-world .` to build an image from a `Dockerfile` located in the current directory with the tag, `hello-world`.

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

5. Use this image to create a new container using `docker run hello-world`. You should see a `Hello World` message printed to the console.

6. Take a look at all stopped containers using `docker ps -a`. Note the `container-name` or `container-id` of the image.

7. Restart the image using `docker start -ia [container-name OR container-id]`. You should see `Hello World` printed to the console once again.

***Tip:** `-i` attaches STDIN and `-a` attaches STDOUT/STDERR to terminal*

## Exercise B: Delete Image

> Confirm you do not need a Docker image anymore before you delete it from your machine

1. Let's pull a [BusyBox](https://en.wikipedia.org/wiki/BusyBox) image from DockerHub. BusyBox is an executible that contains stripped down Unix tools:

```console
docker pull busybox
```

2. Confirm image has been pulled using docker images

3. Delete busybox image:

```console
docker rmi busybox
```

4. Confirm image has been deleted using `docker images`
