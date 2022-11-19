#nested dic
from calendar import day_abbr
from pprint import pprint
emps={
    'chandu':
    {'name':'chandu sharma',
    "salary":15000,
    "age":34,
    "desgination":'foreman'
},
'rohit':
{'name':'rohit',
"salary":25000,
'age':24,
'desgination':'google ceo'},

"anonymous":
{'name':'unkmnown',
"salary":95000,
'age':17,
'occupation':"hacker"
}

}


print(emps)

print("desgination",emps['rohit']['desgination'])




#loop 
for key,data in emps.items():
    print(key," ⬇️")
    for k,v in data.items():
        print(k,v)
        print('--'*10)