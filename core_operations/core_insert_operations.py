from sqlalchemy import insert

from core_database_schema import customers, products, orders, orders_products
from engine_creation import engine


conn = engine.connect()

# Inserting records

# insert() method of Table instance

first_customer = customers.insert().values(
    first_name='Tony',
    last_name='Stark',
    username='IronMan',
    email='jackass@gmail.com',
    address='Main street, bld. 8/10, appt. 23',
    city='New York'
)

customer = conn.execute(first_customer)

# insert() function from the sqlalchemy library


ins = insert(customers).values(
    first_name='Piter',
    last_name='Parker',
    username='SpiderMan',
    email='good_guy@gmail.com',
    address='Second, bld. 8, appt. 37',
    city='New York'
)

# add several elements

new_customers = [
    {
        "first_name": "Natasha",
        "last_name": "Romanov",
        "username": "BlackWidow",
        "email": "killer_one@gmail.com",
        "address": "Unknown",
        "city": "New York"
    },
    {
        "first_name": "Steve",
        "last_name": "Rogers",
        "username": "CaptainAmerica",
        "email": "the_firs@gmail.com",
        "address": "Main street, 7/8",
        "city": "New York"
    },
]

ins2 = insert(customers)

conn.execute(ins2, new_customers)


product_list = [
    {
        "name": "Chair",
        "cost_price": 9.21,
        "selling_price": 10.81,
        "quantity": 6
    },
    {
        "name": "Pen",
        "cost_price": 3.45,
        "selling_price": 4.51,
        "quantity": 3
    },
    {
        "name": "Headphone",
        "cost_price": 15.52,
        "selling_price": 16.81,
        "quantity": 50
    },
]

order_list = [
    {
        "customer_id": 1
    },
    {
        "customer_id": 1
    }
]

order_product_list = [
    {
        "order_id": 1,
        "product_id": 1,
        "quantity": 5
    },
    {
        "order_id": 1,
        "product_id": 2,
        "quantity": 2
    },
    {
        "order_id": 1,
        "product_id": 3,
        "quantity": 1
    },
    {
        "order_id": 2,
        "product_id": 1,
        "quantity": 5
    },
    {
        "order_id": 2,
        "product_id": 2,
        "quantity": 5
    },
]

conn.execute(insert(products), product_list)
conn.execute(insert(orders), order_list)
conn.execute(insert(orders_products), order_product_list)

conn.commit()
