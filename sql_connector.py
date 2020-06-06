import mysql.connector

def connect_and_fetch(word):
    connection = mysql.connector.connect(user="ardit700_student", password="ardit700_student",
                                        host="108.167.140.122", database="ardit700_pm1database")

    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM Dictionary WHERE Expression = "{word}"')
    results = cursor.fetchall()
    
    return results