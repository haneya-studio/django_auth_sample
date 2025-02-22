# ベースイメージの指定
FROM python:3.11

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
