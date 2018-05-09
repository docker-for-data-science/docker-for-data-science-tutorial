# Data Science Workflows Using Docker

This set of exercises will walk you through various use cases using Docker.

## Exercise A: Self-Contained Container

Jupyter notebooks are the perfect vehicle to share the results of an academic paper or data study. But in order for our notebooks to work, users will need to have access to our data and all the dependencies that were used to produce the original calculations.

We refer to this as the ["Works on my Machine" problem](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/)

With Docker, we can package up our notebook, data, and dependencies into a single image. We can upload this image to [Docker Hub](https://hub.docker.com/) for our users to download.

### Create Docker Hub Account

1. Go to [https://hub.docker.com/](https://hub.docker.com/)

2. Sign up for an account

3. You will need your user name later.

### Downloading Notebook and Data

1. Create a new folder for this project:

```console
mkdir self-contained-container && cd self-contained-container
```

2. Save a copy of the [notebook](https://github.com/docker-for-data-science/docker-for-data-science-tutorial/tree/docker-exercises/exercises) in the folder.

```console
wget https://github.com/alysivji/talks/raw/master/data-science-workflows-using-docker-containers/workflow1-self-contained/iris-analysis.ipynb
```

3. Create a subfolder called data and save a copy of [`iris.csv`](https://raw.githubusercontent.com/alysivji/talks/master/data-science-workflows-using-docker-containers/workflow1-self-contained/data/iris.csv) into this folder

```console
mkdir data && cd data
wget https://raw.githubusercontent.com/alysivji/talks/master/data-science-workflows-using-docker-containers/workflow1-self-contained/data/iris.csv
```

### Create Dockerfile

> Recall that a [`Dockerfile`](https://docs.docker.com/engine/reference/builder/) is a file that contains commands that are used to build a Docker image.
>
> For this image, we will:
> * use the `python:3.6.5-slim` image as a base
> * copy in our notebook and data folder into the image
> * install some dependencies

1. Create a `Dockerfile` in the `self-contained-container` folder

2. We need to specify which image we want to build off of. Let's use the `python:3.6.5-slim` image as a base.

```Dockerfile
FROM python:3.6.5-slim
```

3. Next we want to set the working directory and copy in the contents of our current directory into the working directory.

```Dockerfile
WORKDIR /app
COPY . /app
```

4. For this notebook, we require a few dependencies so let's install them via `pip`:

```Dockerfile
RUN pip --no-cache-dir install numpy pandas seaborn sklearn jupyter
```

***Tip:** Always clear cache when building an image*

5. In order to connect to the Jupyter instance that is running inside of the container, we will need to set up port forwarding

```Dockerfile
EXPOSE 8888
```

6. We want to start Jupyter when the container launches:

```Dockerfile
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
```

Complete `Dockerfile` should look as follows:

```Dockerfile
# self-contained-container/Dockerfile

FROM python:3.6.5-slim

WORKDIR /app
COPY . /app

RUN pip --no-cache-dir install numpy pandas seaborn sklearn jupyter

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
```

7. Confirm directory structure looks as follows:

```console
.
├── Dockerfile
├── data
│   └── iris.csv
└── iris-analysis.ipynb
```

### Build Image

> Recall that `docker build` creates an image from a `Dockerfile`

1. In the `self-contained-container` directory, we can build an image as follows:

`docker build -t [docker-hub-user-name]/workflow1-self-contained .`

2. Test image was built successfully by creating a container:

`docker run -p 8888:8888 [docker-hub-user-name]/workflow1-self-contained`

3. Confirm we can open the notebook and recalculate cells by going to the URL of the Jupyter process running in the container.

4. `Ctrl+c` to stop the process

### Push Image to Docker Hub (extra credit)

***TIP:** Please be mindful of the conference WiFi and push the image to Docker Hub at a later date.*

1. Log in to your user account using `docker login`

2. Push image to Docker Hub using `docker push`

```console
docker [docker-hub-user-name]/workflow1-self-contained
```

Users are able to download our image using `docker pull`.

## Exercise B: Data Science Project

Those of us who work on a team know how hard it is to create a standardize development environment. Or if you have ever updated a dependency and had everything break, you understand the importance of keeping development environments isolated.

Using Docker, we can create a project / team image with our development environment and mount a volume with our notebooks and data.

The benefits of this workflow are that we can:
* Separate out projects
* Spin up a container to onboard new employees
* Build an automated testing pipeline to confirm upgrade dependencies do not break code

### Create Dockerfile

1. Create a new folder for this project:

```console
mkdir data-science-project && cd data-science-project
```

2. Create a `Dockerfile` in the `data-science-project` folder

3. We need to specify which image we are building off of. Although [Anaconda](https://hub.docker.com/r/continuumio/miniconda3/) is popular in the Data Science community, we will build off the Debian jessie slim image to not burden the conference wireless.

```dockerfile
FROM python:3.6.5-slim
```

4. Set the working directory:

```dockerfile
WORKDIR /app
```

5. `pip install` some required libraries, make sure to clean up the cache.

```dockerfile
RUN pip --no-cache-dir install pandas jupyter
```

6. In order to connect to the Jupyter instance that is running inside of the container, we will need to set up port forwarding.

```dockerfile
EXPOSE 8888
```

7. Create a mountpoint inside of our container:

```dockerfile
VOLUME /app
```

8. Start Jupyter when the container launches:

```Dockerfile
CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
```

Complete `Dockerfile` should look as follows:

```Dockerfile
# data-science-project/Dockerfile

FROM python:3.6.5-slim

WORKDIR /app

RUN pip --no-cache-dir install pandas jupyter

EXPOSE 8888

VOLUME /app

CMD ["jupyter", "notebook", "--ip='*'", "--port=8888", "--no-browser", "--allow-root"]
```

9. Confirm directory structure looks as follows:

```console
.
└── Dockerfile
```

### Build Image

1. In the `data-science-project` folder, we can build an image as follows:

`docker build -t workflow2-data-science-project .`

2. Test image was built successfully by creating a container and mounting a directory. For this, you use the full path to a directory on your machine.

`docker run -p 8888:8888 -v /full/local/path:/app workflow2-data-science-project`

3. Confirm we can access the Jupyter process by going to the endpoint URL in the container output. You should see the files of the directory you mounted in the previous step in Jupyter.

4. `Ctrl+c` to stop the process
