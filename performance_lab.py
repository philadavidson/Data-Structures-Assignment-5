# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    counts = {}
    most_common = None
    highest_count = 0

    for number in numbers:
        # Increases the number's count, starts at 0 if it's new
        counts [number] = counts.get(number, 0) + 1

        # Updates the result when this number takes the lead
        if counts[number] > highest_count:
            highest_count = counts[number]
            most_common = number

    return most_common

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) Even if every number in the dicitonary is identical the loop still processes each element.
- Worst-case: O(n) Each element is processed once even if every number is unique.
- Average-case: O(n) Each number requies a dictionary update and comparison so the work grows linearly with the list size.
- Space complexity: The dictionary stores an entry for every number. In a worst case scenario where every number is unique it makes the space compelexity O(n).
- Why this approach? Dictionaries allow us to count occurrences without repeatedly searching the list. Keeping track of the most frequent number during the loop also avoids a separate pass over the counts.
- Could it be optimized? For an unsorted list, this approach already reulst in O(n) time. Sorting could help speed things up but might result with O(n log n) time.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n) Even if every number is the same we still check each element. 
- Worst-case: O(n) If every number is unique, each one is checked and added to both the set and the result list.
- Average-case: O(n) Every number is processed once, so the work grows linearly with the input size.
- Space complexity: Both the set and result lists store values. In a worst case scenario where all the numbers are unique the space complexity is O(n).
- Why this approach? This approach allows for fast duplicate checks and preserves the list order. If we only checked the result list that would take O(n) per check, which would make the total runtime O(n^2).
- Could it be optimized? O(n) is already efficient. list(dict.fromkeys(nums)) would allow for shorter code, but the time and space complexity would be the same.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n) If there are no matches, every element is still checked.
- Worst-case: O(n) If every number belongs to a matching pair, we still process every element once.
- Average-case: O(n) For each number, we calculate its complement and check the set. The amount of work grows linearly with the number of inputs.
- Space complexity: Since there are no duplicates, the set will eventually store every number.
- Why this approach? The set checks for each complement O(1) time. If we checked each number with every other number using nested loops we would end up with O(n^2) time.
- Could it be optimized? Since O(n) is already optimal when every element must be examined. If the list were sorted the process could be sped up.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 2
    items = [None] * capacity
    size = 0

    for number in range(n):
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}")

            new_items = [None] * new_capacity

            for index in range(size):
                new_items[index] = items[index]
                print(f"Copying {items[index]}")

            items = new_items
            capacity = new_capacity

        items[size] = number
        size += 1
        print(f"Added {number}")

"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizes occur when the list is full and an element needs to be added. 
- What is the worst-case for a single append? When one element needs to be but the list is full, resulting in the entire list being copied over to a new list along with the new append.
- What is the amortized time per append overall? Adding an element takes O(n) time. So total time is constant based on the number of inputs.
- Space complexity: Capacity grows proportionally to the number of elements. During resizing, both lists exist temporarily, but eventually total space returns to O(n).
- Why does doubling reduce the cost overall? Each resize creates more room for insertions before needing to resize again. This avoids having to create new lsits for each insertion.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    total = 0
    result = 0

    for num in nums:
        total += num
        result.append(total)

    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n) Easier inputs still require an addition and append for each element.
- Worst-case: O(n) No inputs cause extra work. Still requires one addition and append for each element.
- Average-case: The work grows linearly with the inputs, the values don't change how many iterations are needed. 
- Space complexity: O(n) for the list of running totals. The funciton uses O(1) time.
- Why this approach? Keeping a running total, this approach avoids having to add up all the previous elements over and over for each new input. 
- Could it be optimized? O(n) is already optimal since every element must be processed. 
"""
