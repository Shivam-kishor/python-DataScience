#create a contact list dict,where the user can search for a person
#name and if  the name exists,it display the phone number
#else,the user should be provided a choice to add the 
#phone number of that person
#also the user can choose to list all person and numbers


from pprint import pprint
dict={
    "candidate1":
    {    'name':"shivam",
    "occupation":"student",
    'age':13, 
    'phone_number':857479544   
    },

    'candidate2':
    {'name':'shubham',
    "occupation":"teacher",
    'age':14,
    'phone_number':955479544
    },

    "candidate3":
    {   'phone_number':85429544,
    'name':"monu",
    "occupation":"gymnastic"    
    }
    }

print("name",dict[i])

#for k,v in dict.items():
#    if dict==k:
#        print("value find")
#    else:
#        print("not found")

pprint(dict)  
