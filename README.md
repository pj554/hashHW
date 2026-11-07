REFLECTION

I don't think any of my hash functions worked incredibly well. Attempt 1 resulted in a collision almost every time the function ran and most of the space was wasted.
Attempt 3 had no wasted space but a collision happened 13,000 times out of the 15,000 times the hash function ran. It also took by far the longest time to make at
around 3.4 seconds. For both attempts 1 and 3, I added up the ascii values of each char in the title/quote and made that the key. It seemed like a simple bad hash 
function. It was interesting to see how it worked differently with the linked list method vs. linear probing. The linked list table took much less time to create
but resulted in lots of wasted space. The linear probing table had no wasted space but took a very long time to make. Attempt 2 and 4 was with the "good" hash function.
I did a little research online and saw that multiplying the total by a prime number while adding up the ascii values would be more likely to give a unique key. Attempt 
2 used this with the linked list method and was a lot better than attempt 1. There were around 4,000 less collisions and the time was almost the same. Attempt 4 used
the same hash function with the linear probing method. The jump from attempt 3 to 4 was the biggest improvement out of all the attempts. There were about 4,000 less 
collisions and the time went from 3.4 seconds to 0.05 seconds. There was also no wasted space since it was the linear probing method. For attempt 5, I improved upon
attempt 2. I changed my hash table size from 15,000 to 75% of 15,000. I didn't need a slot for every movie because one slot could hold multiple movies with the linked
list. The time for attempt 5 was the same as 1 and 2 and there were 500 more collisions, but the wasted space was cut in half. For the linked list method, attempt 5 was
the best because it wasted the least amount of space while still being as fast as the other attempts. For linear probing, attempt 4 was the best because it was much
faster than attempt 3 since it had less collisions. Between attempt 4 and 5, determining the best depends on what you value. Attempt 4 has no wasted space, and attempt 
5 is faster. Attempt 4 is probably the best because memory is so expensive. But if you have unlimited memory, 5 beats 4 on speed.
