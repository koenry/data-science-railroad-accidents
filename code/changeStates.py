import psycopg2
# some of the values are null because the numbers skipped
# Which of total we get of 56 but we have 50 states - some of the numbers are skipped

states = ['null', 'Alabama', 'Alaska', 'null', 'Arizona', 'Arkansas',
'California', 'null', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
'Florida', 'Georgia','null', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa',
'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts',
'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
'Pennsylvania', 'null', 'Rhode Island', 'South Carolina',
'South Dakota', 'Tennessee', 'Texas', 'Utah' , 'Vermont',
'Virginia', 'null', 'Washington', 'West Virginia', 'Wisconsin',
'Wyoming'
]

# Connect to postgre db
conn = psycopg2.connect(
   database="DataScience", user='postgres', password='sa', host='127.0.0.1', port= '5432'
)
#Create a cursor object using the cursor() method
cur = conn.cursor()

i = 1

for w in states:
    if i < 10: # because the first numbers contain a zero
        cur.execute('UPDATE fulldatasates SET "STATE" = \''+states[i]+'\' WHERE "STATE" ='+'\'0'+str(i)+'\';') 
        conn.commit()
    elif i > 9:
        cur.execute('UPDATE fulldatasates SET "STATE" = \''+states[i]+'\' WHERE "STATE" ='+'\''+str(i)+'\';')
        conn.commit() # Never forget to comit changes for its scope or else the change is only local!
    i+=1
    print(f'{i} Done!') # Print out some feedback so the user knows the script is running
    
conn.close()


# QUICK NOTES about the lack of f strings on cur.execute, seems like SQL queries have some sort of problem when executing from python f strings?
# Needs more testing but f strings would make the code a little more readable
