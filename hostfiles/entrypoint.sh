#!/bin/bash
echo 'SRT LIVE TRANSMIT running.....'
/home/srt/srt-live-transmit -s:5000 -r:5000 -v udp://0.0.0.0:4444/?mode=client srt://72.0.154.251:3000