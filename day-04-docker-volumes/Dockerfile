FROM python:3.11-slim
WORKDIR /app
RUN pip install flask
COPY app.py .
RUN mkdir -p /app/data
EXPOSE 5000
CMD ["python", "app.py"]
