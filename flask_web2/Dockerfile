FROM python:3.7
WORKDIR /ReptilesWeb/flask_web2

COPY requirements.txt ./
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple 
COPY . .
CMD ["gunicorn", "web:app", "-c", "./gunicorn.conf.py"]

