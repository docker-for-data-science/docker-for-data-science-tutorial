# Data Science Workflows Using Docker

This set of exercises will walk you through various use cases using Docker.

## Exercise A: Self-Contained Container

Jupyter notebooks are the perfect vehicle to share the results of an academic paper or data study. But in order for our notebooks to work, users will need to have access to our data and all the dependencies that were used to produce the original dataset.

 but it suffers “works on my machine” syndrome

With Docker, we can create a completely isolated environment to reproduce every single calculation

For this particular workflow, we will:
We create a docker image with libraries, data, and notebook
Push that image to dockerhub
