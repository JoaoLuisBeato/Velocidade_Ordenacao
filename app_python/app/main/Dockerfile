FROM python:3

WORKDIR /usr/src/app

COPY . .

RUN pip install flask
RUN pip install requests

COPY . .

EXPOSE 80

CMD ["python", "./main.py"]

