FROM python:3.8.3

RUN pip install uwsgi

RUN mkdir -p /mentirinha

WORKDIR "/mentirinha"

ADD requirements.txt /mentirinha

RUN pip install -r requirements.txt && \
  rm -rf ~/.cache/pip

COPY . .

RUN mkdir -p /dkdata

RUN ./manage.py collectstatic
