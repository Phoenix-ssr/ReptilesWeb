# ReptilesWeb
爬虫web
## 目录
[TOC]
### 项目简介：
>1. flask+python+docker的web应用
>2. 主要内容为小说爬虫
>用户端输入网址和部分正则表达式，提交给后端存入数据库。后端进行爬取小说，并返回给用户端一个已经爬取的目录，提供下载功能
>3. 当前为1.0版本（前端的修饰都没有。。。）
>4. 目前有四个路由地址
>> + Reptiles:提交小说目录网址和书名
>> + Chapter:目录的信息提取和目录的提取以及正文的正则表达式（会返回小说目录网址的源代码，为啥没有正文因为。。。）
>> + Book:爬取页面
>> + book:下载目录
### 使用说明：
>  1.GitHub下载:压缩包解压后
>```
>#1
>python3 web.py#flask_web2目录下
>#2docker
>构建容器：
>sudo docker build -t 'flask_web' .
>注意命令结尾的"点"
>sudo docker images
>临时运行docker镜像：
>sudo docker run -it --rm -p 5000:5000 flask_web
>运行：
>docker run -p 127.0.0.1:5000:5000/tcp -d flask_web
>```
>2. doker镜像下载后：
>```
>docker push yourname/newimage
>```

