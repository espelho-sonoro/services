from twython import Twython, TwythonError
from time import sleep
from picamera import PiCamera
from datetime import datetime, date, time, timedelta

delay = 1800  #delay in seconds

d = {}
with open("/home/pi/services/twitter_keys") as f:
    for line in f:
       (key, val) = line.split()
       d[key] = val

twitter = Twython(d['APP_KEY'], d['APP_SECRET'], d['OAUTH_TOKEN'], d['OAUTH_TOKEN_SECRET'])


camera = PiCamera()
camera.resolution = (1920,1080)
camera.start_preview()
sleep(10)
for filename in camera.capture_continuous('/home/pi/services/img/img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    ts = datetime.now()
    message = '[' + str(ts.strftime("%Y-%m-%d %H:%M"))  + '] Espelho Sonoro transmitindo ao vivo! Confira em http://www.espelhosonoro.com/'
    with open(filename, 'rb') as photo:
        try:
#            twitter.update_status_with_media(status=message, media=photo)
            response = twitter.upload_media(media=photo)
            twitter.update_status(status=message, media_ids=[response['media_id']])
        except TwythonError as e:
            print e
    sleep(delay)
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
