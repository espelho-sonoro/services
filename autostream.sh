#!/bin/sh

sudo usb_modeswitch -c /etc/usb_modeswitch.conf
sleep 1s
sudo wvdial &
darkice -c /home/pi/darkice.cfg
