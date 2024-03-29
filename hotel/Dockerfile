FROM python:3.9

WORKDIR /app

COPY ./requirements.txt requirements.txt

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y && \
    pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]