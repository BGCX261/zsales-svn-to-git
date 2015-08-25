#-*- encoding:utf-8 -*-

class ref_constains(object):
	def __init__(self, fname, ref_tname, ref_fname, ref_label):
		self.field_name = fname
		self.ref_table_name = ref_tname
		self.ref_field_name = ref_fname
		self.ref_label = ref_label

class entity(object):
	def __init__(self, tname):
		self.table_name = tname
		self.fields_dict = {}
		self.ref_dict = {}
		
books = entity("books")
books.fields_dict = {'title':u'书名',
					 'subtitle':u"子标题",
					 'isbn':u'ISBN',
					 'tcode':u'条形码',
					 'author':u'作者'
					 'publisher':u'出版商',
					 'publish_version':u'版次',
					 'price':u'价格',
					 'memo':u'备注'
					 }

personal = entity('personal')
personal.fields_dict = {'name':u'姓名',
						'company_id':u'就职企业',
						'local_id':u'地区',
						'zip':u'邮政编码',
						'Address':u'地址',
						'movable_phone':u'移动电话',
						'email':u'电子邮件',
						'qq':u'QQ',
						'gacc':u'Google帐号',
						'msn':u'MSN',
						'skype':u'SKYPE',
						'memo':u'备注'
						}

company = entity("comany")
company.fields_dict = {'name':u'公司名',
					   'address':u'地址',
					   'zip':u'邮政编码',
					   'linkman':u'联系人',
					   'is_batch':u'批发商',
					   'is_supplier':u'供货商',
					   'local_id':u'地区',
					   'phone':u'电话',
					   'memo':u'备注'
					   }

employee = entity("employee")
employee.fields_dict = {'name':u'姓名',
						'id_card':u'身份证',
						'local_id':u'地区',
						'role_id':u'职务',
						'movable_phone':u'移动电话',
						'phone':u'电话',
						'email':u'电子邮件',
						'qq':u'QQ'，
						'GACC':u'Google帐号',
						'MSN':u'MSN',
						'skype':u'SKYPE',
						'memo':u'备注'
						}

take_token = entity("take_token")
take_token.field_dict = {'book_id':u'书籍',
						 'amount':u'数目',
						 'employee_id':u'领书人',
						 'local_id':u'地区',
						 'take_date':u'领书日期',
						 'memo':u'备注'
	}

