
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
    "Haha, friends ! Bragging of 105mbps connection to the internetz. Who's laughing now says @comcast. %dmbps. @comcastcares",
    "The @comcastcares so much it does not want me to dangerously surf at the 105mbps speeds I am billed for. We will stick to %dmbps for now",
    "Today my car decided to run at a maximum speed of %dmph. The manufacturer's max spec is 105mph. The manufacturer is @comcast. @comcastcares", 
    "Hey @comcastcares @comcast, why don't you add more fees? the recently imposed fees did not help with my speeds, getting %dmbps while paying for 105",
    "Ayo @comcastcares ! Woot Woot ! Slow speed keep right. %dmbps != 105mbps I pay for - https://youtu.be/ENWeBtvAU90?t=140",
    "Ayo @comcastcares ! Woot Woot ! debug assertion failed : Expected 105mbps, Actual %dmbps. Nerd life.",
    "Hey @comcastcares Watch me being whipped by slow speeds: Actual %dmbps, Billed for 105mbps - https://youtu.be/vjW8wmF5VWc",
    "The @comcastcares wants me to take the banana.. %mbps instead of 105 - https://youtu.be/6n5uhr85Zmo",
    "Sir/Madam @comcastcares please !! %dmbps when I pay for 105?",
    "How come I am getting only %dmbps download when I am paying for 105? @comcastcares",
    "Not Cool @comcastcares ! I paid for 105 mbps not %d!",
    "Oh lordy! %d mbps is NOT 105 @comcastcares", 
    "Martha! Martha! Martha! getting %d instead of 105mbps @comcastcares",
    "Hey @comcastcares can you get your numbers in order? getting %d instead of 105mbps smh",
    "Looks like 105mbps is a dream not coming thru, reality is %dmbps - @comcastcares",
    "Why @comcastcares trolololo me with %dmpbs instead of the 105 I am paying for ?",
    "Hey @comcastcares - 105mbps looks high in the sky of the %dmbps land!",
    "Hey @comcastcares - Speeds look pale at %dmbps compared to the 105mbps I am paying for !",
    "Hey @comcastcares - nightflight to venus would be a very, very long trip at %dmbps instead of the 105mbps I am billed for! - https://youtu.be/P-7-ENyE5yU"
 ]
