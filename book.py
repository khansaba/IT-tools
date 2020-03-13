#Program to calculate total price of a book based on taken inputs


class Book:
    
    #Defining class Book
    #Accepting input from user
    def accept_input(self):                   
        self.name = str(input("Enter name of Book: "))
        self.author = str(input("Enter author of Book: "))
        self.price = float(input("Enter price of Book: "))
        self.n_copies = int(input("Enter no. of copies to purchase of Book: "))

    #Calculating total price
    def total_price(self):                    
        t = self.price*self.n_copies
        print("Total Price: ", t)

    #Display all the details
    def purchase_details(self):
        print("Purcashe Details".center(70,"-"))
        print("Name of Book : ", self.name)
        print("Author of Book : ", self.author)
        print("Price of Book : ", self.price)
        print("Number of copies : ", self.n_copies)


        
#Creating Instance
obj=Book()

obj.accept_input()
obj.purchase_details()
obj.total_price()
