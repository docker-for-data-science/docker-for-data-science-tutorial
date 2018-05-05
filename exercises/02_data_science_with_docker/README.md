# Data Science Workflows Using Docker

This set of exercises will walk you through various use cases using Docker.

## Exercise A: Self-Contained Container

Jupyter notebooks are the perfect vehicle to share the results of an academic paper or data study. But in order for our notebooks to work, users will need to have access to our data and all the dependencies that were used to produce the original dataset.

We refer to this as the ["Works on my Machine" problem](https://blog.codinghorror.com/the-works-on-my-machine-certification-program/)

With Docker, we can package up our notebook, data, and dependencies into a single image. We can upload this image to [Docker Hub](https://hub.docker.com/) for our users to download.

### Create Docker Hub Account

1. Go to [https://hub.docker.com/](https://hub.docker.com/)

2. Sign up for an account

3. You will need your user name later

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

### Building Image

> Recall that `docker build` creates an image from a `Dockerfile`

1. In the current directory, we can build an image as follows:

`docker build -t docker build -t [docker-hub-user-name]/workflow1-self-contained .`

2. Test image was built successfully by creating a container:

`docker run -p 9999:8888 alysivji/workflow1-self-contained`


