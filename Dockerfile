FROM python:3.7 as base
MAINTAINER rayer@vista.aero
FROM base as builder

RUN mkdir /install
COPY requirements.txt /install
WORKDIR /install
RUN pip install --prefix="/install" --no-warn-script-location -r requirements.txt

FROM base
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app
EXPOSE 8000
CMD ["python", "server.py"]