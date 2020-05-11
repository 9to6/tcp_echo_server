FROM python:3.7-alpine

WORKDIR /app
ADD server.py /app/server.py

CMD [""]
ENTRYPOINT ["python", "-u", "server.py"]
