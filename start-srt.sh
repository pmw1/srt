sudo docker rm -f srt
sudo docker run -v /home/kevin/apps/srt/hostfiles/:/hostfiles -p 4444:4444/udp  --network="split" --ip="10.0.10.2" --name='srt' --privileged -i -t   pmw1/srt

 