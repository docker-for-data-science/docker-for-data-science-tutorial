# Docker-Compose Essentials

This set of exercises will help you get familiar with the Docker Compose.

## Exercise A: Run a simple compose file

1. Checkout the code ...

```command
git clone https://github.com/docker-for-data-science/talkvoter.git
cd talkvoter/
```

... then run it.  Wait for the services to spin up and stabilize (stop producing output.)

```command
docker-compose build
docker-compose up
```

Then stop the services.

```command
Ctrl-c
```

2. Build and run in the same step and run in the background.

   - `up` will start the whole application.
   - `--build` will first build the application before starting it.
   - `-d` will run the application in the background.


```command
docker-compose up --build -d
```

3. See that it's running

```command
docker-compose ps
```

You should see output similar to this.
 - the `Name` column is the container name
 - the `Command` column is the command that is running
 - the `State` column displays if the service is up
 - the `Ports` column displays the port mapping

```command
Name                      Command               State    Ports
-----------------------------------------------------------------------
talkvoter_app_1       ./docker-utils/entrypoint- ...   Up      8000/tcp
talkvoter_db_1        docker-entrypoint.sh postgres    Up      5432/tcp
talkvoter_predict_1   ./docker-utils/entrypoint- ...   Up      8000/tcp

```

4. Check how it looks when running in Docker

```command
docker ps
```

Here are the containers that are started as viewed by `docker ps`.

```command
b5cf33bcd497        docker4data/predict_api:prod-1.0.1   "./docker-utils/entr…"   About a minute ago   Up About a minute   8000/tcp            talkvoter_predict_1
ef19b739cffc        docker4data/talkvoter:prod-1.0.1     "./docker-utils/entr…"   About a minute ago   Up About a minute   8000/tcp            talkvoter_app_1
c5919701310f        postgres:10-alpine                   "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp            talkvoter_db_1
```

5. Restart the application

```command
docker-compose restart
```

You can restart the service based on the service name as defined in the docker-compose.yml.  In this case, there is a service called `app`

```command
docker-compose restart app
```

6. Stop the compose application

```command
docker-compose stop
```

7. Restart the compose application

```command
docker-compose start
```

8. Destroy compose application

```command
docker-compose down
```

If you do a docker-compose ps, nothing should be running

## Exercise B: Expose a port

1. Create a docker-compose.override.yaml with the following contents.

```yaml
version: '2'
services:
  app:
    ports:
      - "8000:8000"
```

2. Build and run

```command
docker-compose up --build -d
```

3. In a web browser, visit the following url:

[http://localhost:8000/](http://localhost:8000/)

4. Destroy compose application

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

3. Create an empty file inside of the container, then exit the container

```command
touch /tmp/TESTME
ls -l /tmp/TESTME
exit
```

4. Exec back into the container.  Is the file still there?

```command
docker-compose exec app /bin/bash
ls -l /tmp/TESTME
exit
```

5. Enter the container using the run command and touch a file and exit.

```command
docker-compose run app /bin/bash
touch /tmp/TESTME2
ls -l /tmp/TESTME2
exit
```

6. Enter the container again and look for the touch file.

```command
docker-compose run app /bin/bash
ls -l /TESTME2
exit
```

7. Is the file still there?  What do you notice is different between run and exec?
What do you think would happen to the touch files if you ran docker-compose destroy?


## Exercise D: Add a second node and interact

1. Bring the app up.

```command
docker-compose up --build -d
```

2. See what's running

```command
docker-compose ps
```

3. Enter the running app container with exec

```command
docker-compose exec -u root app /bin/bash
```

4. While inside of the container, ping the db service

```command
ping -c 5 db
```

5. Notice that you can refer to the other service by name inside of the container

6. Install postgres client

```bash
apt update
apt install -y postgresql-client
```

7. Connect to the database

```bash
psql -U postgres -h db postgres
```

8. Destroy compose application

```command
docker-compose down
```

**Note:** you'll never want to install software outside of a Dockerfile
like we did above (unless you are experimenting)
