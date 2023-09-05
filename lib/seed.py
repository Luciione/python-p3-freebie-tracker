#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Company, Dev



Session = sessionmaker(bind=engine)
session = Session()

# Create sample data
company1 = Company(name='Company A', founding_year=2000)
company2 = Company(name='Company B', founding_year=2010)
company3 = Company(name='Company C', founding_year=2020)

dev1 = Dev(name='Dev X')
dev2 = Dev(name='Dev Y')
dev3 = Dev(name='Dev Z')


session.add_all([company1, company2, company3, dev1, dev2, dev3])


session.commit()


session.close()
