class TimeMap:

    def __init__(self):
        self.store = {} #key = string, val = [list [value , t]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = [] #init list
        self.store[key].append([value, timestamp])  #append list into list

    def get(self, key: str, timestamp: int) -> str:
        result = "" #if key doesnt exist, return empty string
        #this will grab the list containing all the lists
        values = self.store.get(key, []) #check if the key exists otherwise return empty list
        l , r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            #because we are not returning only if we find the target
            #we will always return the value that exists even if the time stamp doesnt
            #therefore when looking through the list of lists,
            #the value < timestamp will be the result since the value exists
            #cant be value > timestamp cause what if no timestamp greater
            #if search timestamp < values then return ""
            if values[m][1] <= timestamp: 
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result
        
