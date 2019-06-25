# Mobilise Recommender Service

This is the recommender system that Mobilise uses to generate recommended shifts.

## Getting Started

This project uses Docker and Docker Compose.

You will need to set the environment variables

```
PORT=
API_URL
```

Build and run with

```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

I should probably do something to make this less verbose.

## Project Structure

```
recommender/
    __init__.py
    app.py              # this file contains the app and routes
    resources/
        __init__.py
        recommendations # the recommendation resource
    engine.py           # heavy lifting
    mobiliseapi.py      # class that handles all API interaction
```
