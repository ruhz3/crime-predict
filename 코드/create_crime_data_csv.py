############ create crime data as csv ############
import random

# create file
f = open("crime_data.csv", "w")

# save label
f.write("Type" + ", " + "Date-Time" + ", " + "Latitude" + ", " + "Longitude" + "\n")

############################# random #############################
# create Theft data (1050)
for i in range(2, 1052):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5546645, 37.56886886)) + ", " + 
    str(random.uniform(126.96777894, 127.0176931)) + "\n")

# create Assault data (950)
for i in range(1052, 2002):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5546645, 37.56886886)) + ", " + 
    str(random.uniform(126.96777894, 127.0176931)) + "\n")

# create Sexaul Harassment data (100)
for i in range(2002, 2102):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5546645, 37.56886886)) + ", " + 
    str(random.uniform(126.96777894, 127.0176931)) + "\n")

############################# 2 #############################
# create Theft data (180)
for i in range(0, 180):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5492475, 37.5545530)) + ", " + 
    str(random.uniform(126.9916576, 127.0143248)) + "\n")

# create Assault data (160)
for i in range(0, 160):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5492475, 37.5545530)) + ", " + 
    str(random.uniform(126.9916576, 127.0143248)) + "\n")

# create Sexual Harassment data (20)
for i in range(0, 20):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5492475, 37.5545530)) + ", " + 
    str(random.uniform(126.9916576, 127.0143248)) + "\n")

############################# 3 #############################
# create Theft data (115)
for i in range(0, 115):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5573879, 37.5708829)) + ", " + 
    str(random.uniform(127.0175972, 127.0233386)) + "\n")

# create Assault data (100)
for i in range(0, 100):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5573879, 37.5708829)) + ", " + 
    str(random.uniform(127.0175972, 127.0233386)) + "\n")

# create Sexual Harassment data (15)
for i in range(0, 15):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5573879, 37.5708829)) + ", " + 
    str(random.uniform(127.0175972, 127.0233386)) + "\n")

############################# 4 #############################
# create Theft data (45)
for i in range(0, 45):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5544505, 37.5598302)) + ", " + 
    str(random.uniform(126.9621857, 126.9678786)) + "\n")

# create Assault data (40)
for i in range(0, 40):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5544505, 37.5598302)) + ", " + 
    str(random.uniform(126.9621857, 126.9678786)) + "\n")

# create Sexual Harassment data (5)
for i in range(0, 5):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5544505, 37.5598302)) + ", " + 
    str(random.uniform(126.9621857, 126.9678786)) + "\n")

############################# 5 #############################
# create Theft data (36)
for i in range(0, 36):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5438144, 37.5492054)) + ", " + 
    str(random.uniform(127.0052766, 127.0098404)) + "\n")

# create Assault data (32)
for i in range(0, 32):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5438144, 37.5492054)) + ", " + 
    str(random.uniform(127.0052766, 127.0098404)) + "\n")

# create Sexual Harassment data (4)
for i in range(0, 4):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5438144, 37.5492054)) + ", " + 
    str(random.uniform(127.0052766, 127.0098404)) + "\n")

############################# 6 #############################
# create Theft data (30)
for i in range(0, 30):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5509521, 37.5545297)) + ", " + 
    str(random.uniform(126.9859963, 126.9916777)) + "\n")

# create Assault data (27)
for i in range(0, 27):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5509521, 37.5545297)) + ", " + 
    str(random.uniform(126.9859963, 126.9916777)) + "\n")

# create Sexual Harassment data (3)
for i in range(0, 3):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5509521, 37.5545297)) + ", " + 
    str(random.uniform(126.9859963, 126.9916777)) + "\n")

############################# 7 #############################
# create Theft data (33)
for i in range(0, 33):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5527263, 37.5544725)) + ", " + 
    str(random.uniform(126.9735413, 126.9860058)) + "\n")

# create Assault data (29)
for i in range(0, 29):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5527263, 37.5544725)) + ", " + 
    str(random.uniform(126.9735413, 126.9860058)) + "\n")

# create Sexual Harassment data (4)
for i in range(0, 4):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5527263, 37.5544725)) + ", " + 
    str(random.uniform(126.9735413, 126.9860058)) + "\n")

############################# 8 #############################
# create Theft data (15)
for i in range(0, 15):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5689393, 37.5697908)) + ", " + 
    str(random.uniform(126.9723007, 126.9836303)) + "\n")

# create Assault data (13)
for i in range(0, 13):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5689393, 37.5697908)) + ", " + 
    str(random.uniform(126.9723007, 126.9836303)) + "\n")

# create Sexual Harassment data (2)
for i in range(0, 2):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5689393, 37.5697908)) + ", " + 
    str(random.uniform(126.9723007, 126.9836303)) + "\n")

############################# 9 #############################
# create Theft data (25)
for i in range(0, 25):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5690853, 37.5699044)) + ", " + 
    str(random.uniform(126.9983472, 127.0176016)) + "\n")

# create Assault data (22)
for i in range(0, 22):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5690853, 37.5699044)) + ", " + 
    str(random.uniform(126.9983472, 127.0176016)) + "\n")

# create Sexual Harassment data (4)
for i in range(0, 4):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5690853, 37.5699044)) + ", " + 
    str(random.uniform(126.9983472, 127.0176016)) + "\n")

############################# 10 #############################
# create Theft data (21)
for i in range(0, 21):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5600986, 37.5727126)) + ", " + 
    str(random.uniform(127.0232410, 127.0244540)) + "\n")

# create Assault data (19)
for i in range(0, 19):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5600986, 37.5727126)) + ", " + 
    str(random.uniform(127.0232410, 127.0244540)) + "\n")

# create Sexual Harassment data (2)
for i in range(0, 2):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5600986, 37.5727126)) + ", " + 
    str(random.uniform(127.0232410, 127.0244540)) + "\n")

############################# 11 #############################
# create Theft data (12)
for i in range(0, 12):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5619098, 37.5655062)) + ", " + 
    str(random.uniform(127.0244196, 127.0267064)) + "\n")

# create Assault data (11)
for i in range(0, 11):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5619098, 37.5655062)) + ", " + 
    str(random.uniform(127.0244196, 127.0267064)) + "\n")

# create Sexual Harassment data (1)
for i in range(0, 1):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5619098, 37.5655062)) + ", " + 
    str(random.uniform(127.0244196, 127.0267064)) + "\n")

############################# 12 #############################
# create Theft data (6)
for i in range(0, 6):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5709116, 37.5717914)) + ", " + 
    str(random.uniform(127.0187169, 127.0232510)) + "\n")

# create Assault data (5)
for i in range(0, 5):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5709116, 37.5717914)) + ", " + 
    str(random.uniform(127.0187169, 127.0232510)) + "\n")

# create Sexual Harassment data (0)
#for i in range(0, 0):
#    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
#    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
#    
#    f.write("Sexaul Harassment" + ", " + 
#    str(date) + " " + str(time) + ", " + 
#    str(random.uniform(37.5709116, 37.5717914)) + ", " + 
#    str(random.uniform(127.0187169, 127.0232510)) + "\n")

############################# 13 #############################
# create Theft data (6)
for i in range(0, 6):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5474326, 37.5492220)) + ", " + 
    str(random.uniform(127.0098079, 127.0120788)) + "\n")

# create Assault data (5)
for i in range(0, 5):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5474326, 37.5492220)) + ", " + 
    str(random.uniform(127.0098079, 127.0120788)) + "\n")

# create Sexual Harassment data (1)
for i in range(0, 1):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5474326, 37.5492220)) + ", " + 
    str(random.uniform(127.0098079, 127.0120788)) + "\n")

############################# 14 #############################
# create Theft data (9)
for i in range(0, 9):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5473675, 37.5491551)) + ", " + 
    str(random.uniform(126.9939592, 126.9973658)) + "\n")

# create Assault data (7)
for i in range(0, 7):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5473675, 37.5491551)) + ", " + 
    str(random.uniform(126.9939592, 126.9973658)) + "\n")

# create Sexual Harassment data (2)
for i in range(0, 2):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5473675, 37.5491551)) + ", " + 
    str(random.uniform(126.9939592, 126.9973658)) + "\n")

############################# 15 #############################
# create Theft data (12)
for i in range(0, 12):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5519494, 37.5546495)) + ", " + 
    str(random.uniform(127.0142998, 127.0177351)) + "\n")

# create Assault data (10)
for i in range(0, 10):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5519494, 37.5546495)) + ", " + 
    str(random.uniform(127.0142998, 127.0177351)) + "\n")

# create Sexual Harassment data (2)
for i in range(0, 2):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5519494, 37.5546495)) + ", " + 
    str(random.uniform(127.0142998, 127.0177351)) + "\n")

############################# 16 #############################
# create Theft data (6)
for i in range(0, 6):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5598616, 37.5616501)) + ", " + 
    str(random.uniform(126.9655664, 126.9678445)) + "\n")

# create Assault data (5)
for i in range(0, 5):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5598616, 37.5616501)) + ", " + 
    str(random.uniform(126.9655664, 126.9678445)) + "\n")

# create Sexual Harassment data (1)
for i in range(0, 1):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5598616, 37.5616501)) + ", " + 
    str(random.uniform(126.9655664, 126.9678445)) + "\n")

############################# 17 #############################
# create Theft data (12)
for i in range(0, 12):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))

    f.write("Theft" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5526404, 37.5544163)) + ", " + 
    str(random.uniform(126.9610906, 126.9656221)) + "\n")

# create Assault data (10)
for i in range(0, 10):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Assault" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5526404, 37.5544163)) + ", " + 
    str(random.uniform(126.9610906, 126.9656221)) + "\n")

# create Sexual Harassment data (2)
for i in range(0, 2):
    date = "2019-" + str(random.randrange(1, 13)) + "-" + str(random.randrange(1, 31))
    time = str(random.randrange(0, 24)) + ":" + str(random.randrange(0, 60)) + ":" + str(random.randrange(0, 60))
    
    f.write("Sexaul Harassment" + ", " + 
    str(date) + " " + str(time) + ", " + 
    str(random.uniform(37.5526404, 37.5544163)) + ", " + 
    str(random.uniform(126.9610906, 126.9656221)) + "\n")

# Robber
# Murder

# close file
f.close()