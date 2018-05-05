# Docker Basics

This set of exercises will help you get familiar with the Docker Compose.

## Exercise A: Run a simple compose file

1. Build a docker-compose.yml file ...

  ```yaml
  ---
  version: '2'
  services:
    app:
      image: python:3.6.5
      command: ["python", "-mhttp.server", "8000"]
  ```

  ... then run it.

  ```command
  docker-compose build
  docker-compose up
  ```

2. Build and run in the same step and run in the background.

  ```command
  docker-compose up --build -d
  ```

  See that it's running

  ```command
  docker-compose ps
  ```

  Check how it looks when running in Docker

  ```command
  docker ps
  ```

  Restart the application

  ```command
  docker-compose restart
  ```

  Or

  ```command
  docker-compose restart app
  ```

  Stop the compose application

  ```command
  docker-compose stop
  ```

  Re-Start the compose application

  ```command
  docker-compose start
  ```

  Destroy compose application

  ```command
  docker-compose down
  ```

  If you do a docker-compose ps, nothing should be running


## Exercise B: Expose a port

1. Add the port mapping to your compose file

  ```yaml
  ---
  version: '2'
  services:
    app:
      image: python:3.6.5
      command: ["python", "-m", "http.server", "8000"]
    ports:
      - "8000:8000"
  ```

  Build and run

  ```command
  docker-compose up --build -d
  ```

  In a web browser, visit the following url:

  http://localhost:8000/

  Destroy compose application

  ```command
  docker-compose down
  ```



## Exercise C: Exec vs Run


1. Start the app again

  Build and run

  ```command
  docker-compose up --build -d
  ```

2. Enter the running app container with exec

  ```command
  docker-compose exec app /bin/bash
  ```

  Create an empty file inside of the container, then exit the container
  ```command
  touch /TESTME
  ls -l /TESTME/
  exit
  ```

  Exec back into the container.  Is the file still there?

  ```command
  docker-compose exec app /bin/bash
  ls -l /TESTME/
  exit
  ```

3. Enter the container using the run command and touch a file and exit.

  ```command
  docker-compose run app /bin/bash
  touch /TESTME2
  ls -l /TESTME2
  exit
  ```

  Enter the container again and look for the touch file.

  ```command
  docker-compose run app /bin/bash
  ls -l /TESTME2
  exit
  ```

  Is the file still there?  What do you notice is different between run and exec?
  What do you think would happen to the touch files if you ran docker-compose destroy?


## Exercise D: Add a second node and interact


1. Build a docker-compose.yml file ...

    ```yaml
    ---
    version: '2'
    services:
      app:
        image: python:3.6.5
        command: ["python", "-m", "http.server", "8000"]
        ports:
          - "8000:8000"
      db:
        image: postgres:10
    ```

    ... then run it.

    ```command
    docker-compose up --build -d
    ```

    See what's running

    ```command
    docker-compose ps
    ```

    Enter the running app container with exec

    ```command
    docker-compose exec app /bin/bash
    ```

    While inside of the container, ping the db service

    ```command
    ping -c 5 db
    ```

    Notice that you can refer to the other service by name inside of the container

    Install postgres client

    ```bash
    apt update
    apt install -y postgresql-client
    ```

    Connect to the database
    ```
    psql -U postgres -h db postgres
    ```

    Destroy compose application

    ```command
    docker-compose down
    ```

    **Note:** you'll never want to install software outside of a Dockerfile
    like we did above (unless you are playing around)



## Exercise E: Create a Dockerfile


1. Create a Dockerfile

  ```text
  FROM python:3.6
  RUN pip install "Flask<1.0" psycopg2-binary
  ENV PYTHONPATH=/app/
  RUN mkdir /app/
  WORKDIR /app/
  COPY demo_app.py /app/demo_app.py
  ```

  Modify your docker-compose.yml file to look like this.

  ```yaml
  ---
  version: '2'
  services:
     app:
       build: .
       command: ["flask", "run"]
       environment:
         - FLASK_APP=demo_app
         - DEBUG=True
         - PORT=8000
         - DB_PORT=5432
         - DB_HOST=db
       ports:
         - "8000:8000"
     db:
       image: postgres:10
    ```

  Create a file called demo_app.py and put the following in it.


  ```python
  import os
  import sys
  import time
  import psycopg2
  from flask import Flask
  app = Flask(__name__)

  DEBUG = os.getenv("DEBUG", None)
  PORT = int(os.getenv("PORT", "8000"))
  DB_PORT = int(os.getenv("DB_PORT", "5432"))
  DB_HOST = os.getenv("DB_HOST", "localhost")
  DB_NAME = os.getenv("DB_NAME", "postgres")
  DB_USER = os.getenv("DB_USER", "postgres")
  DB_PASS = os.getenv("DB_PASS", "postgres")


  def connect():
      print("Connecting to db", file=sys.stderr)
      while True:
          try:
              conn = psycopg2.connect(
                  f"dbname={DB_NAME} user={DB_USER} port={DB_PORT} host={DB_HOST}")
          except Exception:
              print("  trying to connect to db....", file=sys.stderr)
              time.sleep(5)
              continue
          print("Connected to db", file=sys.stderr)
          break
      return conn


  def create_test_table(conn):
      cur = conn.cursor()
      cur.execute(
          "CREATE TABLE IF NOT EXISTS test "
          "(id serial PRIMARY KEY, num integer);")
      conn.commit()
      cur.close()


  conn = connect()
  create_test_table(conn)


  @app.route("/")
  def hello():
      cur = conn.cursor()
      cur.execute("INSERT INTO test  (num) Values (1);")
      conn.commit()
      cur.execute("SELECT * FROM test;")
      out = ""
      for record in cur:
          out += "<br>row {}".format(record)
      cur.close()

      return ("Hello World! DEBUG {} PORT {} <br> {}".format(
              DEBUG, PORT, out))


  app.run(
      host='0.0.0.0',
      port=PORT,
      debug=bool(DEBUG == "True"))

  ```

  Then run it:

  ```command
  docker-compose up --build -d
  ```
