#-*- encoding:utf-8 -*-
from app import db
class Get_html(db.Model):
	__tablename__='html'
	id = db.Column(db.Integer,primary_key=True)
	book_name = db.Column(db.String(10))
	html = db.Column(db.String(100))
	get_chapter = db.relationship('Get_chapter',backref='main_html',lazy='dynamic')
	def __repr__(self):
		return '{}'.format(self.html)
class Get_chapter(db.Model):
	__tablename__='chapter'
	id = db.Column(db.Integer,primary_key=True)
	chapter_main =db.Column(db.String(50))
	chapter_all  =db.Column(db.String(50))
	chapter_content = db.Column(db.String(50))
	html_id = db .Column(db.Integer,db.ForeignKey('html.id'))
