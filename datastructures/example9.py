#keyworgs argument
#* list
# ** dictionary
def saveINFO(file='info.txt',**kwargs):
    with open(file,'a')as f:
        for k,v in kwargs.items():
            f.write(f'{k}->{v}\n')

saveINFO(mobile='motorolo',price=20000,expiry='2024',
features='kuch khaas nhi')