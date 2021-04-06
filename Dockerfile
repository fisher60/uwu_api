FROM python:3.9-slim

RUN pip install pipenv

COPY . /app/

WORKDIR /app/

RUN pipenv install --system --deploy

ENTRYPOINT ["pipenv"]
CMD ["run", "start"]
