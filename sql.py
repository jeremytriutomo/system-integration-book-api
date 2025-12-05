from sqlalchemy import create_engine

engine = create_engine("postgresql://myuser:12345678a@localhost:5432/mydb_test")