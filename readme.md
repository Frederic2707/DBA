# BTC scraper

This program scrapes the unconfirmed transactions list for a minute at a time, the largest transaction of that minute is then sent to a mongoDB database. The database is filled with unique data, there are no duplicates that are allowed into it. This data can then later be used for analysis.

[Dockerhub](https://hub.docker.com/r/frederic2707/databases-advanced)

## Table of contents
**[Requirements](#Requirements)**<br>
**[Instalation](#Instalation)**<br>
**[Usage](#Usage)**<br>
**[Environments](#Environments)**<br>


## Requirements

* Python3.8 or above
* pip3
* redis
* mongoDB
* docker
* docker-compose 3

## Instalation

If you attempt to use this manually you need to install redis and mongo DB. Otherwise you can automatically install this with the use of docker and docker compose.

### Manual

Manual installation is the `pip install -r requirements.txt`

### Docker

You can use either docker or docker-compose. 

docker

`docker build -t <tagname> .`

docker-compose

`docker-compose build`

## Usage

### manual

run command `python3 ./main.py`

### docker

docker

`docker run frederic2707/databases-advanced`

docker-compose

`docker-compose up -d`

## Environments

|key           |default      | description |
|--------------|-------------|---------------------------------------|
|DATABASE_HOST | `localhost` | Where the mongoDB database is located |
|REDIS_HOST    | `localhost` | Where the Redis cache is located      |

