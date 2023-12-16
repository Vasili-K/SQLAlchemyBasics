import psycopg2

from env_variables import USER_NAME, POSTGRES_PASSWORD

# Establish a connection with postgres
conn = psycopg2.connect(
    database="postgres",
    user=USER_NAME,
    password=POSTGRES_PASSWORD,
    host="localhost",
    port="5432"
)
conn.autocommit = True

# Create a cursor to perform database operations
cursor = conn.cursor()

# Preparing query to create a database
sql = ''' CREATE database dc_super_heroes ''';


#Creating a database
cursor.execute(sql)
print("Database created successfully........")

# Close connection
conn.close()
