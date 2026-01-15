#Avoid default mutable argument bug
def add_item(item, cart=None):
    #Create a new list if items is None
        if cart is None:
            cart = []#This function avoids using a mutable object as a default parameter.
        cart.append(item)#A new list is creted for every function call.
        return cart


# Multiple calls to prove it works correctly
print(add_item("Apple"))
print(add_item("Banana"))
print(add_item("Orange"))
