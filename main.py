from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:12345_12345@localhost/sqlalchemy_basics",
    echo=True, pool_size=6, max_overflow=10
)

engine.connect()

print(engine)
