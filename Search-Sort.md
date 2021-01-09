# Search & Sort

These questions are mainly about implementing search and sort algorithms. Each question will have step-by-step instructions describing the algorithm. If something is unclear about the algorithms, most questions also have a link to a visualization under them that you can check.

You can create helper functions, and/or use recursion if you wish. It could be beneficial to think how you could implement your solution both with and without recursion. Make sure you implement the algorithm correctly. This means don't use python's own search/sort functions, and keep complexity in mind as you write your code.

Also, these algorithms have python solutions available online, for your benefit, try to implement them without getting any hints from other code.

You can find the function templates in the file search_sort.py . We also gave you two functions called `random_list` and `sorted_list` which generate lists for you, you can use them to generate inputs for your code.

---

**Question 1)** Complete the function `counting_sort`. Your function should take a list of integers with a maximum value of 100 and use the counting sort algorithm to sort the list, then return the sorted data.

Algorithm steps: 
1. Create an array named `aux` of size greater than the maximum element of the list you need to sort, initialize it with 0 values.
2. Iterate over the list you must sort, for each element, increment `aux[element]` by 1.
3. Iterate over `aux`, and generate a sorted list by appending each non-zero element to an empty list.

Visualization:
https://www.cs.usfca.edu/~galles/visualization/CountingSort.html

---

**Question 2)** Complete the function `ternary_search`. Your function should take a list of sorted numbers (float or int shouldn't matter) and a target number as input, then use the ternary search algorithm to find the index of the target. Ternary search is just like binary search, but at each step, you divide the list into three parts rather than two. If the target doesn't exist in the list, you must return -1.

Algorithm steps:
1. Divide the list into three sublists.
2. Check which partition should contain the target.
3. Repeat steps 1-2 until you find the target number, or notice that it does not exist in the list.

Visualization:
https://media.geeksforgeeks.org/wp-content/uploads/ternaryS-3.png

---

**Question 3)** Complete the function `insertion_sort`. Your function should take a list of numbers (float or int shouldn't matter) and use the insertion sort algorithm to sort the list, and return the sorted data.

Algorithm steps:
1. Start from the second element of the list
2. If the current element is smaller than the element on the left, move it so that the left side of the array is properly sorted.
3. Move to the next element on the right
4. Repeat until you reach the end of the list

Visualization:
https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/

---

**Question 4)** Complete the function `nary_search`. This function should work just like binary and ternary search, but the amount of sublists you divide the sorted array is given to you as an input to the function,`n`.

Algorithm steps:
1. Divide the list into n sublists.
2. Check which partition should contain the target.
3. Repeat steps 1-2 until you find the target number, or notice that it does not exist in the list.

---

**Question 5)** Given a sorted list, a target to search for, and an integer named "jump", implement the `jumping_binary_search` function, which looks for an element in the list and returns its index. If the element does not exist in the list, you must return -1 instead. The jump search algorithm is as follows:

1. Starting from the 0 indexed element, start checking array elements with indexes 0, jump, 2\*jump ... k\*jump until you find an element that is larger than the target element.
2. Assuming the index you stopped at is i\*jump, take the sublist from (i-1)\jump to i\*jump.
3. Do binary search on the sublist to find the target.
4. Return the index of the target.

Example usage:
`jumping_binary_search([0, 1, 2, 3, 4, 5, 6], 3, 2)`
> Should return 4

`jumping_binary_search([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 12, 5)`
> Should return 6

`jumping_binary_search([0, 1, 2, 3, 4, 5, 6], 7, 2)`
> Should return -1

Visualization:
https://harkishen-singh.github.io/jump-search-visualisation/

---

**Extra Question)** Can you determine the complexities of all the functions you have written?