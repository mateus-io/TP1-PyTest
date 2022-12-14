FROM python:3.11.0a5-alpine3.15

WORKDIR /home/python/tp1-pytest

COPY . ./

RUN pip install -r requirements.txt

CMD pytest

# or CMD python -m pytest