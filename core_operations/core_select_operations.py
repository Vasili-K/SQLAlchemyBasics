from sqlalchemy import select, not_, and_, or_, asc, desc, func, update, delete, cast, Integer, Numeric, DateTime, Date, \
    union, text

from core_database_schema import customers, products, orders, orders_products
from engine_creation import engine

conn = engine.connect()

s = customers.select()
s2 = select(customers)
result = conn.execute(s)

# get records from request result: fetchall(), fetchone(), fetchmany(2), first()

# print(result.fetchall())
# print(result.fetchone())
# print(result.fetchmany(2))
# print(result.first())

# print(result.rowcount)
# print(result.keys())
# print(result.scalar())

# row = result.fetchone()
# print(row)
# print(type(row))
# print(row['id'], row['first_name']) # Error
# print(row[0], row[1])
# print(row[customers.c.id], row[customers.c.first_name]) # Error
# print(row.id, row.first_name)

# Record Filtering

s3 = select(products).where(
    products.c.cost_price > 5
)

s4 = select(products). \
    where(products.c.cost_price + products.c.selling_price > 20).where(products.c.quantity > 10)

s5 = select(products).where(
    (products.c.cost_price + products.c.selling_price > 20) &
    (products.c.quantity > 10)
)

s6 = select(products).where(
    (products.c.cost_price > 20) |
    (products.c.quantity < 5)
)

s7 = select(products).where(
    ~(products.c.quantity == 50)
)

s8 = select(products).where(
    ~(products.c.quantity == 50) &
    (products.c.cost_price < 20)
)

# union functions not_, and_, or_

select(products).where(
    and_(
        products.c.quantity >= 50,
        products.c.cost_price < 100,
    )
)

select(products).where(
    or_(
        products.c.quantity >= 50,
        products.c.cost_price < 100,
    )
)

select(products).where(
    and_(
        products.c.quantity >= 50,
        products.c.cost_price < 100,
        not_(
            products.c.name == 'Headphone'
        ),
    )
)

# IS NULL / IS NOT NULL
select(orders).where(
    orders.c.date_shipped == None
)

select(orders).where(
    orders.c.date_shipped != None
)

# IN / NOT IN
select(customers).where(
    customers.c.first_name.in_(["Valeriy", "Vadim"])
)

select(customers).where(
    customers.c.first_name.notin_(["Valeriy", "Vadim"])
)

# BETWEEN / NOT BETWEEN
select(products).where(
    products.c.cost_price.between(10, 20)
)

select(products).where(
    not_(products.c.cost_price.between(10, 20))
)

# LIKE / NOT LIKE
select(products).where(
    products.c.name.like("Wa%")
)

select(products).where(
    not_(products.c.name.like("wa%"))
)

# Sort the result

select(products).where(
    products.c.quantity > 10
).order_by(products.c.cost_price)

select(products).where(
    products.c.quantity > 10
).order_by(asc(products.c.cost_price))

select(products).where(
    products.c.quantity > 10
).order_by(desc(products.c.cost_price))

select(products).order_by(
    products.c.quantity,
    desc(products.c.cost_price)
)

# Limiting results

select(products).order_by(products.c.quantity).limit(2)
select(products).order_by(products.c.quantity).limit(2).offset(1)

# Column Limitation
select(products.c.name, products.c.quantity).where(
    products.c.quantity == 50
)

# with calculations

select(products.c.name, products.c.quantity, products.c.selling_price * 5).where(
    products.c.quantity == 50
)

s10 = select(products.c.name, products.c.quantity, (products.c.selling_price * 5).label('price')).where(
    products.c.quantity == 50
)

# Access built-in functions

c = [

    #  date/time

    func.timeofday(),
    func.localtime(),
    func.current_timestamp(),
    func.date_part("month", func.now()),
    func.now(),

    #  math

    func.pow(4, 2),
    func.sqrt(441),
    func.pi(),
    func.floor(func.pi()),
    func.ceil(func.pi()),

    #  string

    func.lower("ABC"),
    func.upper("abc"),
    func.length("abc"),
    func.trim("  ab c  "),
    func.chr(65),
]

# Grouping results with group_by

c2 = [
    func.count("*").label('count'),
    customers.c.city
]
select(*c).group_by(customers.c.city)

c3 = [
    func.count("*").label('count'),
    customers.c.city
]

select(*c3).group_by(customers.c.city).having(func.count("*") > 2)

# Joins
# join() - creates an inner join
# outerjoin() - creates an outer join (LEFT OUTER JOIN, to be more precise)

s = select(
    orders.c.id.label('order_id'),
    orders.c.date_placed,
    orders_products.c.quantity,
    products.c.name,

).select_from(
    orders.join(customers).join(orders_products).join(products)
).where(
    and_(
        customers.c.first_name == "Tony",
        customers.c.last_name == "Stark",
    )
)

select(
    customers.c.first_name,
    orders.c.id,
).select_from(
    customers.outerjoin(orders)
)

# Updating records

update(products).where(
    products.c.name == 'Water Bottle'
).values(
    selling_price=30,
    quantity=60,
)

# Deleting records

s = delete(customers).where(
    customers.c.username.like('BlackWidow')
)

# rs = conn.execute(s)

# Converting data with cast

s = select(
    cast(func.pi(), Integer),
    cast(func.pi(), Numeric(10, 2)),
    cast("2010-12-01", DateTime),
    cast("2010-12-01", Date),
)

# Union

union(
    select(products.c.id, products.c.name).where(products.c.name.like("Wa%")),
    select(products.c.id, products.c.name).where(products.c.name.like("%e%")),
).order_by(desc("id"))

# Creating Subqueries

s = select(products.c.id, products.c.name).where(
    products.c.id.in_(
        select(orders_products.c.product_id).select_from(customers.join(orders).join(orders_products)).where(
            and_(
                customers.c.first_name == 'Tony',
                customers.c.last_name == 'Stark',
                orders.c.id == 1
            )
        )
    )
)

# "Raw" queries

s = text(
    """
    SELECT
        orders.id as "Order ID", products.id, products.name
    FROM
        customers
    INNER JOIN orders ON customers.id = orders.customer_id
    INNER JOIN orders_products ON orders_products.order_id = orders.id
    INNER JOIN products ON products.id = orders_products.product_id
    where customers.first_name = 'Tony' and customers.last_name = 'Stark'
    """
)

print(s)
rs = conn.execute(s)
print(rs.fetchall())

print(s)
rs = conn.execute(s)
print(rs.fetchall())

# conn.commit()
