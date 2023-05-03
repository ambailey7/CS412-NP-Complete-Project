# !/bin/bash

cd ..
cd exact_solution

# Run the test cases
for file in test_cases/*.txt; do
    echo "Running test case: $file"
    time python3 ../approximate_solution/cs412_tsp_approx.py < $file
    echo "Done running test case: $file"
    echo ""
    echo "-----------------------------------"
    echo ""
done