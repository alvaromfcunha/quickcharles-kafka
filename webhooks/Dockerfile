FROM python:3.10

COPY ./src /code/src
COPY ./requirements.txt /code

WORKDIR /code
RUN pip install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]