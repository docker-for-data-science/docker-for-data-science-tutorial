# Data Science Essentials

For this lab we will be using a Jupyter Notebook.

1. Navigate to this folder on your local machine.

2. Build the Dockerfile and start the container.

```bash
docker build -t talk_recommender .
docker run -p 8888:8888 -p 9000:9000 -v $(pwd):/app talk_recommender
```

3. Take the url from the log and load up the Jupyter notebook `talk_recommender.ipynb` in your browser.
