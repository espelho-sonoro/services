#!/bin/sh

#sudo usb_modeswitch -c /etc/usb_modeswitch.conf
#sleep 1s
#sudo wvdial &
#sed '/localDumpFile/ s/$/ $filename/' /home/pi/services/darkice.cfg.bak
sed "/localDumpFile/ s/$/$(date '+%Y_%m_%d__%H_%M_%S').ogg/" /home/pi/services/template.cfg | tee /home/pi/services/darkice.cfg

#sed -i -e '/localDumpFile/ =/ s/= .*/= \1$filename/' /home/pi/services/darkice.cfg.bak
darkice -c /home/pi/darkice.cfg
