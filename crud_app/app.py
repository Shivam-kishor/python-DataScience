#from unicodedata import category
#rom zipapp import create_archive
import streamlit as st
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.ext.declarative import decleartive_base
from datetime import datetime

# from traitlets import default


#create  a model class
Base=declarative_base() #biolerplate code

class Food(Base):
    __tablename__='foodP_table'
    id=Column(Integer,primary_key=True)
    title=Column(String(100),unique=True)
    duration=Column(Integer,defualt=2)
    ingredients=Column(String)
    category=Column(String(7),default='veg')
    kind=Column(String(50),default='south-indian')
    created_on=Column(Date,default=datetime.now())
    def __str__(self):
        return f'{self.title} ({self.kind})'


#create databse
engine=create_engine('sqlite://food.sqlite',echo=True)# blank databse
Base.metadata.Create_all(engine)


#open the databse
def open_db():
    Session=sessionmaker(bind=engine)
    return Session()

#save data in db
def save_food(title,duration=2,ingredients='',category='veg',kind='south-indian'):
    db=open_db
    food=Food(title=title,duration=duration,ingredients=ingredients,category=category,kind=kind) 
    db.add(food)
    db.coomit()
    db.close()
    return foods

def delete_food(id):
    db=open_db()
    try:
        db.query(Food).filter(Food.id==id).delete()
        db.open_db()
    except Exception as e:
        st.error(f'Error:{e}')
    finally:
        db.close()


#ui using streamlit
st.title('Food CRUD App')

with st.form st.text_input('Title')



