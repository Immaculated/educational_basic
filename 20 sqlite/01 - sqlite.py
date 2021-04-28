# there are theory and homework without some prints. works fine in jupiter
import sqlite3
import pandas as pd

conndb = sqlite3.connect("my_database.db") # create DB
cursor = conndb.cursor()

cursor.execute(
    """CREATE TABLE  albums(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    artist TEXT, 
    title TEXT, 
    label TEXT,
    units_mln INT,
    year INT)
    """
)

albums = [('Pink Floyd', 'The Wall', 'Columbia Records', 23, 1979),
          ('Pink Floyd', 'The Wall', 'Columbia Records', 23, 1979),
          ('Pink Floyd', 'The Wall', 'Columbia Records', 23, 1979)]
 
cursor.executemany(
    "INSERT INTO albums(artist, title, label, units_mln, year) VALUES (?,?,?,?,?)", 
    albums
)
conndb.commit()

cursor.execute(
    """SELECT name FROM sqlite_master WHERE type='table'"""
).fetchall()

cursor.execute("UPDATE albums SET year=? WHERE id=?", (1970, 3))

for row in cursor.execute("SELECT * FROM albums"):
    print(row)
    
cursor.execute("""DROP TABLE albums""") 
conndb.commit()


data = pd.read_excel('art.xls')
data.head()
data.to_sql('albums',conndb)
SQLres = cursor.execute(
    """
    SELECT * FROM albums 
    WHERE `year` > 1980 
    AND units_mln <33
    ORDER BY units_mln DESC 
    LIMIT 0, 10
""" 
)
for row in SQLres:
    print(row)
for row in cursor.execute("""
SELECT * FROM `albums` 
WHERE `year` > 1976  
ORDER BY `units_mln` DESC LIMIT 0, 10
"""):
    print(row)
cursor.execute(
    """
    SELECT
        label,
        COUNT(label),
        MIN(year) AS min_year
    FROM
        albums
    GROUP BY
        label
    ORDER BY min_year;
    """
).fetchall()

# HOMEWORK

# Самый свежий альбом
cursor.execute(
    """
    SELECT
        artist,
        title,
        label,
        units_mln,
        MAX(year)      
    FROM
        albums;
    """
).fetchall()

# Сколько альбомов было выпущено в 1987 году.
count = 0
for row in cursor.execute("""
SELECT * FROM `albums`
WHERE year == 1987;
"""):
    count += 1
    print(row)
print('Quantity of albums were released in 1987 = ', count)

# Кто выпустил самый успешный альбом до 1987 года включительно?
cursor.execute("""
    SELECT *, MAX(units_mln) 
    FROM albums
    WHERE year <= 1987
 """
).fetchall()

# Кто выпустил самый успешный альбом после 1987г?
cursor.execute("""
    SELECT *, MAX(units_mln) 
    FROM albums
    WHERE year >1987  
 """
).fetchall()

# Сколько всего копий альбомов 1987 года было продано?
copies = 0
for row in cursor.execute("""
SELECT * FROM `albums`
WHERE year==1987;
"""):
    copies += row[-2]
print('There was sold out ', copies, ' albums in 1987')

# Какой исполнитель выпустил больше всего альбомов?
cursor.execute(
    """
    SELECT
        artist,
        MAX(units_mln)      
    FROM
        albums;
    """
).fetchall()

# В каком году было выпущено больше всего альбомов?
cursor.execute("""
    SELECT year, count(title) as count 
    FROM albums
    GROUP BY year
    ORDER BY -count
 """
).fetchall()

# Альбомы какого года продавались лучше?
cursor.execute("""
    SELECT year, sum(units_mln) as sum 
    FROM albums
    GROUP BY year
    ORDER BY -sum
 """
).fetchall()