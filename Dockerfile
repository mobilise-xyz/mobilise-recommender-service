FROM python:3.7

# Install Poetry for package management.
RUN pip install poetry

COPY . /app
WORKDIR /app/recommender

# Install dependencies.
RUN poetry config settings.virtualenvs.create false
RUN poetry install --no-interaction

# Setup flask environment variables.
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

CMD ["flask", "run"]
