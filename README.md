# Mobilise Recommender Service

This is the recommender system that Mobilise uses to generate recommended shifts.

## Getting Started

This project uses Docker and Docker Compose.

You will need to set the environment variables

```
PORT=
DB_USERNAME=
DB_PASSWORD=
DB_NAME=
DB_HOST=
DB_PORT=
```

If you have the [EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-local.html) installed, build and run with

```
eb local run
```

Otherwise, you can build and run it yourself

```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

I should probably do something to make this less verbose.

## Project Structure

```
recommender/
    __init__.py
    app.py                 # this file contains the app and routes
    models/               
    resources/
        __init__.py
        recommendations.py # the recommendation resource
    engine.py              # heavy lifting
    mobiliseapi.py         # class that acts as an abstraction for the database
```
