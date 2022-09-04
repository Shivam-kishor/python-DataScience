#4 sep/2022
movies={
'm1':'sholay',
'm2':'looper',
'm3':'spider'
}
print(movies)   
print(movies.keys())   
print(movies.values())

print("----------------------------------------------------------------------------")

#travesring  1 stway give just key
print('style 1')
for name in movies:
    print(name)

print("----------------------------------------------------------------------------")
#travesring  2nd way give just value
print('style 2')
for key in movies:
    print(movies[key])

print("----------------------------------------------------------------------------")

#travesing dictionary 3rd way give keys and value
print('style 3\n')
for key in movies:
        print(key,movies[key]) 

print("----------------------------------------------------------------------------")
#travesing dictionary 4th way give keys and value

print('style 4')
for k,v in movies.items():
    print(k,v)