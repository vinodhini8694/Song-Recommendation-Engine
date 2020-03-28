# -*- coding: utf-8 -*-
"""Asmt1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15maTSHHRkW8VAu33XpwrRoXHhdw6Gvkf
"""

import math
from operator import itemgetter
from similarity import *



# user ratings - this is the same data as we used in the User Recommendation Lecture
songData = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
                         "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
            "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0,
                     "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
            "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
                     "Slightly Stoopid": 1.0},
            "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0,
                    "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
            "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
                       "Vampire Weekend": 1.0},
            "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0,
                       "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
            "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
                    "Slightly Stoopid": 4.0, "The Strokes": 5.0},
            "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
                         "The Strokes": 3.0}
            }

# for whom are we making recommendations?
userX = str(input(
    "\nWho do you want to make recommendations for? \n Angelica \n Bill \n Chan \n Dan \n Hailey \n Jordyn \n Sam \n Veronica \n"))
userXRatings = songData[userX]
print(f"\n{userX}'s ratings are.. \n \n {userXRatings}")

similarity_measures = ["minkowski", "pearson"]
measure_index = int(input(
    "\n\nWhich similarity measure do you want to use? \n Enter 1 for Minkowski Distance \n Enter 2 for Pearson Correlation \n")) - 1
measure = similarity_measures[measure_index]
userSimilarities = []

if measure_index == 0:  # minkowski measure

    # r-value for minkowski distance
    minkowski_r = int(input("\nEnter the r-value for calculating minkowski distance.. \n "))

    for user in songData.keys():
        if user != userX:
            dist = similarity(songData[userX], songData[user]).minkowski(minkowski_r)
            # print(userX, user, dist)
            userSimilarities.append((user, dist))
            # print(f"\nUser similarities between {userX} and other users:\n", userSimilarities)

    # smaller the distance, closer the users are. Hence sort in aescending order of distance
    sortedUserSimilarities = sorted(userSimilarities, key=itemgetter(1), reverse=False)
    print(f"\nUser similarities between {userX} and other users (sorted): \n", sortedUserSimilarities)

else:  # pearson correlation measure

    for user in songData.keys():
        if user != userX:
            corr = similarity(songData[userX], songData[user]).pearson()
            # print(userX, user, corr)
            userSimilarities.append((user, corr))
    # print(f"\n User similarities between {userX} and other users: \n", userSimilarities)

    # migher the correlation, more similar the users are. Hence sort in descending order of correlation
    sortedUserSimilarities = sorted(userSimilarities, key=itemgetter(1), reverse=True)
    print(f"\n User similarities between {userX} and other users (sorted): \n", sortedUserSimilarities)

# find nearest neighbour of userX
userXNN = sortedUserSimilarities[0][0]
userXNNRatings = songData[userXNN]
print(f"\nNearest Neighbour of {userX} is {userXNN} \n")
print(userX, userXRatings)
print(userXNN, userXNNRatings)

# Recommendations for UserX
userXRecos = []
for item in set(userXNNRatings.keys()):
    if item not in set(userXRatings.keys()):
        userXRecos.append((item, userXNNRatings[item]))
# print(f"\nRecommendations for {userX} ", userXRecos)

# Sorted recommendations
userXSortedRecos = sorted(userXRecos, key=itemgetter(1), reverse=True)
# print(f"\nRecommendations for {userX} (sorted):", userXSortedRecos)

print("\n", "=" * 30)
print("Recommendations for", userX)
print("=" * 30)
print()
print(userXSortedRecos)