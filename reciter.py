from playsound import playsound
import os



current_PATH = os.getcwd()
count = 1
r = list()
data = dict()






f = open("surahname.txt", "r")
print(f.read())

data_Raw = open("data.txt","r")

while(True):
	line = data_Raw.readline()
	if not line:
		break
	r += line.strip().split(",")

data_Raw.close


choice = int(input("Enter the surah:"))

num = choice
choice -= 1
max = r[choice + num]


MaxAyat = int(max)
surahNumber = num
current_ayyah = 1

if(surahNumber < 9):
    SS = "/Shuraim/00"+str(surahNumber)
    TT = "/Urdu/00"+str(surahNumber)

elif(surahNumber > 10 and surahNumber < 100):
    SS = "/Shuraim/0"+str(surahNumber)
    TT = "/Urdu/0"+str(surahNumber)

else:
    SS = "/Shuraim/"+str(surahNumber)
    TT = "/Urdu/"+str(surahNumber)



while(count <= int(max)):
    if(current_ayyah < 10):
        S = SS+"00{0}.mp3".format(count)
        T = TT+"00{0}.mp3".format(count)
        playsound(current_PATH + S)
        playsound(current_PATH + T)
        count += 1
        current_ayyah += 1
    elif(current_ayyah > 9 and current_ayyah < 100):
        S = SS+"0{0}.mp3".format(count)
        T = TT+"0{0}.mp3".format(count)
        playsound(current_PATH + S)
        playsound(current_PATH + T)
        count += 1
        current_ayyah += 1
    elif(current_ayyah > 99):
        S = SS+"{0}.mp3".format(count)
        T = TT+"{0}.mp3".format(count)
        playsound(current_PATH + S)
        playsound(current_PATH + T)
        count += 1
        current_ayyah += 1
