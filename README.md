# Docker for Data Science

![Alt text](./_materials/build_passing.svg)

Materials for "Docker for Data Science" tutorial presented at PyCon 2018 in Cleveland, OH

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

#### Windows

1. Download [VirtualBox for Windows Hosts](https://www.virtualbox.org/wiki/Downloads).

2. Download VirtualBox image containing all required files and containers. We also have USB sticks containing these images to reduce strain on the conference WiFi.

3. Open VirtualBox Manager

4. Click New

5. Enter name: `docker-for-data-science`

6. Select OS: `Linux`

7. Select Version: `Arch Linux (64-bit)`

8. Select Memory: `2048 MB`

9. For hard disk, you will need to put at the image you downloaded in Step 2.

10. Double-click VM to start an instance.

11. Login: `osboxes` | Password: `osboxes.org` | Root password: `osboxes.org`

Talk about how it is set up for files and what not, they'll need to do a git pull and they are done

### Step 2: Clone Git Repositories

1.

### Step 3: Download Docker Images

Please pre-download Docker images to reduce the strain on the conference WiFi.
