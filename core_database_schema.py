from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    String,
    Integer,
    Column,
    DateTime,
    Numeric,
    CheckConstraint,
    ForeignKey,
)
from datetime import datetime

metadata = MetaData()

engine = create_engine("postgresql+psycopg2://postgres:12345_12345@localhost/sqlalchemy_basics")

customers = Table('customers', metadata,
                  Column('id', Integer(), primary_key=True),
                  Column('first_name', String(100), nullable=False),
                  Column('last_name', String(100), nullable=False),
                  Column('username', String(50), nullable=False),
                  Column('email', String(150), nullable=False),
                  Column('address', String(250), nullable=False),
                  Column('city', String(50), nullable=False),
                  Column('created_on', DateTime(), default=datetime.now),
                  Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                  )

products = Table('products', metadata,
                 Column('id', Integer(), primary_key=True),
                 Column('name', String(200), nullable=False),
                 Column('cost_price', Numeric(10, 2), nullable=False),
                 Column('selling_price', Numeric(10, 2), nullable=False),
                 Column('quantity', Integer(), nullable=False),
                 CheckConstraint('quantity >= 0', name='quantity_check')
                 )

orders = Table('orders', metadata,
               Column('id', Integer(), primary_key=True),
               Column('customer_id', ForeignKey('customers.id')),
               Column('date_placed', DateTime(), default=datetime.now),
               Column('date_shipped', DateTime())
               )

orders_products = Table('orders_products', metadata,
                        Column('id', Integer(), primary_key=True),
                        Column('order_id', ForeignKey('orders.id')),
                        Column('product_id', ForeignKey('products.id')),
                        Column('quantity', Integer),
                        CheckConstraint('quantity > 0', name='quantity_check')
                        )

metadata.create_all(engine)
