from sqlalchemy import create_engine

from env_variables import USER_NAME, POSTGRES_PASSWORD

engine = create_engine(f"postgresql+psycopg2://{USER_NAME}:{POSTGRES_PASSWORD}@localhost/dc_super_heroes")


engine.connect()
