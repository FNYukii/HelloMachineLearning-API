# Dockerfile
FROM tensorflow/tensorflow:2.9.2

EXPOSE 8000

WORKDIR /app
COPY ./requirements.txt /app
RUN apt update
RUN apt install -y libopencv-dev
RUN pip install -r requirements.txt

CMD ["hug", "-f", "index.py"]
