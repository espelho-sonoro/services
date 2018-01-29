from twython import Twython, TwythonError



d = {}
with open("twitter_keys") as f:
    for line in f:
       (key, val) = line.split()
       d[key] = val
print d



# Requires Authentication as of Twitter API v1.1
twitter = Twython(d['APP_KEY'], d['APP_SECRET'], d['OAUTH_TOKEN'], d['OAUTH_TOKEN_SECRET'])

try:
    twitter.update_status(status='Ola pessoal')
except TwythonError as e:
    print e

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
