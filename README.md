![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![R](https://img.shields.io/badge/r-%23276DC3.svg?style=for-the-badge&logo=r&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
# THIS IS STILL WORK IN PROGRESS!




# Analysis of railroad accidents of 2010-2021




## DATA

 I have downloaded the data from  [here](https://safetydata.fra.dot.gov/officeofsafety/publicsite/on_the_fly_download.aspx) 
  * With these properties: <br>
  ![image](https://user-images.githubusercontent.com/68077710/151796773-874e4c0c-42e4-4279-b4b8-6f2873856ea8.png)

Because we can only download data by each year and not a year range I will manually create a .csv of the data needed.

[2010-2021.csv](https://github.com/koenry/dataScience_PROJECT/blob/main/dotCsvNew/2010_2021_updated.csv) 

[DEMO](https://github.com/koenry/dataScience_PROJECT/blob/main/dotCsvNew/demo.csv) 

<details>
  <summary>DEMO Code</summary>
	https://github.com/koenry/dataScience_PROJECT/blob/main/Code/demo.py	
</details>

### I have created a database and imported the .csv to the database   
<details>
  <summary>Import .csv to DB</summary>
  
I am using postgre database. After table creation we need to import the data, it can be either be done through the GUI but for learning experience I think its best to learn the CLI so I will guide you through the steps.
 
  ```
\COPY railroad2 FROM 'C:\Users\user\someDIR\csv.csv' DELIMITER ',' CSV HEADER;                    --Copy without \ will need permission escalation so its a simple workaround. I will upload the generated .csv to this repo as well for each year. 
  ```
  Now if you get an error:

![ERROR1 WIN](https://user-images.githubusercontent.com/68077710/151793586-d839c9da-d92f-4cce-a670-7580faf82f4e.png)

We need to run the following command:
``` SET CLIENT_ENCODING TO 'utf8'; ```
This is mostly for Windows only systems
</details>

<details>
  <summary>Create a Database</summary>
  
 This is how we create a database with the right columns so we can export the .csv with ease. Why? Because its going to be easier query and import other year data because the .csv files are only generated for the selected year not year range.
  
  ```CREATE TABLE railroad2 (
	"AMTRAK" varchar,
	"IYR" varchar,
	"IMO" varchar,
	"RAILROAD" varchar,
	"INCDTNO" varchar,
	"TYPPERS" varchar,
	"JOBCODE" varchar,
	"NATINJ" varchar,
	"LOCATION" varchar,
	"IFATAL" varchar,
	"OCCODE" varchar,
	"TCODE" varchar,
	"AGE" varchar,
	"DAYSABS" varchar,
	"DAYSRES" varchar,
	"DUMMY" varchar,
	"STATE" varchar,
	"TYPRR" varchar,
	"DUMMY1" varchar,
	"REGION" varchar,
	"DUMMY2" varchar,
	"NARRLEN" varchar,
	"CASFATAL" varchar,
	"CAS57" varchar,
	"CAS54" varchar,
	"DUMMY3" varchar,
	"DAY" varchar,
	"YEAR4" varchar,
	"TIMEHR" varchar,
	"TIMEMIN" varchar,
	"AMPM" varchar,
	"COUNTY" varchar,
	"CNTYCD" varchar,
	"STCNTY" varchar, 
	"ALCOHOL" varchar,
	"DRUG" varchar,
	"PHYACT" varchar,
	"LOCA" varchar,
	"LOCB" varchar,
	"LOCC" varchar,
	"EVENT" varchar,
	"TOOLS" varchar,
	"INJCAUS" varchar,
	"HZMEXPOS" varchar,
	"TERMINAT" varchar,
	"NARR1" varchar,
	"NARR2" varchar,
	"NARR3" varchar,
	"COVERDATA" varchar,
	"LATITUDE" varchar,
	"LONGITUD" varchar,
	"NULL" varchar
);
  ```
</details>

### As we can see with the original .csv we have the state code but not the actual state name. So if we wanted to create a heatmap we need to change the state ids to coresponding state name. I have created a [python script](https://github.com/koenry/dataScience_PROJECT/blob/main/Code/changeStates.py) for this.

<details>
  <summary>Python Script</summary>\
	Our data with the state column has the USA states id code ( not an abbreviation ) ex. 01 - Alabama. So we upload our .csv to a database and write a script to change the state column ids to the coresponding state name.
  Iam using psycopg2 its a Python library for postgres DB. I wanted to learn more about Postgres thats why iam using this database
 Python Code:
  
  ```
	import psycopg2

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


conn = psycopg2.connect(
   database="DataScience", user='postgres', password='sa', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cur = conn.cursor()

i = 1

for w in states:
    if i < 10:
        cur.execute('UPDATE railroad SET "STATE" = \''+states[i]+'\' WHERE "STATE" ='+'\'0'+str(i)+'\';')
        conn.commit()
    elif i > 9:
        cur.execute('UPDATE railroad SET "STATE" = \''+states[i]+'\' WHERE "STATE" ='+'\''+str(i)+'\';')
        conn.commit()
    i+=1
    print(f'{i} Done!')
    
conn.close()


  ```
  Last thing I noticed that district of Columbia and Washington yield separate results so before exporting back to csv lets run a simple sql query to change it to Washington only
```
UPDATE
  TABLE
SET
  "STATE" = 'Washington'
WHERE
  "STATE" = 'District of Columbia';

```
</details>

Cases where drugs or alcohol were involved which lead to death:
<br> <img src="https://user-images.githubusercontent.com/68077710/151950924-eb0fd16d-3b63-415b-b00c-6436fbe70ad4.png" width="300" height="300" /> 
<br> Total drugs and alcohol involved incidents:
<br> <img src="https://user-images.githubusercontent.com/68077710/151952397-42a5ce5a-901b-454a-a52a-255cae82aece.png" width="300" height="300" />
<details>
  <summary>Code</summary>
	https://github.com/koenry/dataScience_PROJECT/blob/main/Code/drugsAlcoDeaths.py	
</details>

	






	
	
