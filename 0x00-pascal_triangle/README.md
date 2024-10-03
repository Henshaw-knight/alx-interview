## Pascal's Triangle

This task involves generating Pascal's Triangle, a triangular array of binomial coefficients. Each row in the triangle corresponds to the coefficients of the binomial expansion of powers of (a + b).

### Task Objective
The goal is to implement a function that generates Pascal's Triangle up to a given number of rows. Each row in the triangle is built by summing adjacent values from the previous row.

### Algorithm Explanation
1. The triangle starts with a single `1` at the top (row 0).
2. Each subsequent row starts and ends with `1`.
3. Each interior value is the sum of the two numbers directly above it in the previous row.


### Code Implementation
The solution is implemented in Python, and the function `pascal_triangle(n)` takes an integer `n` as input and returns the first `n` rows of Pascal's Triangle.
