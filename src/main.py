from speedtest_cli import speedtest
from config import Config
import twitter
import commands
import random
import logging

def tweet(msg):
  api = twitter.Api(consumer_key=Config.Twitter_key,
                  consumer_secret=Config.Twitter_secret,
                  access_token_key=Config.Twitter_access_key,
                  access_token_secret=Config.Twitter_access_secret)
  return api.PostUpdate(msg)


def main():
  logging.basicConfig(format='%(asctime)s %(message)s', 
                      filename=Config.Log_filename, level=logging.INFO)

  ret = commands.getstatusoutput('speedtest --simple')
  logging.getLogger('comchast').info(ret[1].replace('\n', ' '))
  parts = ret[1].split('\n') 
  ping = parts[0]
  down = parts[1]
  up = parts[2]
  down_n = float(down.split(' ')[1])
  up_n= float(up.split(' ')[1])

  
  if down_n < Config.Comcast_DL_Threshold:
    modulus = len(Config.Tweet_Templates)
    template = Config.Tweet_Templates[int(random.random() * 10) % modulus]
    tweet(template % down_n)
  

if __name__ == '__main__':
  main()
