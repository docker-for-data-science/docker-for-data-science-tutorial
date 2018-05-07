For this lab we will be using the Jupyter Notebook.
Build the Dockerfile and start the container.

```bash
docker build -t recommend .
docker run -p 8888:8888 -p 9000:9000 recommend
```

Take the url from the log and load up the jupyter notebook  `talk_recommender.ipynb` in your broweser.