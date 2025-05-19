FROM python:3.12-slim-bookworm

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0", "main:app"]