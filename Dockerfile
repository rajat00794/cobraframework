#!/bin/bash
FROM python:3.8-alpine

RUN mkdir -p /app
WORKDIR /app 
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update
RUN apk add  git
RUN pip install --upgrade pip && pip install uvicorn
COPY ./requirements.txt /app/requirements.txt
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps
# copy project
RUN apk add python3-tkinter
COPY . /app
RUN pip install .
RUN pip uninstall -y bson
RUN pip uninstall -y pymongo
RUN pip install pymongo==3.12.3
RUN pip uninstall -y  flask_openapi3
RUN pip install passlib
RUN pip install flask_mailing
RUN pip install requests
RUN pip install -U flask-cors
RUN pip install "git+https://github.com/rajat45mishra/flaskopenapi.git#egg=flask-openapi3"
EXPOSE 8000
CMD ["uvicorn","infrastructure.server.app.wsgi:app","--workers","4","--host","0.0.0.0","--port","8000"]
