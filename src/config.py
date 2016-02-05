
class Config(object):
  Log_filename = 'logs/comchast.log'
  
  #TODO 
  Twitter_key = ''
  Twitter_secret = '' 
  Twitter_access_key = ''
  Twitter_access_secret = ''
  #TODO - End
  
  Comcast_DL_Threshold = 105 * .5
  Comcast_UPL_Threshold = 20 * .5

  Tweet_Templates = [
    "@comcastcares Watch me being whipped by slow speeds : Actual %dmbps, Expected 105mbps - https://youtu.be/vjW8wmF5VWc",
    "@comcastcares wants me to take the banana.. %mbps instead of 105 - https://youtu.be/6n5uhr85Zmo",
    "@comcastcares please !! %dmbps when I pay for 105?",
    "How come I am getting only %dmbps download when I am paying for 105? @comcastcares",
    "Not Cool @comcastcares ! I paid for 105 mbps not %d!",
    "Oh lordy! %d mbps is NOT 105 @comcastcares", 
    "Martha! Martha! Martha! getting %d instead of 105mbps @comcastcares",
    "@comcastcares can you get your numbers in order? getting %d instead of 105mbps smh",
    "Looks like 105mbps is a dream not coming thru, reality is %dmbps - @comcastcares",
    "@comcastcares - why trolololo me with %dmpbs instead of the 105 I am paying for ?",
    "@comcastcares - 105mbps looks high in the sky of the %dmbps land!",
    "@comcastcares - Speeds look pale at %dmbps compared to the 105mbps I am paying for !",
    "@comcastcares - nightflight to venus would be a very, very long trip at %dmbps instead of the 105mbps I am billed for! - https://youtu.be/P-7-ENyE5yU"
 ]
