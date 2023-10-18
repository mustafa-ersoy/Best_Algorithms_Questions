#this is the solution of Question 380 on Leetcode
#O(1) time complexity for each insert, remove, getRandom operations, O(n) space complexity if n elements are inserted.


#we need to design a data structure where each operation takes O(1) time.
#if we use a linked list or a set to store values, getRandom will not be O(1).
#one solution is storing values in an array and keeping value indexes in a hashmap
#deleting from middle in array is O(n) but deleting from end is O(1) so before we delete a value,
#we can just swap it with last element and delete (pop) last element.


class RandomizedSet:
    def __init__(self):
        #initializing data structure with an array and hashmap
        self.arr = []
        self.hash = {}

    def insert(self, val: int) -> bool:
        #we insert at the end of array and set its index value in hashmap
        if val in self.hash: return False
        self.arr.append(val)
        self.hash[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        #when removing, we get the index of value and swap this value with the last value in array and pop that value.
        if val not in self.hash: return False
        ind = self.hash[val]
        if ind == len(self.arr)-1:
            self.arr.pop()
            del self.hash[val]
            return True
        self.arr[ind], self.arr[-1] = self.arr[-1], self.arr[ind]
        self.arr.pop()
        del self.hash[val]
        self.hash[self.arr[ind]] = ind
        return True

    def getRandom(self) -> int:
        #we return a random value from array
        return random.choice(self.arr)