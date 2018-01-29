import RPi.GPIO as GPIO
import time
import subprocess, signal

reckey = 17
rstkey = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(reckey, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rstkey, GPIO.IN, pull_up_down=GPIO.PUD_UP)
recording_state = False
shutdown_state = False

while True:
    GPIO17_instate = GPIO.input(reckey)
    if GPIO17_instate == False:
        print("[17]: pinoi 17 acionado")
        if recording_state == False:
            try:
          #      process = subprocess.Popen('/home/pi/scripts/gravar.sh', shell=True, stdout=subprocess.PIPE)
                recording_state = True
            except:
                print("[17]: erro inesperado:", sys.exc_info()[0])
            else:
                print('[17]: gravando')
        else:
#            process.send_signal(2)
#            process.wait()
#            print process.returncode
            print('[17]: parando de gravar')
            recording_state = False
    GPIO18_instate = GPIO.input(rstkey)
    if GPIO18_instate == True:
        if shutdown_state == False:
            try:
                process = subprocess.Popen('sudo shutdown -h now', shell=True, stdout=subprocess.PIPE)
                print("[18]: pinoi 18 acionado")
                shutdown_state = True
            except:
                print("[18]: erro inesperado:", sys.exc_info()[0])
            else:
                print('[18]: shutdown')
    time.sleep(0.2)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
