FROM python:alpine3.15
WORKDIR /app
COPY requirements.txt .
COPY main.py .
RUN pip install pytelegrambotapi
RUN pip install pip --upgrade
RUN pip install pytelegrambotapi --upgrade
CMD ["python", "main.py"]