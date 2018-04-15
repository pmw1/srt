#!/bin/bash
echo 'SRT LIVE TRANSMIT running.....'
/home/srt/srt-live-transmit -s:5000 -r:5000 -v srt://@:3000/?mode=server udp://10.0.10.4:4444