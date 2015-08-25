#!/usr/bin/env python
#coding=utf-8

import sql_func

#书籍
books_sql = sql_func.create_table_sql("books", 
        *[
            sql_func.title_field_sql("title"),
            sql_func.title_field_sql("subtitle"),
            sql_func.title_field_sql("author"),
            sql_func.sn_field_sql("ISBN"),
            sql_func.sn_field_sql("tcode"),
            sql_func.title_field_sql("publisher"),
            sql_func.int_field_sql("publisher_version"),
            sql_func.money_field_sql("price"),
            sql_func.memo_field_sql()
        ]
    )

#地区
local_sql = sql_func.create_table_sql("location",
    *[
        sql_func.title_field_sql("title"),
        sql_func.money_field_sql("money"),
        sql_func.memo_field_sql()
    ]
)

#仓储
storage_sql = sql_func.create_table_sql("storage",
    *[
        sql_func.id_field_sql("book_id"),
        sql_func.id_field_sql("local_id"),
        sql_func.int_field_sql("amount")
    ]
)

#角色
role_sql = sql_func.create_table_sql("role",
    *[
        sql_func.title_field_sql("name"),
    ]
)

#员工信息
employee_sql = sql_func.create_table_sql("employee",
    *[
        sql_func.title_field_sql("name"),
        sql_func.id_field_sql("local_id"),
        sql_func.id_field_sql("role_id"),
        sql_func.phone_field_sql("phone"),
        sql_func.title_field_sql("email"),
        sql_func.title_field_sql("qq"),
        sql_func.title_field_sql("gacc"),
        sql_func.title_field_sql("MSN"),
        sql_func.title_field_sql("skype"),
        sql_func.memo_field_sql()
    ]
)

#客户/供应商个人信息
personal_sql = sql_func.create_table_sql("personal",
    *[
        sql_func.title_field_sql("name"),
        sql_func.id_field_sql("company_id"),
        sql_func.id_field_sql("local_id"),
        sql_func.zip_field_sql("zip"),
        sql_func.title_field_sql("address"),
        sql_func.title_field_sql("email"),
        sql_func.title_field_sql("qq"),
        sql_func.title_field_sql("gmail"),
        sql_func.title_field_sql("MSN"),
        sql_func.title_field_sql("skype"),
        sql_func.memo_field_sql()
    ]
)

#客户/供应商公司信息
company_sql = sql_func.create_table_sql("cmpany",
    *[
        sql_func.title_field_sql("name"),
        sql_func.title_field_sql("local_id"),
        sql_func.title_field_sql("adress"),
        sql_func.zip_field_sql("zip"),
        sql_func.id_field_sql("linkman_id"),
        sql_func.bool_field_sql("is_batch"),
        sql_func.bool_field_sql("is_supplier"),
        sql_func.memo_field_sql()
    ]
)

#领书单
take_token_sql = sql_func.create_table_sql("take_token",
    *[
        sql_func.id_field_sql("book_id"),
        sql_func.id_field_sql("token_id"),
        sql_func.id_field_sql("employee_id"),
        sql_func.int_field_sql("amount"),
        sql_func.date_field_sql("take_date"),
        sql_func.memo_field_sql()
    ]
)

#反馈类别
feedback_class_sql = sql_func.create_table_sql("feedback_class",
    *[
        sql_func.title_field_sql("title")
    ]
)

#反馈单
feedback_token_sql = sql_func.create_table_sql("feedback_token",
    *[
        sql_func.id_field_sql("take_token_id"),
        sql_func.id_field_sql("token_id"),
        sql_func.id_field_sql("book_id"),
        sql_func.id_field_sql("personal_id"),
        sql_func.id_field_sql("company_id"),
        sql_func.int_field_sql("amount"),
        sql_func.id_field_sql("feedback_class"),
        sql_func.stamp_field_sql("feedback_datetime"),
        sql_func.bool_field_sql("is_batch"),
        sql_func.money_field_sql("price"),
        sql_func.memo_field_sql()
    ]
)

#销售报价单
sell_quotation_sql = sql_func.create_table_sql("sell_quotation",
    *[
        sql_func.id_field_sql("book_id"),
        sql_func.id_field_sql("local_id"),
        sql_func.date_field_sql("quotation_date"),
        sql_func.money_field_sql("price"),
        sql_func.bool_field_sql("is_batch"),
        sql_func.memo_field_sql()
    ]
)

#进货报价单
buy_quotation_sql = sql_func.create_table_sql("buy_quotation",
    *[
        sql_func.id_field_sql("book_id"),
        sql_func.id_field_sql("company_id"),
        sql_func.date_field_sql("quotation_date"),
        sql_func.money_field_sql("price"),
        sql_func.bool_field_sql("is_batch"),
        sql_func.memo_field_sql()
    ]
)

#进货单
buy_token_sql = sql_func.create_table_sql("buy_token",
    *[
        sql_func.id_field_sql("book_id"),
        sql_func.id_field_sql("token_id"),
        sql_func.id_field_sql("supplier_id"),
        sql_func.money_field_sql("price"),
        sql_func.int_field_sql("amount"),
        sql_func.memo_field_sql()
    ]
)

#调拨单
requisition_sql = sql_func.create_table_sql("requisition",
    *[
        sql_func.id_field_sql("book_id"),
        sql_func.int_field_sql("amount"),
        sql_func.id_field_sql("from_id"),
        sql_func.id_field_sql("to_id"),
        sql_func.id_field_sql("buy_token_id"),
        sql_func.date_field_sql("out_date"),
        sql_func.date_field_sql("in_date"),
        sql_func.memo_field_sql()
    ]
)

#人员变动记录
employee_token_sql = sql_func.create_table_sql("employee_token",
    *[
        sql_func.id_field_sql("employee_id"),
        sql_func.id_field_sql("from_local_id"),
        sql_func.id_field_sql("to_local_id"),
        sql_func.id_field_sql("from_role_id"),
        sql_func.id_field_sql("to_role_id"),
        sql_func.memo_field_sql()
    ]
)

#现金出纳单
money_token_sql = sql_func.create_table_sql("money_token",
    *[
        sql_func.id_field_sql("employee_id"),
        sql_func.stamp_field_sql("datetime"),
        sql_func.money_field_sql("money"),
        sql_func.bool_field_sql("is_input"),#是否为还款
        sql_func.id_field_sql("token_id"),
        sql_func.memo_field_sql()
    ]
)

#返点记录
privilege_sql = sql_func.create_table_sql("privilege",
    *[
        sql_func.id_field_sql("token_id"),
        sql_func.id_field_sql("book_id"),
        sql_func.int_field_sql("amount"),
        sql_func.money_field_sql("money"),
        sql_func.memo_field_sql()
    ]
)

tables = [
    books_sql,
    local_sql,
    storage_sql,
    role_sql,
    employee_sql,
    personal_sql,
    company_sql,
    take_token_sql,
    feedback_class_sql,
    feedback_token_sql,
    sell_quotation_sql,
    buy_quotation_sql,
    buy_token_sql,
    requisition_sql,
    employee_token_sql,
    money_token_sql,
    privilege_sql
]

if __name__=="__main__":
    f = open("create_tables.sql", "wrb")
    for sql in tables:
        f.write(sql)
    f.close()