import sqlite3 as sql

connection = sql.connect("dabaseMovies.db")

pointer = connection.cursor()
pointer.execute("CREATE TABLE IF NOT EXISTS MOVIES( NAME TEXT, ACTOR TEXT, ACTRESS TEXT,DIRECTOR_NAME TEXT, YEAR INTEGER )")
pointer.execute("INSERT INTO MOVIES VALUES('Master','vijay','malavika mohan','vijay sethupathi',2021)")
pointer.execute("INSERT INTO MOVIES VALUES('maari','dhanush','kajal agarwal','bad ravi',2015)")
pointer.execute("INSERT INTO MOVIES VALUES('vikram','kamal hassan','gayathri','fahadh fassil',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('maaran','dhanush','rathi','ameer',2022)")
pointer.execute("INSERT INTO MOVIES VALUES('beast','nelson','pooja','selva',2021)")

print("*********Everything in the database*********")
allMovies = pointer.execute("SELECT * FROM MOVIES").fetchall()
for i in allMovies:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")

print("*********Actor Query*********")
actorQuery = pointer.execute("SELECT * FROM MOVIES WHERE ACTOR = 'vijay'").fetchall()
for i in actorQuery:
  title,actor,actress,director,releasedYear = i
  print("{t}\t\t{a}\t\t{ats}\t\t{d}\t\t{ry}".format(t=title,a=actor, ats=actress,d=director,ry=releasedYear))
  print("============================================================================================")