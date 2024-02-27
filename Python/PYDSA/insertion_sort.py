"""
Implement Insertion Sort and return intermediate states.

Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right.
It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

Objective:

Given a list of key-value pairs, sort the list by key using Insertion Sort. Return a list of lists showing the state of
the array after each insertion. If two key-value pairs have the same key, maintain their relative order in the sorted list.

Input:

pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).
Example 1:

Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")],
 [(2, "banana"), (5, "apple"), (9, "cherry")],
 [(2, "banana"), (5, "apple"), (9, "cherry")]]
Notice that the output shows the state of the array after each insertion. The last state is the final sorted array.
There should be pairs.length states in total.

Example 2:

Input:
pairs = [(3, "cat"), (3, "bird"), (2, "dog")]

Output:
[[(3, "cat"), (3, "bird"), (2, "dog")],
 [(3, "cat"), (3, "bird"), (2, "dog")],
 [(2, "dog"), (3, "cat"), (3, "bird")]]
In this example, you can observe that the pairs with key=3 ("cat" and "bird") maintain their relative order,
illustrating the stability of the Insertion Sort algorithm.

Where to test: https://neetcode.io/problems/insertionSort
"""
from typing import List


# Definition for a pair.
class Pair:

    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionsort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)  # get the length of our values
        result = []  # store results
        # loop over array
        for i in range(n):  # for every i in n list of values
            pairs = [5, 2, 1]
            # perform swap at i location in list of values to sort
            j = i - 1
            # compare by key values
            # if value at the j pointer is greater than value at the j+1 pointer, swap
            # make sure j is >= 0 to prevent index out of bounds after j decrement
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                # at j place j+1, at j+1 place j
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                # after swap, we're left with [2, 1, 5]
                # decrement j pointer by 1 to shift indices to compare 1 and 2
                j -= 1
            # append result to handle intermediary steps
            # pairs must be cloned with [:] due to frequent modifying
            result.append(pairs[:])

            # after algorithm completion, we're left with [1, 2, 5]
        return result
