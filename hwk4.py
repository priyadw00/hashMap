# Name:  Priya Dalal-Whelan
# Peers:  n/a
# References: 
# https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/ 
# https://www.youtube.com/watch?v=7J3GadLzydI 

import math
import time
import csv  
import random  
        # Used to read a .csv file.

### DO NOT EDIT ###
def new_array(size: int):
    """ Creates a new array of a given size.
    :param size: (int) the number of 0s you want in the array
    :return : (list) the array with zeros 
    >>> new_array(3)
    [0,0,0]
    """
    L = [0] * size
    return L

class HashNode:
    """Class to instantiate linked list node objects, with both a key and a value.
    >>> node = HashNode(7, "Matt Damon")
    >>> print(node)
    {key:7, value:Matt Damon}
    """
    
    def __init__(self, key:int, value:str):
        """ Constructor of new node with a key and value. Initially nodes do not have a next value.
        :param key: (int) the key that will be added to the node
        :param value: (str) the value that will be added to the node
        :return : (HashNode) a pointer to the object
        """
        self.key = key
        self.value = value
        self.next = None
        
    def __str__(self) -> str:
        """ Returns a string representation of the object.
        :return : (str) a string description of the HashNode object.
        """
        return "{key:" + str(self.key) + ", value:" + self.value + "}"     

### END OF DO NOT EDIT###

class SLL:
    """Class to instantiate a linked list made up of hashNode values 
    >>> list = SLL(hashNode)
    >>> addNode(hashNode)
    >>> print(list)
    {[ {key:7, value: matt damon}, {key: 8, value: charlie xx} ]}
    """

    def __init__(self, head:HashNode or None):
        """ Constructor of new node with a key and value. Initially nodes do not have a next value.
        :param head: (HashNode) the hashnode that will become the initial head of the list
        :return : (SLL) a pointer to the object
        """
        self.head = head


    def addNode(self, new:HashNode):
        """adds a new node to the head of the list. 

        Args:
            new (HashNode):  new hashode to be added
        """
        new.next = self.head
        self.head = new 
    
    def __str__(self)-> str:
        """ Returns a string representation of the object. 

        :return : (str) a string description of the SLL object.
        """

        string = "[ "
        curr = self.head
        while curr != None:
           string += "{key:" + str(curr.key) + ", value:" + curr.value + "} "
           curr = curr.next
        return string + "]"
    



class HashTable:

    """Class to instantiate and use a hashing function to store data 
    >>> hash_table = HashTable(10, 0)
    >>> print(hashtable)
    Hashmap: {[ {key:332, value:Don Cheadle}}
    >>> print(list) 
    {[ {key:7, value: matt damon}, {key: 8, value: charlie xx} ]}
    >>> hashfunc(7, 1) 
    0
    >>> hash_table.insert(7, "matt damon")
    True 
    >>> hash_table.getValue(7)
    "Matt Damon"
    >>> hash_table.remove(7)
    True 
    >>> hash_table.isOverLoadFactor()
    False 
    >>> hash_table.reHash()
    True 
    """
    
    def __init__(self, size:int, hash_choice:int):
        """Contructs new hash table with specified size and hash function. 

        Args:
            size (int): initial size of array containing hash values
            hash_choice (int): which of the five hash functions should be used 
        """
        self.size = size
        self.arr = [None] * size 
        #self.arr:list [SLL]  
        self.hash_choice = hash_choice   
        self.listcounter = 0               # Which hash function you will use.
        pass
    
    def __str__(self) -> str:
        """Returns a string representation of the hashmap 
        :return : (str) a string description of the SLL object.
        """
        string = "Hashmap: {"

        for item in self.arr:
            if item!= None :
                string += (str(item) + "\n")
            else: 
                string += "- \n"
        return string + "}"

        
    def hashFunc(self, key:int) -> int | None:
        """Takes in key and returns hashed key. The function chooses which of the five hash functions to use 
        by checking has_choice variable. 

        Args:
            key (int): unique id associated with the data 

        Returns:
            int | None: Hashkey which determines where the data will be stored, 
            or None if something has gone wrong 
        """

        if type(key) != int:
            return None

        if self.hash_choice == 0:
            return hash(key) % self.size    # Embedded Python hash function.
        
        elif self.hash_choice == 1:
            return 0    #Everything is stored in a single linked list.
        
        # just plain modulo self  
        elif self.hash_choice == 2:
            k = key 
            return  k % self.size 
            pass #TODO Implement your has functions here.
        
        # divide by a prime 
        elif self.hash_choice == 3:
            k = key // 11
            return k % self.size  
    
        # quadratic formula 
        elif self.hash_choice == 4:
            a = key % 10 
            b = key % 100 
            c = key % 1000 
            k = round(-b + math.sqrt(4*a*c)/2*a)
            return k % self.size 
        
        return None 
    
    def insert(self, key:int, val:str) -> bool:
        """ Inserts new entry into the hashtable by first calling hashfunc on the key, 
        then creating a SLL node and storing it in the appropiate place. Returns whether 
        or not the operation was sucessful. 

        Args:
            key (int): unique integer identifying the entry 
            val (str): information associated with entry 

        Returns:
            bool: Returns true if the operation was sucessful and false
              f the item was unable to be inserted (such as if there 
              was already an entry with that key)
        """

        hashvalue = self.hashFunc(key)
        #print("hashvalue is:", hashvalue)
        if hashvalue  == None: 
            #print("hash error")
            return False
        else:
            if self.arr[hashvalue] == None: 
                #print("slot currently empty")
                #create node 

                n = HashNode(key, val)
                # create list w/ head 
                l = SLL(n)
                # add list to array 
                self.arr[hashvalue] = l 

                #increment list counter
                self.listcounter += 1  

                return True  
            else: 
                #print("slot has list already")
                #print(str(self.arr[hashvalue]))

                l = self.arr[hashvalue]
                curr = l.head # type: ignore
                while curr!= None: 
                    #key or value ... key is unique right? b/c key contains the whole int not the hash value?
                    if curr.key == key: 
                        #print("element already exists ")
                        return False
                    else:
                        curr = curr.next

                #print("element not found ")
                n = HashNode(key, val)
                l.addNode(n)

                return True 

    def getValue(self, key:int) -> str | None: # type: ignore

        """Takes in key and returns value associated with it from the hash table, 
        or None if there is no entry matching that key
        
        Args: 
            int: key of item to look up 
        Returns:
            str: string value associated with given key   
        """


        hashvalue = self.hashFunc(key)
        #print("hashvalue is:", hashvalue)
        if self.arr[hashvalue] == None: 
            #print('returning None')
            return None 
        else: 
            l= self.arr[hashvalue]
            #print(l)
            curr = l.head 
            while curr != None:
                #print(curr)
                if curr.key == key:
                    return curr.value
                else: 
                    curr = curr.next 

#1159
    def remove(self, key:int) -> bool:
        """Takes in key and removes entry from the hashtable. Returns true if the operation 
        was sucessful and false if it was unsucessful (for example if the entry was not in the table)

        Args:
            key (int): key 

        Returns:
            bool:  weheter or not the operation was sucessful. 
        """

        hashvalue = self.hashFunc(key)
        
        if self.arr[hashvalue] == None: 
            #print("No entry found with key", key)
            return False 
        else: 
            l = self.arr[hashvalue] 
            #print("l: \n")
            #print(l)
            curr = l.head 
            #if value is at head of the list, delete by making .next the head 
            if curr.key == key: 
                l.head = curr.next 
                return True 
            
            #the and is fine right? bc next was already chcked at the last loop  
            while curr != None and curr.next!= None: 
                #print("curr is:", str(curr))
                # if curr.next.key is key, then curr.next should be deleted and curr.next.next should become curr.next
                if (curr.next.key == key):
                    newNext = curr.next.next 
                    curr.next = newNext 
                    return True
                else: 
                    curr = curr.next 
            return False 
                
            

        return False
    
    def isOverLoadFactor(self) -> bool:

        """Checks wheter the hastable is more then 70 percent full 

        Returns:
            boolean: True if load factor > .7, otherwise false 
        """
        #print(self.listcounter)
        loadFactor = self.listcounter/ self.size
        #print(loadFactor)
        if loadFactor > .7: 
            return True
        else: 
            return False  
    
    def reHash(self) -> bool:

        """ Doubles the size of the hash array and rehashes all entries to fit in the new size. 
        Returns whether or not the operation was sucessful (if it fails reverts to old hash)

        Returns:
            boolean: True if operation was sucesfful, false if not 
        """

        self.size = self.size *2 

        old_arr = self.arr
        #print("old arr:", old_arr)

        self.arr = [None] * self.size 
        #reset list counter 
         
        self.listcounter = 0 

        for list in old_arr:
            if list == None: 
                pass 
            else: 
                curr = list.head 
                while curr != None: 
                    suc = self.insert(curr.key, curr.value)
                    if suc == False: 
                        self.arr = old_arr 
                        return False 

                    else: 
                        curr = curr.next 
        
        # if it fails revert to original and then return false 

        return True 
                    

            
                    
def main():
    # You should update these three values as you test your implementation.

    hash_func_to_test = 0
    initial_bucket_size = 10 
    initial_num_to_add = 100

    hash_table = HashTable(initial_bucket_size, hash_func_to_test)
    with open('hwk4-people.csv') as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = csv_reader.__next__()
        for row_iterator in range(initial_num_to_add):
            row = csv_reader.__next__()
            hash_table.insert(int(row[0]),row[1])
        print("Hash Map Initialized")
                
        option = ""
        while option != "QUIT":
            option = input("Select an option (ADD, GET, REMOVE, PRINT, CHECK, REHASH, QUIT): ").upper()        

            if option == "ADD":
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
                print("Added - Key:", int(row[0]), "\tValue:", row[1])
            elif option == "GET":
                key = int(input("Which # would you like to get the value of? "))
                val = hash_table.getValue(key)
                if val is None:
                    print("Error,", key, "not found.")
                else:
                    print(val)
            elif option == "REMOVE":
                key = int(input("Which # would you like to remove? "))
                suc = hash_table.remove(key)
                if suc:
                    print(key, "was removed.")
                else:
                    print("Error,", key, "was not removed.")                    
            elif option == "PRINT":
                print(hash_table)   # calls the __str__ method.  
            elif option == "CHECK":
                isOver = hash_table.isOverLoadFactor()
                if isOver:
                    print("Your load factor is over 0.7, it's time to rehash.")
                else:
                    print("Load factor is ok.")
            elif option == "REHASH":
                suc = hash_table.reHash()
                if suc:
                    print("Rehash was successful.")
                else:
                    print("ERROR: rehash failed.")
            elif option == "QUIT" or option == "Q":
                break 
            elif option == "ADD REPEAT": 
                print(hash_table.insert(int('0000134'), "Robert De Niro"))
            else:
                print("Error: invalid input, please try again.")
                
        print("Goodbye!")
            

def profilerMain():    
    # You should update these three values as you profile your implementation.

    # for expirement 3: generate values outside of the loop so that each hasFunc is being tested on the 
    # same values 
    keys = new_array(20)
    keys = [134, 197,8,243,31,7,658, 358,1627,22,6,158,72,
            12, 60, 138,49,30]

    for i in range(5): 
 
        hash_func_to_test = i 
        initial_bucket_size = 600 
        initial_num_to_add = 999

        # Get start Time.
     

        #### Start of code you want to profile ####
    
    ###experiment one and two (changed intial bucket size between expirments )

        hash_table = HashTable(initial_bucket_size, hash_func_to_test)
        with open('hwk4-people.csv') as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = csv_reader.__next__()
            #rehashes = 0 
            for row_iterator in range(initial_num_to_add):
                row = csv_reader.__next__()
                hash_table.insert(int(row[0]),row[1])
                isOver =  hash_table.isOverLoadFactor()
                while isOver:
                    hash_table.reHash()
                    #rehashes += 1
                    isOver = hash_table.isOverLoadFactor()


        ### experiment 3 

        start_time_create =  time.time()  

        for key in keys:
            hash_table.getValue(key)
            

        #### End of code you want to profile ####
        
        end_time_create = time.time()      # Get end Time. 
        calc = end_time_create - start_time_create  
        print("Hash Map w/ function:", hash_func_to_test, "\tTime:", calc, "seconds.")
            
    

if __name__ == "__main__":
    # Swap these options to profile or test your code.
    profilerMain()     
    #main()
    
