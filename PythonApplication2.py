import sqlite3
db= sqlite3.connect('ogog.db')
c = db.cursor()
c.execute('''DROP TABLE gru1''')
db.commit()
c.execute('''
    CREATE TABLE gru1 (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(60),
	phone VARCHAR(60));
    '''
    )
db.commit()
for i in range(3):
    f = str(input('1 INPUT:'))
    h = str(input('2 INPUT:'))
    c.execute('''INSERT INTO gru1 (name, phone) VALUES('{0}','{1}')'''.format(f,h))
    c.execute('''SELECT * FROM gru1''')
for ex in c.fetchall():
    print(ex)