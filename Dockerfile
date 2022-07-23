FROM python:3.11.0b3-alpine3.16
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY app.py /code
CMD python app.py