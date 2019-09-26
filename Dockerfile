FROM python:3.7

EXPOSE 5000

# Install Poetry for package management.
RUN pip install poetry

COPY . /app
WORKDIR /app

# Install dependencies.
RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction

# Setup flask environment variables.
ENV FLASK_APP recommender/app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV PYTHONPATH /app/recommender

CMD ["flask", "run"]
