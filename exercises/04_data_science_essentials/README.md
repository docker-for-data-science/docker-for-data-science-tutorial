# Data Science Essentials

For this lab we will be using a Jupyter Notebook.

1. Build the Dockerfile and start the container.

```bash
docker build -t recommend .
docker run -p 8888:8888 -p 9000:9000 recommend
```

2. Take the url from the log and load up the Jupyter notebook `talk_recommender.ipynb` in your browser.
