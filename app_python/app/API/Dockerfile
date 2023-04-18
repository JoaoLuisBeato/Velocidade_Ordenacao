FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install flask

COPY . .

EXPOSE 80

CMD ["python", "./API.py"]

