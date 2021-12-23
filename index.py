from playsound import playsound
import os

#warna
class bcolors:
	HEADER = '\033[95m'
	hi = '\033[94m'
	hai = '\033[93m'
	woi = '\033[92m'
	yo = '\033[91m'
	bro = '\033[0m'
	gan = '\033[1m'
	coy = '\033[2m'
#function
def menu():
  os.system("clear")
  print(bcolors.yo + "MP3 player by SenjaDev\ngit : https://github.com/phantom43\n")
  print(bcolors.hi + "option : " + bcolors.bro + "1.play | exit\n isi folder:" )
  print(bcolors.woi)
  os.system("ls")
def main():
 anjay = input("/play/~# ")
 playsound(anjay)
#main
menu()
senja = input("->" )
if senja == '1':
 main()
elif senja == "play":
	main()
elif senja == "exit":
	os.system("exit")
elif senja == "":
	os.system("python3 index.py")