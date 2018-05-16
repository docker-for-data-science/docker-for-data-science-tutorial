# Docker for Data Science

![Alt text](./_materials/build_passing.svg)

Materials for "Docker for Data Science" tutorial presented at PyCon 2018 in Cleveland, OH.

[YouTube](https://www.youtube.com/watch?v=jbb1dbFaovg) / [Slides](http://bit.ly/docker-for-data-pycon)

---

<!-- TOC -->

- [Description](#description)
- [Audience](#audience)
- [Installation Instructions](#installation-instructions)
    - [Step 1: Install Docker and Docker-Compose](#step-1-install-docker-and-docker-compose)
    - [Step 2: Clone Git Repositories](#step-2-clone-git-repositories)
    - [Step 3: Download Docker Images](#step-3-download-docker-images)

<!-- /TOC -->

## Description

Jupyter notebooks simplify the process of developing and sharing Data Science projects across groups and organizations. However, when we want to deploy our work into production, we need to extract the model from the notebook and package it up with the required artifacts (data, dependencies, configurations, etc) to ensure it works in other environments. Containerization technologies such as Docker can be used to streamline this workflow.

This hands-on tutorial presents Docker in the context of Reproducible Data Science - from idea to application deployment. You will get a thorough introduction to the world of containers; learn how to incorporate Docker into various Data Science projects; and walk through the process of building a Machine Learning model in Jupyter and deploying it as a containerized Flask REST API.

## Audience

This session is geared towards Data Scientists who are interested in learning about Docker and want to understand how to incorporate it in their projects. No prior knowledge of Docker is assumed. Proficiency with Git and the Command Line is not a prerequisite, but will make it easier to follow along.

Upon completion of this tutorial, students will be able to:

* Navigate the Docker ecosystem with ease
* Leverage containers as part of their data science workflow
* Productionize & deploy a Machine Learning model wrapped in an API

Learn how to become a Full-Stack Data Scientist!

## Installation Instructions

### Step 1: Install Docker and Docker-Compose

#### Mac

1. Download [Docker for Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac). Contains both Docker and Docker-Compose.

2. Install

#### Linux

1. Update your package manager.

2. Use package manager to install Docker.

3. Use package manager to install Docker-Compose.

Might need to add user account to `docker` group.

#### Windows

> **Note:** Windows 10 users can use the Linux subsystem to install Docker and Docker-Compose. [Instructions from a post we found on Medium](https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4).
>
> Please also make sure to install Docker-Compose when you are installing Docker. Then proceed to Step 2

Otherwise, we have created a VM image. USB sticks with the image will be available at the tutorial

1. Download [VirtualBox for Windows Hosts](https://www.virtualbox.org/wiki/Downloads).

2. [Download VirtualBox image](https://s3.us-east-2.amazonaws.com/docker-for-data-science/docker-for-data-science.ova) containing all required files and containers. We also have USB sticks containing these images to reduce strain on the conference WiFi.

3. Open VirtualBox Manager.

4. File > Import Applicance > point to the file you just downloaded. Import it in.

5. Double-click VM to start an instance.

6. Login: `osboxes` | Password: `osboxes.org` | Root password: `osboxes.org`

The image you download contains images as well as repositories that were cloned to `~/docker-for-data-science`.

7. Update cloned repos by going into each folder and doing a `git pull`. Skip Steps 2 and 3.

### Step 2: Clone Git Repositories

1. Create a folder for this tutorial, we recommend `~/docker-for-data-science` as this will be the folder we use in all of our examples.

2. `cd` into folder

3. Download both repositories:

```console
git clone https://github.com/docker-for-data-science/docker-for-data-science-tutorial.git
git clone https://github.com/docker-for-data-science/talkvoter.git
```

### Step 3: Download Docker Images

Please pre-download Docker images to reduce the strain on the conference WiFi.

1. `cd ~/docker-for-data-science/docker-for-data-science-tutorial/installation_files`

2. Run the shell script: `./download_docker_images.sh`

3. Build images for Talk Recommendation application:

```console
cd ~/docker-for-data-science/talkvoter
docker-compose build
```
