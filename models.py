from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, ForeignKey, Table
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table('pizza_choice', Base.metadata,
                          Column('pizza_id', Integer, ForeignKey('pizza.identifier')),
                          Column('choice_id', Integer, ForeignKey('choice.identifier'))
                          )


class Pizza(Base):
    __tablename__ = "pizza"
    identifier = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    choices = relationship(
        'Choice',
        secondary=association_table
    )

    def __str__(self):
        return self.title


class Choice(Base):
    __tablename__ = "choice"
    identifier = Column(Integer, primary_key=True)
    title = Column(String(100))
    price = Column(Integer)

    def __str__(self):
        return "%s - %sруб." % (self.title, self.price)
