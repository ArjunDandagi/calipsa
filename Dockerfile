FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 8080/tcp 9110/tcp
ENTRYPOINT [ "python" ] 
CMD [ "dumpheaders.py" ]
