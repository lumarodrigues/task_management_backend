FROM python:3.12-slim

RUN apt-get update && apt-get install -y git libmongo-client-dev

RUN apt-get update && apt-get install -y netcat-traditional

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
