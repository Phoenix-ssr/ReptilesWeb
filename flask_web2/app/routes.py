# -*- coding: utf-8 -*-
from app import app,db
from flask import render_template,flash,redirect,url_for,request,send_from_directory
from app.forms import Get_chapterForm,Get_htmlForm
from werkzeug.urls import url_parse
from app.models import Get_html,Get_chapter
import sys   #reload()之前必须要引入模块
import re
import io#文件打开问题
import requests#请求
from concurrent.futures import ThreadPoolExecutor#异步
import imp#python3.5解决reload(sys)问题
import os.path#文件下载路径
imp.reload(sys)
#sys.setdefaultencoding('utf8')
@app.route('/')
@app.route('/Reptiles',methods=['GET','POST'])
def Reptiles_get():
	form=Get_htmlForm()
	if form.validate_on_submit():
		h = Get_html(html=form.html.data,book_name=form.book_name.data)
		db.session.add(h)
		db.session.commit()
		id='/Chapter/'+str(h.id)
		return redirect(id) 
	return render_template('reptiles.html',form=form)
@app.route('/Chapter/<id>',methods=["GET","POST"])
def Chapter_get(id):
	form=Get_chapterForm()
	h=Get_html.query.get(id)
	if form.validate_on_submit():
		c=Get_chapter(
		chapter_main = form.chapter_main.data,
		chapter_all  = form.chapter_all.data,
		chapter_content = form.chapter_content.data,
		main_html    = h
		)
		db.session.add(c)
		db.session.commit()
		url='/Book/'+str(c.id)
		return redirect(url)
	html=str(h.html)
	response = requests.get(html)
	response.encoding = 'utf-8'
	show = response.text
	return render_template('chapter.html',show=show,form=form)
def Run(book_name,chapter_inof_list,chapter):#耗时任务
	fb = io.open('book/%s'%book_name,'w',encoding='utf-8')
	for chapter_inof in chapter_inof_list:
        	chapter_url = 'https://www.xiaoshuo530.com%s' % chapter_inof[0]                 
        	chapter_title = chapter_inof[1]
        	chapter_response = requests.get(chapter_url)
        	chapter_response.encoding = 'utf-8'
        	chapter_html = chapter_response.text
        	chapter_content = re.findall(r'%s'%chapter,chapter_html,re.S)[0]
        	chapter_content = chapter_content.replace('&nbsp;','')
        	chapter_content = chapter_content.replace('</p>','')
        	chapter_content = chapter_content.replace('<br/>','')
        	fb.write(chapter_title)
        	fb.write(u'\n')
        	fb.write(chapter_content)
        	fb.write(u'\n')
	fb.close()
	return 'ok'
executor = ThreadPoolExecutor(10)
@app.route('/Book/<id>',methods=["GET","POST"])
def Book_get(id):
	b=Get_chapter.query.get(id)#b是实例
	url=str(b.main_html.html)
	response = requests.get(url)
	response.encoding = 'utf-8'
	show = response.text
	chapter=b.chapter_main#chapter临时储存正则内容
	dl = re.findall(r'%s'%chapter,show,re.S)[0]
	chapter=b.chapter_all
	chapter_inof_list = re.findall(r'%s'%chapter,dl,re.S)
	chapter=b.chapter_content
	book_name=b.main_html.book_name+'.txt'
	url=re.findall(r'https:.*?com',url,re.S)[0]
	executor.submit(Run,book_name,chapter_inof_list,chapter)
	book_names=Get_html.query.all()
	return render_template('book.html',book_names=book_names)
@app.route('/Book')
def Book_show():
	book_names=Get_html.query.all()
	return render_template('book.html',book_names=book_names)
dirpath = os.path.join(app.root_path,'book')
@app.route('/book/<path:book_name>')
def download(book_name):
	return send_from_directory(dirpath,book_name,as_attachment=True)


