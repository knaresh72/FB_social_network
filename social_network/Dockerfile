FROM python:3.10

ENV PYTHONUNBUFFERED = 1
WORKDIR /CODE
COPY requirements.txt .

RUN pip install -r requirements.txt

copy . .

EXPOSE 8000

CMD ["Python", "manage.py","runserver"]

LABEL authors="Admin"

ENTRYPOINT ["top", "-b"]