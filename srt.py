#!/usr/bin/python3

import sys
import random
import os
import socket

user=os.getlogin()
hostname=socket.gethostname()
srt_ip='10.0.10.2'
internal_port='4444'

if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--target', '-t', help="Override default profile")
	parser.add_argument('--mode', '-m', help='set mode to (client/server)')
	parser.add_argument('--port', '-p', help='set port')

	args = parser.parse_args()
	print()

	if(args.target):
		target=args.target
	if(args.mode):
		mode=args.mode
	if(args.port):
		port=args.port

print('--------------------\nDefined Variables\n--------------------')
try:
	target and mode and port
except:
	print('Must set TARGET IP and MODE and PORT\n')
	quit()
else:
	print('Target IP:	' + target)
	print('Mode:		' + mode)
	print('Port:		' + port)

print('\n--------------------\nStatic Variables (defined in python script)\n--------------------')
print('Internal Port:	' + internal_port)
print('SRT IP:			' + srt_ip)
print('Hostname:		' + hostname)








def buildSendEntrypoint(mode):
	print('\nRunning Build Send Entrypoint in ' + mode +' mode')
	import stat
	srt_entrypoint = open("hostfiles/entrypoint.sh", "wb")
	srt_entrypoint.write(bytes("#!/bin/bash\n", 'UTF-8'))
	srt_entrypoint.write(bytes("echo \'SRT LIVE TRANSMIT running.....\'\n", 'UTF-8'))
	if(mode == "client"):
		print('Client Mode is Active (trying to make connection)')
		srt_entrypoint.write(bytes("/home/srt/srt-live-transmit -s:5000 -r:5000 -v udp://0.0.0.0:" + internal_port + "/?mode=client srt://" + target + ":" + port, 'UTF-8'))
	if(mode == "server"):
		print('Server Mode is Active (listening for connection)')
		srt_entrypoint.write(bytes("/home/srt/srt-live-transmit -s:5000 -r:5000 -v srt://@:" + port + "/?mode=server " + "udp://10.0.10.4:" + internal_port, 'UTF-8'))	
	srt_entrypoint.close()

	os.chmod('hostfiles/entrypoint.sh', stat.S_IXOTH)




def initDocker():
	print('\nRunning Init Docker')
	import stat
	import subprocess
	srt_docker = open("start-srt.sh", "wb")
	srt_docker.write(bytes('sudo docker rm -f srt\n', 'UTF-8'))
	srt_docker.write(bytes('sudo docker run ', 'UTF-8'))
	srt_docker.write(bytes('-v /home/' + user + '/apps/srt/hostfiles/:/hostfiles ', 'UTF-8'))
	srt_docker.write(bytes('-p 4444:4444/udp  ', 'UTF-8'))
	srt_docker.write(bytes('--network=\"split\" ', 'UTF-8'))
	srt_docker.write(bytes('--ip=\"10.0.10.2\" ', 'UTF-8'))
	srt_docker.write(bytes('--name=\'srt\' ', 'UTF-8'))
	srt_docker.write(bytes('--privileged -i -t  ', 'UTF-8'))
	##srt_docker.write(bytes("--entrypoint=\"/bin/bash\" " ,'UTF-8'))
	srt_docker.write(bytes(' pmw1/srt\n\n ', 'UTF-8'))
	srt_docker.close()

	os.chmod("start-srt.sh", stat.S_IXOTH)
	proc = subprocess.Popen('sudo ./start-srt.sh', shell=True)
	print('\n')


buildSendEntrypoint(mode)
initDocker()



