For this lab we will be using the Jupyter Notebook.
Build the Dockerfile and start the container.

```bash
docker build -t talk_recommender .
docker run -p 8888:8888 -p 9000:9000 -v $(pwd):/app talk_recommender
```

Take the url from the log and load up the jupyter notebook  `talk_recommender.ipynb` in your broweser.