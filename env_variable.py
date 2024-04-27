import os

key = os.environ.get('SPEECH_KEY')
region = os.environ.get('SPEECH_REGION')

print("key {0} and region {1}".format(key, region))