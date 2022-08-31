from pstats import Stats
from readline import append_history_file
import statistics  as stat

a=[]    
for i in range (1,11):
    val=int( input (f'{i}'))
    a.append_history_file(val)
    
for i in a:
    print(i,end=" ")



print("minimum value",min(a))
print("max value",max(a))
print("total value",sum(a))
print("avg value",Stat.mean(a))
print("minimum value",stat.median(a))