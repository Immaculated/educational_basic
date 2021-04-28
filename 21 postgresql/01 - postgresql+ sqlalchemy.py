from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:123@localhost/postgres", echo=True)

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    posts = relationship("Post")
    comments = relationship("Comment")
    def __repr__(self):
        return f'Пользователь:{self.login}'
    
class Post(Base):
    __tablename__ = 'posts'
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key=True, autoincrement='auto')
    title = Column(String)
    text = Column(String)
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    def __init__(self, **kwargs):
        now = datetime.now()
        super().__init__(date=datetime.strftime(now, "%Y.%m.%d %H:%M:%S "), **kwargs)

    def __repr__(self):
        return f'Постс с текстом: {self.text}' 
      
class Comment(Base):
    __tablename__ = 'comments'
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key=True, autoincrement='auto')
    text = Column(String)
    date = Column(DateTime)
    # post_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    def __init__(self, **kwargs):
        now = datetime.now()
        super().__init__(date=datetime.strftime(now, "%Y.%m.%d %H:%M:%S "),  **kwargs)
        
    def __repr__(self):
        return f'Комментарий с текстом: {self.text}'
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
users = session.query(User).all()
posts =  session.query(Post).all()
commentt = session.query(Comment).all()
post = Post(title='Title_4123', text='Random_ajshdh123')
comment = Comment(text='askdpokovdsy')