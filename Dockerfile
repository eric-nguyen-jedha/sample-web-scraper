FROM continuumio/miniconda3
WORKDIR /home
COPY . . 
RUN apt upgrade -y 
RUN pip install -r requirements.txt 
CMD ["python", "scraper.py"]