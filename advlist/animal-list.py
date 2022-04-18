#!/usr/bin/env python3

#challenge
#Fox Fly Ant Bee Cod Cat Dog Yak Cow Hen Koi Hog Jay Kit

animallist = ['fox','fly','ant','bee','cod','cat','dog','cow']
print(animallist)

moreanimals = ['yak','hen']
animallist.append(moreanimals)
print(animallist)

evenmore = ['koi','hog']
animallist.extend(evenmore)
print(animallist)