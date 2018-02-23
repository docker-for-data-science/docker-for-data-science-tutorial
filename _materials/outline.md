# Outline

1. Course and Instructor Introduction (3 minutes)
    * Make sure everybody is in the right location
    * Instructor Bios
    * High level overview of next three hours

1. Go over system requirements and where to find course materials (2 minutes; total time: 5 minutes)
    * Students will need a working laptop with a WiFi connection
    * Students will need to be running one of the following Operating Systems:
        * Windows
        * Mac
        * Linux
    * Required software:
        * Git command line tools
        * Docker
        * Docker Compose
    * Link to course material on Github
        * Have students pre-download a few Docker images to reduce strain on the conference WiFi
    * Unprepared students will have time to get their system set up during the first set of lecture

1. Reproducible Data Science - Lecture (5 minutes; total time: 10 minutes)
    * Overview of Data Science
    * Need for Full-Stack Reproducible Data Science
    * Discuss how Docker solves the problem of reproducibility
    * Note: this section will be adapted from the [Data Science Workflows using Docker Containers](https://docs.google.com/presentation/d/1LkeJc-O5k0LQvzcFokj3yKjcEDns10JGX9uHK0igU8M/) presentation

1. Introduction to Docker - Lecture (15 minutes; total time: 25 minutes)
    * High level overview of Docker
    * Containers vs Virtual Machines
    * Applications of Docker
    * Docker Architecture
    * DockerHub
    * Docker Objects (images / containers)
    * Creating images: `docker commit` vs Dockerfile
    * Overview of useful Docker commands
        * Provide cheatsheet handouts (also on Github)
    * Best Practices + Tips & Tricks
    * Note: this section will be adapted from the [Data Science Workflows using Docker Containers](https://docs.google.com/presentation/d/1LkeJc-O5k0LQvzcFokj3yKjcEDns10JGX9uHK0igU8M/) presentation

1. Introduction to Docker - Hands-on Lab (20 minutes; total time: 45 minutes)
    * Pull image from Docker Hub
        * Small image (we got you conference WiFi)
    * Start a container
    * Stop a container
    * Shell into container
    * Kill container
    * Delete container
    * Hello World Dockerfile
        * Students will create from scratch
    * Delete image

1. Data Science Workflows with Docker Containers - Lecture / Demonstration (15 minutes; total time: 1 hour)
    * Walking through actual applications of Docker
        * Workflow #1: Self-Contained Container
        * Workflow #2: Data Science Project
        * Workflow #3: Data Driven Application
        * Workflow #4: Data Science API
    * Note: this section will be adapted from the [Data Science Workflows using Docker Containers](https://docs.google.com/presentation/d/1LkeJc-O5k0LQvzcFokj3yKjcEDns10JGX9uHK0igU8M/) presentation

1. Data Science Workflow - Hands-on Lab (20 minutes; total time: 1 hour and 20 min)
    * For two of the workflows from the previous section, students will:
        * Write a Dockerfile from scratch following requirements and directions from previous section
        * `docker build` to create an image
        * `docker run` to initialize container
        * Run process inside container to confirm everything works
    * There will be exercises for all four workflows if students finish before the allocated time or want to work over the break
        * Solutions will be provided

1. Break (15 minutes; total time: 1 hour 35 min)

1. Docker Compose Overview - Lecture (20 minutes; total time: 1 hour 55 min)
    * In context of multi-container Data Science applications.
    * Introduce Docker Compose and provide a high-level overview of its core concepts and operation.
    * Overall Goals of Compose Integration:
        * Create a simple, dynamic interface for Data Scientists to download and easily run a fully-working copy of a Data Science Application.
        * Bundle all internal and external package and code dependencies into a single buildable configuration.
    * Indicate use-cases where it would and would not be appropriate.
    * Make parallels between Docker and Docker Compose.
        * Show the equivalent Docker and Docker Compose commands.
        * Show what to put in a Compose file vs what to put in a Dockerfile.
        * Walk through a Compose file.
        * Introduce concepts such as services, ports, volumes, networks, environment variables, and much more.
        * Work through common issues with Compose.
    * Demonstrate how to execute a Docker Compose file.
    * Aside: what is REST and how can we interact with APIs?

1. Introduction to Project and related Topics - Lecture (10 minutes; total time: 2 hour 5 min)
    * Project Description
        * Note: We are thinking of building out a classification model in Jupyter, pickling it and wrapping it with a REST API inside of a container (using Flask RESTful). We will plug this container into our web application that is powered by Docker Compose. This web application will have a front end which allows users to upload CSV files; app will create predictions based on input and store data inside of a Postgres database container. This project is subject to change.
    * Overview of `pickle` and the benefits of serialization

1. Building and pickling ML model - Hands-on Lab (5 minutes; total time: 2 hour 10 min)
    * We will provide a Jupyter notebook containing a pre-built model with a few empty cells for Exercises
    * Students will:
        * Save tuned model to disk
        * Load pickled model from disk
        * Make predictions using model and given inputs
    * This notebook serves as the basis for the Flask container

1. Build REST API Container - Lecture / Demonstration (10 minutes; total time: 2 hours 20 min)
    * Walk through the process of extracting the required code from Jupyter and putting it the provided Flask RESTful template
    * Fill in template Dockerfile
    * Build image and launching container
    * Testing endpoint works with `requests.get()`

1. Build REST API Container - Hands-on Lab (10 minutes; total time: 2 hours 30 min)

1. Build and Launch Data Application - Lecture / Demonstration (10 minutes; 2 hours 40 min)
    * Begin integrating previous project into a Docker Compose-based workflow.
        * Introduce Docker images needed for this project
            * Dockerfile-based image, Nginx, and Postgres
        * Introduce project boilerplate with barebones Compose file needed for lab
            * Compose will facilitate creating a web-interface for exposing data to end-users.
        * See Project Description section below
    * Show strategies for working through common Docker development issues.

1. Hands on Project (15 minutes; total time: 2 hours 55 min)
    * We will provide all the building blocks that go into this data driven application (i.e. other containers)
    * Students will plug their container from the previous exercise into the given template
    * Modify the Docker Compose file and `docker-compose up` to get the application running
    * Verify it works

1. Summary and Next Steps (5 minutes; total time: 3 hours)
    * Where to go from here
