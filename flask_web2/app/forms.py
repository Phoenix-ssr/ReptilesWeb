#-*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Length,DataRequired
from app.models import Get_chapter,Get_html
class Get_htmlForm(FlaskForm):
	book_name =TextAreaField('小说名',validators=[DataRequired(message='请输入'),Length(min=0,max=10)])
	html = TextAreaField('网址',validators=[Length(min=0,max=100),DataRequired(message='请输入')])
	submit = SubmitField('提交')
class Get_chapterForm(FlaskForm):
	chapter_main = TextAreaField('获取网页内容主体',validators=[Length(min=0,max=50),DataRequired(message='请输入')])
	chapter_all  = TextAreaField('获取每章目录和地址',validators=[Length(min=0,max=50),DataRequired(message='请输入')])
	chapter_content = TextAreaField('获取正文',validators=[Length(min=0,max=50),DataRequired(message='请输入名户名')])
	submit = SubmitField('提交')

