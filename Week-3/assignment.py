favouriteMusicians = []
#for musicians add favouriteMusicians
#copy to a new list called celebs
#sort the list
#pop out two celebs
#count the remaining celebs
favouriteMusicians.insert(0,'kahush')
favouriteMusicians.insert(1,'nyashinski')
favouriteMusicians.insert(2,'21 savage')
favouriteMusicians.insert(3,'quavo')
favouriteMusicians.insert(4,'nf')
favouriteMusicians.insert(5,'lowki')
favouriteMusicians.insert(6,'davaji')
favouriteMusicians.insert(7,'Don Toliver')
print(favouriteMusicians)
celebs =favouriteMusicians.copy()
celebs.sort()
print(celebs)
celebs.pop(-1)
print(celebs)
celebs.pop(-2)
print(celebs)
print(len(celebs))