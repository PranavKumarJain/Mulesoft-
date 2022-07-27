# Importing Packages
import sqlite3
import pandas as pd

# Creating DB using SQLiteJDBC driver
db = sqlite3.connect('../DB/movies.db')

# DB Cursor
cursor = db.cursor()

# Creating Table
cursor.execute('''CREATE TABLE movies(id INTEGER PRIMARY KEY, Movie_Name TEXT, Lead_Actor TEXT, Lead_Actress TEXT, Year_Of_Release YEAR, Director_Name TEXT)''')

# Inserting Data
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(1,"Laal Singh Chaddha","Aamir Khan","Kareena Kapoor",2022,"Advait Chandan")''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(2,"Brahmastra Part One: Shiva","Ranbir Kapoor","Alia Bhatt",2022,"Ayan Mukherjee")''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(3,"Raksha Bandhan","Akshay Kumar","Bhumi Pednekar",2022,"Aanand L. Rai")''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(4,"Ek Villain Returns","John Abraham","Disha Patani",2022,"Mohit Suri")''')
cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress, Director_Name,Year_Of_Release) VALUES(5,"VR (Vikrant Rona)","Sudeep","Neetha Ashok",2022,"Anup Bhandari")''')

# SELECT statement to query all rows from 'movies'
sqlite_select_query = """SELECT * from movies"""
cursor.execute(sqlite_select_query)
records = cursor.fetchall()
print("\n")
print("Full Database")
print(pd.DataFrame(records,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Year_Of_Release","Director_Name"]))
print("\n")

# SELECT query with parameter like actor name to select movies based on the actor's name
sqlite_select_query = """SELECT * from movies where Lead_Actor = 'Ranbir Kapoor'"""
cursor.execute(sqlite_select_query)
records_select = cursor.fetchall()
print("Movies filter based on an Actor")
print(pd.DataFrame(records_select,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Year_Of_Release","Director_Name"]))
print("\n")

# User Input
print("Enter 0: Exit")
print("Enter 1: Insert new movie details")
print("Enter 2: View movie details with your favourite actor name")
while True:
    inp = int(input("Enter your choice: "))
    if inp == 0:
        break
    elif inp == 1:
        movie_name = input("Enter movie name: ")
        lead_actor = input("Enter lead actor: ")
        lead_actress = input("Enter lead actress: ")
        year_of_release = int(input("Enter year of release: "))
        director_name = input("Enter director name: ")
        cursor.execute('''INSERT INTO movies(id, Movie_Name, Lead_Actor, Lead_Actress ,Year_Of_Release, Director_Name) VALUES(?,?,?,?,?,?)''',(len(records)+1,movie_name,lead_actor,lead_actress,year_of_release,director_name))
        db.commit()
        print("Movie details inserted")
    elif inp == 2:
        print("Enter the query")
        query = input()
        cursor.execute(query)
        records = cursor.fetchall()
        print(pd.DataFrame(records_select,columns = ["ID","Movie_Name","Lead_Actor","Lead_Actress","Year_Of_Release","Director_Name"]))