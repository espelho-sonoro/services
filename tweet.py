from twython import Twython, TwythonError
from time import sleep
from picamera import PiCamera
from datetime import datetime, timedelta


d = {}
with open("twitter_keys") as f:
    for line in f:
       (key, val) = line.split()
       d[key] = val
print d

twitter = Twython(d['APP_KEY'], d['APP_SECRET'], d['OAUTH_TOKEN'], d['OAUTH_TOKEN_SECRET'])

def wait():
    # Calculate the delay to the start of the next hour
    next_hour = (datetime.now() + timedelta(minutes=1)).replace(
       second=0, microsecond=0)
    delay = (next_hour - datetime.now()).seconds
    sleep(delay)

camera = PiCamera()
camera.start_preview()
wait()
for filename in camera.capture_continuous('img/img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    try:
        twitter.update_status_with_media(status=message, media=photo)
    except TwythonError as e:
        print e
    with open('/home/pi/Downloads/image.jpg', 'rb') as photo:
    wait()
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
