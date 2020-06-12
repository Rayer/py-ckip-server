FROM python:3.7
MAINTAINER rayer@vista.aero
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "server.py"]