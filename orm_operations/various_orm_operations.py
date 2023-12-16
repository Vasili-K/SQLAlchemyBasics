from sqlalchemy import or_, and_, not_
from sqlalchemy.orm import Session, sessionmaker

from engine_orm_database import engine
from orm_operations.orm_database_schema import Hero

sess = sessionmaker(bind=engine)
session = sess()

h1 = Hero(
    first_name='Bruce',
    last_name='Wayne',
    hero_name='Batman',
    address='Cave',
)

h2 = Hero(
    first_name='Clark',
    last_name='Kent',
    hero_name='Superman',
    address='New York',
)

# Insert in the table

# session.add(h1)
# session.add(h2)
# session.add_all([h1, h2])
# session.commit()

# Select

session.query(Hero).all()
session.query(Hero.id, Hero.first_name).all()
session.query(Hero).count()
session.query(Hero).first()
session.query(Hero).filter(Hero.first_name == 'Bruce').all()

session.query(Hero).filter(or_(
    Hero.first_name == 'Bruce',
    Hero.first_name == 'Clark'
)).all()

session.query(Hero).filter(and_(
    Hero.first_name == 'Bruce',
    not_(
        Hero.last_name == 'Kent',
    )
)).all()

session.query(Hero).filter(Hero.first_name.like("%r")).all()
session.query(Hero).filter(Hero.first_name.ilike("w%")).all()
session.query(Hero).filter(not_(Hero.first_name.like("W%"))).all()

session.query(Hero).limit(2).all()
session.query(Hero).limit(2).offset(2).all()

# Some other methods. Use by analogy with core

"""
    order_by()
    join()
    outerjoin()
    group_by()
    having()
    distinct()
    cast()
    union()
    union_all()
    update()
    delete()
"""

# ORM provides the ability to use raw SQL queries using the text() function.
