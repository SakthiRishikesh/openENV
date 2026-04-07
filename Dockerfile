FROM python:3.10

WORKDIR /app

<<<<<<< HEAD
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "inference.py"]
=======
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
>>>>>>> 0ea8f3143bc72fc35cd1ce87055f727d096606c4
