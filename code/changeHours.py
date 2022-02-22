import psycopg2

conn = psycopg2.connect(
   database="DataScience", user='postgres', password='sa', host='127.0.0.1', port= '5432'
)

cur = conn.cursor()

i = 1
ii = 13 
while i < 12: 
    command = 'UPDATE railroad SET "TIMEHR" = \''+str(ii)+'\' WHERE "AMPM" = \'PM\' AND "TIMEHR" = \''+ str(i)+'\''
    print(command)
    cur.execute(command)
    i+=1
    ii+=1
    conn.commit()

command2 = 'UPDATE railroad SET "TIMEHR" = \'24\' WHERE "AMPM" = \'AM\' AND "TIMEHR" = \'12\'' # 24h is 12am
print(command2)
cur.execute(command2)
conn.commit()

conn.close()

