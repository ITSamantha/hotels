FROM python:3.9

WORKDIR /app

COPY ./requirements.txt requirements.txt
ADD ./entrypoint.sh /entrypoint.sh


RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
