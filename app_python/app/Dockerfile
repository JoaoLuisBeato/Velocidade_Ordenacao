FROM ubuntu

WORKDIR /app

COPY . /app

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install flask

 CMD ["python3", "-m", "API", "run", "--host=0.0.0.0"]

