import psycopg2

if __name__ == "__main__":
    print(f"Hello, World!")

    #establishing the connection
    conn = psycopg2.connect(
        database="sample-python-project", user='db_user', password='db_password', host='127.0.0.1', port= '5432'
    )


    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute("select version()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Connection established to: ",data)

    #Closing the connection
    conn.close()

    print(f"Good-Bye, World!")