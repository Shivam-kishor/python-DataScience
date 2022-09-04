#import imp
from pprint import pprint#use to preety look from new line dictionary 
movies={}
#adding a si gle value
movies["sholay"]='2 frnds jai and veeru'
movies['inception']="no summary"
print (movies)


#adding multiple values
movies.update(
    ironman=" iron man tha",
    hulk='having not she hulk',
    power_ranger='having ninja techniques')


movies.pop('sholay')

#update
#movies['inception']="dream recursion logic"

#update
movies['hulk']+="  and fight with joker"

#print(movies)
pprint(movies)