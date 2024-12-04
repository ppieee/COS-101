number=[12,23,33,44,9,70]
okpa_list=['bambara nut' ,'maggie' , 'palmnut']
print(okpa_list)
okpa_list.append('fish')
print(okpa_list)
ingredient=input('enter ingredient ')
for item in okpa_list :
    if item== ingredient:
        print (ingredient+' is in the list')
    else: print(ingredient+ ' is not in list')

