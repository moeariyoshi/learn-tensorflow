FROM python:3.9 
RUN pip install tensorflow
ADD main.py .
CMD [“python”, “./main.py”] 
