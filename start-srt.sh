sudo docker rm -f srt
sudo docker run -v /home/kevin/apps/srt/hostfiles/:/hostfiles -p 3000:3000/udp -p 4444:4444/udp  --network="split" --ip="10.0.10.2" --name='srt' --privileged -i -t  --entrypoint="/bin/bash"  pmw1/srt

 