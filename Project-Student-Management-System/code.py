# --------------
# Code starts here
class_1 = [ 'Geoffrey Hinton' , 'Andrew Ng' , 'Sebastian Raschka' , 'Yoshua Bengio' ]
class_2 = [ 'Hilary Mason' , 'Carla Gentry', 'Corinna Cortes' ]
new_class=class_1+class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}
print(courses)
total=courses['Math']+courses['English']+courses['History']+courses['French']+courses['Science']
print("Total=",total)
percentage=(total/500)*100
print("Percentage=",percentage)
# Code ends here


# --------------
# Code starts here
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Rachka':65,'Yoshua Benjio':50,
'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
topper = max(mathematics,key = mathematics.get)
print ("Highest in maths:",topper)



# Code ends here  


# --------------
# Given string
topper = 'andrew ng'
print("topper:",topper)
first_name=(topper.split()[0])
print("first name:",first_name)
last_name=(topper.split()[1])
print("last name:",last_name)
# Code starts here
full_name=last_name+" "+first_name
print("full name:",full_name)
full_name.upper()
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


