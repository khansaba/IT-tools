print("Program for calculating area and perimeter of a Rectangle".center(78,"-"))
  

#Defining a class
class Rectangle:
     
     #Method for calculating area  
     def calculate_area(self):       
          self.height = float(input("Enter Height: "))
          self.width = float(input("Enter Width: "))
          area = self.height*self.width
          return (area)

     #Method for calculating perimeter
     def calculate_perimeter(self):  
          perimeter = 2*(self.height +
                          self.width)
          return (perimeter)


#Creating Instance

obj = Rectangle()
print ("Area of rectangle = %f" %(obj.calculate_area()))
print ("Perimeter of rectangle = %f"%(obj.calculate_perimeter()))
