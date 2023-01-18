#class Car:
   #def __init__(self, seats):
     #We can also call these attributes instance attributes
      #self.seats = seats
    #def enter_race_mode(self): 
      #self.seats = 2 
#My_car = Car(5)
#my_car.enter_race_mode()

#print(My_car.seats)



#class IceCream:
  #Class attribute
  #ice_toppings ="choco chips"
  
  #Instance attribute
  #def __init__(self,icename,color,price):
    #self.ice_name=icename
    #self.ice_color = color
    #self.ice_price =price 

    #instance of a class or object

#my_cream=IceCream("Vanila", "yello",10)
#my_cream2= IceCream("Strawbeery","red",20)

#print(my_cream.ice_price)
#print(IceCream.ice_toppings)
#print(IceCream.ice_price)
#print(my_cream.ice_name, my_cream.ice_toppings)   
class Student:
   mentor = "Sam"
   def __init__(self, first_name, last_name, age):
       self.first_name = first_name
       self.last_name = last_name
       self.age = age
     
   def enroll_to_course(self, course_name="general"): #We can supply default name and an intial argument to be used if user doesn't enter anything.
       self.course_name = course_name
     
   def remove_from_course(self):
       self.course_name = "None"
     
john = Student("John", "Smith", 19)
mary = Student("Mary", "Williams", 20)
john.enroll_to_course("Science")
mary.enroll_to_course("Commerce")

print("Mary's mentor is : ", mary.mentor)
print("John\'s last name:", john.last_name)
print ("Mary's age is: ",  mary.age)
print ("John is enrolled to the course: ", john.course_name)
john.remove_from_course()
mary.enroll_to_course()
print ("John is enrolled to the course: ", john.course_name)
print ("Mary is enrolled to the course: ", mary.course_name)