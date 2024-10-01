FROM python:3.9 
RUN pip install matplotlib tensorflow torch torchvision
ADD main.py .
CMD [“python”, “./main.py”] 
