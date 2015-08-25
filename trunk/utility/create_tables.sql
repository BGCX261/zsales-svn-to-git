
create table books
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    title char(100), subtitle char(100), ISBN char(30), tcode char(30), publisher char(100), publisher_version integer, price numeric(18, 4), memo varchar(500),
    constraint books_cons primary key (id)
);


create table location
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    title char(100),
    constraint location_cons primary key (id)
);


create table storage
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    book_id char(30), local_id char(30), amount integer,
    constraint storage_cons primary key (id)
);


create table role
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    name char(100),
    constraint role_cons primary key (id)
);


create table employee
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    name char(100), local_id char(30), role_id char(30), phone varchar(20), email char(100), qq char(100), gacc char(100), MSN char(100), skype char(100), memo varchar(500),
    constraint employee_cons primary key (id)
);


create table personal
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    name char(100), company_id char(30), local_id char(30), zip char(6), address char(100), email char(100), qq char(100), gmail char(100), MSN char(100), skype char(100), memo varchar(500),
    constraint personal_cons primary key (id)
);


create table cmpany
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    name char(100), adress char(100), zip char(6), linkman_id char(30), is_batch integer, is_supplier integer, memo varchar(500),
    constraint cmpany_cons primary key (id)
);


create table take_token
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    book_id char(30), token_id char(30), employee_id char(30), amount integer, take_date date default CURRENT_DATE, memo varchar(500),
    constraint take_token_cons primary key (id)
);


create table feedback_class
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    title char(100),
    constraint feedback_class_cons primary key (id)
);


create table feedback_token
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    take_token_id char(30), token_id char(30), book_id char(30), personal_id char(30), company_id char(30), amount integer, feedback_class char(30), feedback_date date default CURRENT_DATE, is_batch integer, price numeric(18, 4), memo varchar(500),
    constraint feedback_token_cons primary key (id)
);


create table sell_quotation
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    book_id char(30), local_id char(30), quotation_date date default CURRENT_DATE, price numeric(18, 4), is_batch integer, memo varchar(500),
    constraint sell_quotation_cons primary key (id)
);


create table buy_quotation
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    book_id char(30), company_id char(30), quotation_date date default CURRENT_DATE, price numeric(18, 4), is_batch integer, memo varchar(500),
    constraint buy_quotation_cons primary key (id)
);


create table buy_token
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    book_id char(30), token_id char(30), supplier_id char(30), price numeric(18, 4), amount integer, memo varchar(500),
    constraint buy_token_cons primary key (id)
);


create table requisition
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    book_id char(30), amount integer, from_id char(30), to_id char(30), buy_token_id char(30), memo varchar(500),
    constraint requisition_cons primary key (id)
);


create table employee_token
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    employee_id char(30), from_local_id char(30), to_local_id char(30), from_role_id char(30), to_role_id char(30), memo varchar(500),
    constraint employee_token_cons primary key (id)
);


create table money_token
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    datetime timestamp default CURRENT_TIMESTAMP, money numeric(18, 4), memo varchar(500),
    constraint money_token_cons primary key (id)
);


create table privilege
(
    id char(30) not null,
    time_stamp timestamp default CURRENT_TIMESTAMP,
    token_id char(30), book_id char(30), amount integer, money numeric(18, 4), memo varchar(500),
    constraint privilege_cons primary key (id)
);

