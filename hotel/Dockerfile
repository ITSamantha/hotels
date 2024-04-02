FROM python:3.9

WORKDIR /app

COPY ./requirements.txt requirements.txt
COPY ./entrypoint.sh entrypoint.sh

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]