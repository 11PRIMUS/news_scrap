from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://user:password@localhost/ai_tracker"

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
