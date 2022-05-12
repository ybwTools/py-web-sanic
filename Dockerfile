FROM sanicframework/sanic:LTS

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/