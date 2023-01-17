FROM python:3.8.16-slim

LABEL author='okazivaetsya' version=1 

WORKDIR /app

COPY requirements.txt /app

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY ./ /app

CMD ["python", "main.py"] 