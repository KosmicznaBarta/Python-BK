import random

class AlternatingIterator:
    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        result = self.value
        self.value = 1 - self.value
        return result
    
alt_iter = iter(AlternatingIterator())
for _ in range(10):
    print(next(alt_iter), end=" ")
print("\n")



class RandomDirectionIterator:
    def __iter__(self):
        return self
    
    def __next__(self):
        return random.choice(["N", "E", "S", "W"])
    
dir_iter = iter(RandomDirectionIterator())
for _ in range(10):
    print(next(dir_iter), end=" ")
print("\n")



class DayOfWeekIterator:
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        result = self.current
        self.current = (self.current + 1) % 7
        return result
    
day_iter = iter(DayOfWeekIterator())
for _ in range(14):
    print(next(day_iter), end=" ")