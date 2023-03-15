FROM python:3.9
COPY . usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
ENTRYPOINT uvicorn --host 0.0.0.0 main:app --reload
EXPOSE 8000
CMD ["uvicorn", "main:data_src_app", "--host", "0.0.0.0"]