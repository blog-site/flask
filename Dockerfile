FROM python:3.11

RUN pip install flask

ENTRYPOINT ["python","/app/app.py"]
EXPOSE 5000
