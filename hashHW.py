# Name: Phillip Therriault
# Date: 11/04/2026
# Description: Creates a hash table for a given data set of movies.

import time

#to do: good LL, bad LP, good LP, final

def create_movie(title, genre, date, director, revenue, rating, minutes, company, quote):
    movie = {
        "title":title,
        "genre":genre,
        "date":date,
        "director":director,
        "revenue":revenue,
        "rating":rating,
        "minutes":minutes,
        "company":company,
        "quote":quote
    }
    return movie

# add up ascii values for each char is title/quote. return int for hash table
def hashFunction(titlequote):
    hashValue = 0
    for i in titlequote:
        hashValue += ord(i)
    return hashValue
    
# take hash table and add up every empty list to get number of wasted slots
def waste_stat_track(table):
    wasted_slots = 0
    for i in range(len(table)):
        if table[i] == []:
            wasted_slots+=1
    return wasted_slots      

def main():

    
    hashTable = [] # empty hash table to start

    table_size = 15000 # data set has 15,000 entries, so size of table is 15,000

    collisions = 0

    # create hash table with 15,000 empty slots to add to it correctly and to keep track of empty slots
    for i in range(table_size):
        hashTable.append([])
   
    file = open("MOCK_DATA.csv","r", encoding="utf-8") # utf-8 bit is help from chatgpt. I asked ai for help because I didn't understand why I was getting an error trying to read in the data
    line = file.readline() #skip header line
    line = file.readline()

    # add each movie to hash table using hash function
    start_time = time.perf_counter()
    while line != "":
        line = line.split(",")
       
        movie = create_movie(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8])

        key = hashFunction(movie["quote"])
        
        key = key % table_size
        
        line = file.readline()

        if len(hashTable[key]) > 1:
            collisions += 1

        hashTable[key] = movie
    end_time = time.perf_counter()

    file.close()
    
    print("\nHash table type: Movie Quote\n")
    print("Statistics:")
    print(f"Wasted slots: {waste_stat_track(hashTable)}")
    print(f"Collisions: {collisions}")
    print(f"Time taken to construct hash table: {end_time - start_time} \n")
    print("Optimization attempt: Linked list method with poor hash function\n")
   
main()