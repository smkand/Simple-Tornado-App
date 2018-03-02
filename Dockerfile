FROM python:2.7
EXPOSE 5000
COPY . /home
WORKDIR /home
RUN pip install -r requirements.txt 
CMD python main.py