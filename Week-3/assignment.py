favouriteMusicians = []
celebs =['kahush','nyashinski','21 savage','quavo','lowki','davaji','Don Toliver']
for celeb in celebs:
    favouriteMusicians.append(celeb.title())
print(favouriteMusicians)
print(len(favouriteMusicians))
celebs.sort()
print(celebs)
print(celebs)
celebs.pop(-1)
celebs.pop(-1)
print(celebs)
print(len(celebs))
print(int(len(favouriteMusicians))- 2 == int(len(celebs)))