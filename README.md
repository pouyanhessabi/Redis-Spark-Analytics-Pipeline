A simple data engineering task. This project implements a comprehensive data engineering pipeline that combines
real-time data storage and batch analytics processing.

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

# Part 2: Batch Analytics Processing
