FROM python:3.7

WORKDIR /usr/src/app

RUN pip install --no-cache-dir pipenv

COPY Pipfile ./
RUN pipenv install --skip-lock
EXPOSE 5000

COPY ./src /usr/src/app

CMD [ "pipenv", "run", "python", "app.py" ]