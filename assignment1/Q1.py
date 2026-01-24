#Message Counter(Immutable Parameter)
def count_message(msg,count=0):
    #Increment the counter
    count=count+1
    #print the message and counter
    print(f"Message: {msg} | Count: {count}")
    #return the final count
    return count

# Sample calls
count_message("heya")
count_message("Welcome")
count_message("Hii")
