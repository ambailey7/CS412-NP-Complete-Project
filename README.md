# CS412-NP-Complete-Project

This is the source code and presentation repo for the NP project in Dr. Bowers' CS412 class, Spring 2023 semester.



## Exact Solution
"The input is a weighted graph specified by a line containing the number of vertices n and the number of edges m followed by m lines containing the edges given in u v w format, meaning an edge between u and v of weight w. TSP graphs are assumed to be undirected and edges will be listed only once, LP graphs are directed. TSP graphs will be complete."   --Dr. Bowers

Example input:


3 3

a b 3

b c 4

a c 5


Example output:


12

a b c a



## Approximate Solution
The input is exactly the same as for the exact solution. It will run the nearest neighbor algorithm to greedily choose the closest solution. A hill climbing implementation is also provided, reminiscent of a slower attempt at an approximation solution.



## Running Test Cases
In both the exact and approximate solution folders, there exists a run_test_case.sh file. Each file will run the corresponding solution with the provided test cases. Any added test cases must be in the form "test_case#.txt" where the '#' is a new number.
