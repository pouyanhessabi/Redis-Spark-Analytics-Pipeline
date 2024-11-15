A simple data engineering task. This project implements a comprehensive data engineering pipeline that combines
real-time data storage and batch analytics processing.

# Part 1:

Install Redis database using docker, Implement one API for storage and one API for retrieving data from redis database
using Flask (Python).

## Step 1: Install Redis database using docker:

``` docker pull redis ``` <br>

> ``` docker images -a ``` <br> REPOSITORY, TAG, IMAGE ID, CREATED, SIZE <br>
> redis, latest, 6c199afc1dae, 6 weeks ago, 117MB,

``` docker run -d --name redis-container -p 6379:6379 redis ```
> ``` docker ps ``` <br> CONTAINER ID, IMAGE, COMMAND, CREATED, STATUS, PORTS, NAMES <br>
> 407a3a425580, redis,     "docker-entrypoint.s…", 13 seconds ago, Up 11 seconds, 0.0.0.0:6379->6379/tcp,
> redis-container

## Step 2: Implement an API that get a key and stores the received word in Redis using Flask.

- Implement one API for storage and one API for retrieving data from redis database using Flask (Python).
 
