#dictionary=A changeable, unorderd collection of unique key:value pairs
#            Fast because they use hashing,allow us to access a value quickly

capitals={'USA':'Washington DC',
          'india':'New Delhi',
          'China':'Beijing',
          'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
#capitals.clear()

print(capitals['Germany'])
print(capitals.get('Germany'))
print(capitals.keys())#prints keys
print(capitals.values())#prints value assigned to keys
print(capitals.items())#print both keys and value assigned to them

for key,value in capitals.items():
    print(key,value)