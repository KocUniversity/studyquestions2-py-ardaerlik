# Algorithmic Complexity

### Free Code

What is the time complexity of the following algorithms? Write a short explanation for each case.

1.

```
a, b = 0, 0
for i in range(N):
  a += a * a 

for j in range(M):
  b += b * b; 
```

> Time Complexity: O(N+M) or O(N*M)?


2.

```
a = 0
for i in range(N):
  for j in range(N):
    a += i - j
```

> Time Complexity: O(log N) or O(N) or O(N^2) or O(N*log(N))?


3.

```
i, j, k = N/2, 2, 0

while i < N:
  while j < N:
    k = k + n / 2; 
    j *= 2
  i += 1
```

> Time Complexity: O(log N) or O(N) or O(N^2) or O(N*log(N))?


4.

```
a, i = 0, N
while i > 0: 
  a += i
  i /= 2
```

> Time Complexity: O(log N) or O(N) or O(N^2) or O(N*log(N))?


### Searching

1. What is the cost of searching an element in an unsorted list? Think about best and worst cases? Can you name the algorithmic complexity of the searcing algorithm? (Linear, Logarithmic, Quadratic, etc.)

2. Now, assume the list is sorted and we are searching for a value? What can we do to improve the speed of our searching algorithm? Can you find a way to reduce the complexity of the algorithm? Can you name the algorithmic complexity of the *new* searcing algorithm?

3. Now, assume we are searching for the maximum element in the **sorted** list. What is the best way of finding the maximum element in the **sorted** list? Can you name the algorithmic complexity of that search algorithm?


### The Devil in the Permutations

Remember the first question of PS3.5 where you wrote a recursive function to find all permutations of a string? What is the time complexity of that function, and why?


### Math is fun!

Remember the two different ways of computing exponentiation recursively that we have seen earlier in the class. Now that you know complexity classses, can you comment on their complexity, which complexity classes do each belong to?

1.
```
# write a recursive function to compute exponentiation: x**n
# pow(x, n) = x * pow(x, (n-1))
def exponentiate(x, n):
  if(n == 0):
    return 1
  else:
    return x * exponentiate(x, n - 1)
```

2.

```
# if n is even, then x**n = (x**2)**(n/2)
# if n is odd, then x**n = x * (x**2)**((n-1)/2)

def exponentiate_faster(x, n):
  if(n == 0):
    return 1
  else:
    if n % 2 == 0:
      return exponentiate_faster(x**2, n/2)
    else:
      return x * exponentiate_faster(x**2, (n-1)/2)
```

### Duplicates

Write a function called `repetitive` which checks for duplicates in a list of integers and returns `True` if there are any duplicates and `False` otherwise. What is the complexity of the algorithm you come up with in your first go? Can you make better than that?

**Hint**: What if I tell you that integers in the list can only take values between 0 and 100 (i.e. some fixed number and I tell you that number)? I also tell you that we have unlimited storage, can you create a *mapping* which will make your life better when searching for repetitive elements?


### Random Question

Now, assume you are given two lists and you are asked to find how many elements of the first list is also element of the second list. So, the problem is finding the number of common elements.

> list1 = [1,2,3,4,5]
> list2 = [3,4,5,6,7,8]

In that case, answer should be 3 since 3,4,5 are the common elements. 

Implement an algorithm to solve this problem. The most basic way might be checking all elements of the first list whether they are also in the second list. Analyze this algorithm's complexity. If we are given two lists whose lengths are N and M, what should be algorithmic complexity of this solution?

Now, please optimize the algorithm. What can you do improve the speed of the algorithm? Think about the possibilities. For example, lists can be sorted or unsorted. 

**Hint**: Every time, we are searching for an element. Can you suggest a better way for this? There is a trade-off between speed and space. What if you construct a database with the second list and query if an element is present instead of searching.

**Hint2**: Asking if an element in a list will require a linear search. Asking if an element in a dictionary will not require any search and it is constant.