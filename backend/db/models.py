from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/ai_launch_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String)
    title = Column(String)
    link = Column(String)
    summary = Column(String)

def init_db():
    Base.metadata.create_all(bind=engine)

def store_news(news_list):
    session = SessionLocal()
    for news in news_list:
        session.add(News(**news))
    session.commit()
    session.close()
