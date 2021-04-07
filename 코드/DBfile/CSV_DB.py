import pymysql
import csv

#DB connection
conn = pymysql.connect(host='localhost', user='dongyeon0317', password='1Q2w3e4r!@', db='crime_prediction', charset='utf8')
curs = conn.cursor()
idx = int(input("1.Crime 2.Artificial 3.Weather 4.CCTV 5.Police_Station 6.Resident 7.Floating 8.grid_num"))

#Crime table
if idx == 1:    
    year = int(input("input year: "))
    file_name = 'crime_data_' + str(year) + '.csv'
    sql = "insert into Crime (type, date_time, latitude, longitude, grid) values (%s, %s, %s, %s, %s)"
    f = open(file_name, 'r', encoding='utf-8')
    rd = csv.reader(f)
    for line in rd:
        curs.execute(sql, (line[0], line[1], line[2], line[3], line[4])) #type, datetime, latitude, longitude, grid 
    f.close()
    print("Query OK!")
    
#Artificial table
elif idx == 2:    
    year = int(input("input year: "))
    file_name = 'artificial_data_' + str(year) + '.csv'
    sql = "insert into Crime (type, date_time, latitude, longitude, grid) values (%s, %s, %s, %s, %s)"
    f = open(file_name, 'r', encoding='utf-8')
    rd = csv.reader(f)
    for line in rd:
        curs.execute(sql, (line[0], line[1], line[2], line[3], line[4])) #type, datetime, latitude, longitude, grid 
    f.close()
    print("Query OK!")    
    
#Weather table
elif idx == 3:
    year = int(input("input year: "))
    file_name = 'Weather_Seoul_HR_' + str(year) + '.csv'
    sql = "insert into Weather (date_time, temperature, rainfall, windspeed, humidity, sunshine, snowfall, cloud) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    f = open(file_name, 'r', encoding='utf-8')
    rd = csv.reader(f)
    for line in rd:
        # exception for excel blank
        value = []
        for i in range(0,8):
            if line[i] == "":
                value.append(0)
            else:
                value.append(line[i])
        curs.execute(sql, (value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7])) #datetime, temperature, rainfall, windspeed, humidity, sunshine, snowfall, cloud 
    f.close()
    print("Query OK!")

#CCTV table
elif idx == 4:
    sql = "insert into CCTV (latitude, longitude, CCTV_num, grid) values (%s, %s, %s, %s)"
    f = open('CCTV.csv', 'r', encoding='utf-8')
    rd = csv.reader(f)
    for line in rd:
        curs.execute(sql, (line[0], line[1], line[2], line[3])) #latitude, longitude, CCTV_num, grid 
    f.close()

#Police table
elif idx == 5:
    sql = "insert into Police (latitude, longitude, grid, police_value) values (%s, %s, %s, %s)"
    f = open('Police_Station.csv', 'r', encoding='utf-8')
    rd = csv.reader(f)
    for line in rd:
        curs.execute(sql, (line[0], line[1], line[2], line[3])) #latitude, longitude, grid, police_value 
    f.close()
    
#Resident table
elif idx == 6:
    sql = "insert into Resident (grid, population) values (%s, %s)"
    f = open('Resident.csv', 'r', encoding='utf-8')
    rd = csv.reader(f)
    for line in rd:
        curs.execute(sql, (line[0], line[1])) # Grid, Population
    f.close()

#Floating table
elif idx == 7:
    sql = "insert into Floating (grid, time, population) values (%s, %s, %s)"
    f = open('Floating.csv', 'r', encoding='utf-8')
    rd = csv.reader(f)
    for line in rd:
        curs.execute(sql, (line[0], line[1], line[2])) # grid, time, population
    f.close()

#Grid_num table    
else:
    sql = "insert into Grid_num (num) values (%s)"
    f = open('grid_num.csv', 'r', encoding='utf-8')
    rd = csv.reader(f)
    for line in rd:
        curs.execute(sql, (line[0])) 
    f.close()
    
conn.commit()
conn.close()

