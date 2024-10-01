FROM python:3.9 
RUN pip install matplotlib tensorflow torch torchvision

WORKDIR /learn-tensorflow

COPY tutorials/ .
