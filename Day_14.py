class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        min_element = min(self.__elements)
        max_element = max(self.__elements)
        self.maximumDifference = abs(max_element - min_element)
    # End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)