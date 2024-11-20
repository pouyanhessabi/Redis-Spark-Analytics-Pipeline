A simple data engineering task. This project implements a comprehensive data engineering pipeline that combines
real-time data storage and batch analytics processing. <br>
Implementation Technologies: ***Python, Flask, Redis, Docker, Spark***

# Table of Content:

[Part one: Real-time Data Storage](#part-1-real-time-data-storage) <br>
&nbsp;&nbsp;&nbsp;&nbsp;[1: Install Redis database using docker](#step-1-install-redis-database-using-docker) <br>
&nbsp;&nbsp;&nbsp;&nbsp;[2: Add cities to redis database](#step-2-add-cities-to-redis-database)<br>
&nbsp;&nbsp;&nbsp;&nbsp;[3: Get cities from redis database](#step-3-get-cities-from-redis-database)<br>
[Part two: Analytics Reports](#part-2-analytics-reports) <br>
&nbsp;&nbsp;&nbsp;&nbsp;[1: Setup Docker](#step-1-setup-docker)<br>

# Part 1: Real-time Data Storage

Install Redis database using docker, Implement one API for storage and one API for retrieving data from redis database
using Flask (Python).

## Step 1: Install Redis database using docker:

``` docker pull redis ```: pull the redis image <br>

> ``` docker images -a ```: list all docker images <br> REPOSITORY, TAG, IMAGE ID, CREATED, SIZE <br>
> redis, latest, 6c199afc1dae, 6 weeks ago, 117MB,

``` docker run -d --name redis-container -p 6379:6379 redis ```: run and create the redis container <br
> ``` docker ps ``` <br> CONTAINER ID, IMAGE, COMMAND, CREATED, STATUS, PORTS, NAMES <br>
> 407a3a425580, redis,     "docker-entrypoint.s…", 13 seconds ago, Up 11 seconds, 0.0.0.0:6379->6379/tcp,
> redis-container

**Each time to start the redis container before running the application** : ``` docker start redis-container ``` <br>

## Step 2: Add cities to redis database:

An API that get a key and stores the received word in Redis using Flask, the used data structure is set. <br>
Image of the API: <br>
![Postman add city](https://github.com/pouyanhessabi/Redis-Spark-Analytics-Pipeline/blob/main/Report/pic/Postman%20add-city.jpg)

## Step 3: Get cities from redis database:

An API that get a key and returns all cities from Redis; the JSON response is returned. <br>
Image of the API: <br>
![Postman get cities](https://github.com/pouyanhessabi/Redis-Spark-Analytics-Pipeline/blob/main/Report/pic/Postman%20get-cities.jpg)

# Part 2: Analytics Reports

Batch Analytics Processing: create the requested analytical reports using Apache Spark and store the analysis outputs as
files in MinIO. <br>

## Step 1: Setup Docker:

In the first part, we set up the Docker environment for the redis database, now we want to implement and refactor the
docker environment for the redis, flask, spark, and minio application. <br>

``` docker network create data_engineering_network```: create the docker network <br>
***Redis***: <br>
``` docker pull redis```: set up Redis <br>
```docker run --name redis-container --network data_engineering_network -d redis```: run <br>

***Spark***: <br>
```docker pull bitnami/spark```: set up Spark <br>
```docker run --name spark-master --network data_engineering_network -d bitnami/spark spark-shell```: run <br>

***MinIO***: <br>
```docker pull minio/minio```: set up Minio <br>
```docker run --name minio-container --network data_engineering_network -d -p 9000:9000 -p 9001:9001 -e "MINIO_ROOT_USER=pouyan" -e "MINIO_ROOT_PASSWORD=12345678" minio/minio server /data --console-address ":9001"```:
run <br>
***Flask***: <br>
Create ```Dockerfile```.<br>
***Add ```requirements.txt```*** <br>
***Add ```docker-compose.yml```***: for each container: redis, spark, minio, flask<br>

## Step 2
