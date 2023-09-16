FROM python:3.11-slim-bookworm
WORKDIR /usr/app/src
COPY healthHttp.py ./
EXPOSE 8000
CMD ["python","./healthHttp.py"]
