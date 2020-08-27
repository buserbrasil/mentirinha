FROM python:3.8.3

RUN pip install uwsgi

RUN mkdir -p /mentirinha

WORKDIR "/mentirinha"

COPY . .

RUN pip install -r requirements.txt && \
  rm -rf ~/.cache/pip

RUN mkdir -p /dkdata

RUN ./manage.py collectstatic

ENTRYPOINT [ "uwsgi", "--ini", "uwsgi.ini" ]
