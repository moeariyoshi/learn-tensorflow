FROM python:3.9 
RUN pip install matplotlib numpy tensorflow torch torchvision

WORKDIR /learn-tensorflow

COPY tutorials/ .
