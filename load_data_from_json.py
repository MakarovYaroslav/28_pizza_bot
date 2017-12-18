from sqlalchemy.orm import sessionmaker
from create_db import engine
from models import Pizza, Choice, Base
import json
import argparse

session = sessionmaker()
session.configure(bind=engine)
s = session()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with open(args.filename, "r") as file:
        catalog = json.load(file)

    for pizza in catalog:
        new_pizza = Pizza(title=pizza['title'],
                          description=pizza['description'])
        for choice in pizza['choices']:
            new_choice = Choice(title=choice['title'],
                                price=int(choice['price']))
            new_pizza.choices.append(new_choice)
        s.add(new_pizza)

    s.commit()
