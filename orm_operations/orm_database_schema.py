from sqlalchemy import Column, Integer, String, DateTime, PrimaryKeyConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

from sqlalchemy.orm import relationship

from engine_orm_database import engine

Base = declarative_base()


class Hero(Base):
    __tablename__ = 'heroes'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    hero_name = Column(String(150), nullable=False, unique=True)
    address = Column(String(250))
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Capability(Base):
    __tablename__ = 'capabilities'
    id = Column(Integer())
    title = Column(String(250), nullable=False)
    system_code = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='capability_pk'),
        UniqueConstraint('system_code'),
    )


class CapabilitySet(Base):
    __tablename__ = 'capability_sets'
    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer(), ForeignKey('heroes.id'))
    date_created = Column(DateTime(), default=datetime.now)
    line_items = relationship("CapabilityLine", backref='CapabilitySet')


class CapabilityLine(Base):
    __tablename__ = 'capability_lines'
    id = Column(Integer, primary_key=True)
    capability_set_id = Column(Integer(), ForeignKey('capability_sets.id'))
    capability_id = Column(Integer(), ForeignKey('capabilities.id'))
    capability = relationship("Capability")


Base.metadata.create_all(engine)
