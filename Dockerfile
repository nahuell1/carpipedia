FROM python:3 AS app

RUN apt-get update \
    #&& apt-get install -y --no-install-recommends \
    #     \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
ENTRYPOINT ["./django-start.sh"]
CMD ["python", "manage.py", "runserver_plus", "--cert-file", "/tmp/cert"]
