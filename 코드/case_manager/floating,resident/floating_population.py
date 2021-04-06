import codecs

f = codecs.open("floating_population_data.csv", 'w', "utf-8")

FLOATING_POPULATION = [
    129810,	126650,	124430,	122740,	122220,	127230,	147650,	218540,	354470,	409980,	427850,	434940,	
    440640,	445600,	444000,	435440,	422640,	391220,	294780,	235240,	200210,	173050,	149930,	135880]

POPULATION_RATIO = [
    20, 54, 30, 40, 48, 50, 17, 80, 150, 183, 149, 97, 113, 121, 85]

LOCATION_LABEL = [
    "소공동", "회현동", "명동", "필동", "장충동", "광희동", "을지로동", 
    "신당동", "다산동", "약수동", "청구동", "신당5동", "동화동", "황학동", "중림동"]

SUM_OF_POPULATION_RATIO = 1237

f.write(u'\ufeff')
f.write("Time" + ", " + "Location" + ", " + "Floating Population" + "\n")

for i in range(0, 24):
    for j in range(0, 15):
        population = (FLOATING_POPULATION[i]/SUM_OF_POPULATION_RATIO)*POPULATION_RATIO[j]
        f.write(str(i) + ", " + str(LOCATION_LABEL[j]) + ", " + str(round(population)) + "\n")

print("create floating_population_data.csv\n")

f.close()