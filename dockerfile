# 设置基础镜像
FROM python:3.9

# 将工作目录设置为 /app
WORKDIR /app

# 复制当前目录下的所有文件到容器的 /app 目录下
COPY . /app

# 安装依赖包
RUN pip install -r requirements.txt

# 运行应用程序
CMD ["python", "app.py"]
