# Pascal's Triangle

## Overview
This project implements a Python function to generate Pascal's Triangle up to a specified number of rows. Pascal's Triangle is a mathematical construct named after the French mathematician Blaise Pascal. It is a triangular array of binomial coefficients, where each number is the sum of the two numbers directly above it in the previous row.

## Project Structure
The project consists of the following files:

- **0-pascal_triangle.py**: Contains the implementation of the `pascal_triangle(n)` function to generate Pascal's Triangle.
- **0-main.py**: A sample script demonstrating how to use the `pascal_triangle` function to print Pascal's Triangle up to a specified number of rows.

## How to Use
To generate Pascal's Triangle, follow these steps:

1. Ensure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the `0x00-pascal_triangle` directory.
4. Use the `pascal_triangle` function in your Python script as follows:
    ```python
    from 0-pascal_triangle import pascal_triangle

    # Generate Pascal's Triangle with 5 rows
    triangle = pascal_triangle(5)
    print(triangle)
    ```

## Function Documentation
### `pascal_triangle(n)`
Generates Pascal's Triangle up to the `n`th row.

- **Parameters:**
  - `n` (int): The number of rows in Pascal's Triangle to generate.

- **Returns:**
  - List[List[int]]: A list of lists representing Pascal's Triangle.

- **Note:**
  Returns an empty list if `n` is less than or equal to 0.

## Examples
- Generating Pascal's Triangle with 5 rows:
  ```python
  triangle = pascal_triangle(5)
  print(triangle)

Output

[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

Resources
What is Pascal’s triangle
Pascal’s Triangle - Numberphile
What are Python Algorithms
Mock Technical Interview
Author
This Pascal's Triangle implementation was created by Elizabeth Eunice Ndzukule
