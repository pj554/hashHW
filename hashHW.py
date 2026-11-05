class hash_table():
    def __init__(self, table, collisions):
        self.table = table
        self.collisions = collisions

    def wasted_space(self, table):
        pass 

def hashFunction_1(movie, max_index):
    index = 0
    for i in movie:
        index += ord(i)
    if index > max_index:
        index = max_index
    return index

def waste_stat_track(table):
    wasted_slots = 0
    pass
        

def main():
    file = open("MOCK_DATA.csv","r", encoding="utf-8") # encoding = utf-8 bit was help from chatgpt. I kept getting an error trying to read in without it, so i asked ai for help. I've never seen anything like that before.
    data = file.readlines()
    data_count = len(data) - 1 # -1 because header line doesn't count
    file.close()



    hashTable = hash_table([], 0)

    # create empty hash table for linked list method
    for i in range(data_count):
        hashTable.table.append([])

    file = open("MOCK_DATA.csv","r", encoding="utf-8")
    line = file.readline() #skip header line
    line = file.readline()
    counter = 0
    while line != "":
        hashTable.table[hashFunction_1(line.split(",")[0],14999)].append(line.split(",")[0])
        line = file.readline()
     
    file.close()
    print("done")
    


    
main()