FROM continuumio/miniconda3
WORKDIR /home
COPY . . 
RUN apt upgrade -y 
RUN pip install -r requirements.txt 
ENV PYTHONPATH=/home
CMD ["python", "scraper.py"]