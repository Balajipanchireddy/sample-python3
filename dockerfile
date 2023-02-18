FROM python:alpine
WORKDIR /home/data
COPY ./ ./
CMD ["python" ,"dockerassignment.py"]
