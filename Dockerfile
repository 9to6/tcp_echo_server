#FROM python:3.8-alpine
#
#WORKDIR /app
#ADD server.py /app/server.py
#
#EXPOSE 10000 20000
#CMD [""]
#ENTRYPOINT ["python", "-u", "server.py"]
FROM golang:1.14-alpine

WORKDIR /app
ADD server.go /app/server.go

CMD [""]
ENTRYPOINT ["go", "run", "server.go"]
