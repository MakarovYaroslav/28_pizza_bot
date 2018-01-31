from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship


Base = declarative_base()


class Pizza(Base):
    __tablename__ = 'pizza'
    identifier = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    choices = relationship(
        'Choice',
        secondary='pizza_link'
    )

    def __str__(self):
        return self.title


class Choice(Base):
    __tablename__ = 'choice'
    identifier = Column(Integer, primary_key=True)
    title = Column(String(100))
    price = Column(Integer)

    def __str__(self):
        return "%s - %sруб." % (self.title, self.price)


class PizzaChoiceLink(Base):
    __tablename__ = 'pizza_link'
    pizza_id = Column(Integer,
                      ForeignKey('pizza.identifier'),
                      primary_key=True)
    choice_id = Column(Integer,
                       ForeignKey('choice.identifier'),
                       primary_key=True)
