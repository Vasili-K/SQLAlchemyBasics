import psycopg2


# Establish a connection with postgres
connection = psycopg2.connect(dbname="postgres", user="postgres", password="12345_12345", host="localhost", port="5432")
connection.autocommit = True

# Create a cursor to perform database operations
cursor = connection.cursor()

#Preparing query to create a database
sql = "CREATE database sqlalchemy_basics"


#Creating a database
cursor.execute(sql)
print("Database created successfully........")

# Close connection
connection.close()
