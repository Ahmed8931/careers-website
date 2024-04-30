from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:@localhost/testco.db",pool_pre_ping=True)

Base = declarative_base()
class Job(Base):
  __tablename__ = 'jobs'

  id = Column(Integer,primary_key=True)
  title = Column(String,nullable=False)
  location = Column(String)
  salary = Column(Integer,nullable = True)
  currency = Column(String)
  responsibilities = Column(String)
  requirements = Column(String)
  def __repr__(self):
    return f"{self.title} - {self.location}"
Session = sessionmaker(bind=engine)
session = Session()

jobs = session.query(Job).all()
for job in jobs:
  print(job)