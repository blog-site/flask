FROM python:3.11

RUN pip install flask
RUN pip install flask-jwt-extended

ENTRYPOINT ["python","/app/app.py"]
EXPOSE 5000
