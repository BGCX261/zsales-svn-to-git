#!/usr/bin/env python
#coding=utf-8

def create_table_sql(table_name, *field_list):
    create_template = """
create table %s
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    %s,
    constraint %s_cons primary key (id)
);

"""
    fields = ', '.join(field_list)
    return create_template%(table_name, fields, table_name)

def id_field_sql(name):
    return "%s char(30)"%name

def title_field_sql(name):
    return "%s char(100)"%name

def sn_field_sql(name):
    return "%s char(30)"%name

def int_field_sql(name):
    return "%s integer"%name

def money_field_sql(name):
    return "%s numeric(18, 4)"%name

def memo_field_sql(name="memo"):
    return "%s varchar(500)"%name

def zip_field_sql(name="zip"):
    return "%s char(6)"%name

def phone_field_sql(name="phone"):
    return "%s varchar(20)"%name

def address_field_sql(name):
    return "%s varchar(30)"%name
    
def date_field_sql(name):
    return "%s date default CURRENT_DATE"%name

def stamp_field_sql(name):
    return "%s timestamp default CURRENT_TIMESTAMP"%name

def bool_field_sql(name):
    return "%s integer"%name
                
def add_gen(table_name):
    return """CREATE GENERATOR gen_%s;"""%table_name;
