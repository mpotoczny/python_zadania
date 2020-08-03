import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="zawodnicy",
    user="postgres",
    password="abc",
    port="5432"
)

cur = conn.cursor()
cur.execute("select * from zawodnicy")

dane = cur.fetchall()
# print(dane)
# print(type(dane))

for zawodnik in dane:
   print(zawodnik[1], zawodnik[4])

sql = "insert into zawodnicy (id_skoczka, imie, nazwisko) values (%s, %s, %s)"
dane = (20, "Piotr", "GG")
cur.execute(sql,dane)
conn.commit()