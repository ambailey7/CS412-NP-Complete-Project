# !/bin/bash


# Run the test cases
for file in test_cases/*.txt; do
    echo "Running test case: $file"
    time python3 cs412_pa_a.py < $file
    echo "Done running test case: $file"
    echo ""
    echo "-----------------------------------"
    echo ""
done