# Aarithi Rajendren
# UFID: 70126719
# Cache Eviction Policy Comparison (FIFO, LRU, OPTFF)

## Repository Structure

```text
├── README.md
├── src
│   └── cache_eviction_policy.py
├── data
    ├── nontrivial_file1.in
    ├── nontrivial_file2.in
    ├── nontrivial_file3.in
    ├── example.in
```

## Requirements
Python 3.11.6 (or compatible 3.11.x)

## Build / Compile
No compilation is needed for the Python code.

## Running the Program
example command: python cache_eviction_policy.py <input_file> <output_file>
From the src directory:
python3 cache_eviction_policy.py ../data/example.in ../data/example.out

## Expected output:  
```
FIFO  : <number_of_misses>  
LRU   : <number_of_misses>  
OPTFF : <number_of_misses>
```
You can run the three nontrivial inputs used in the written component:  
python3 cache_eviction_policy.py ../data/nontrivial_file1.in  
python3 cache_eviction_policy.py ../data/nontrivial_file2.in  
python3 cache_eviction_policy.py ../data/nontrivial_file3.in
```
Each run prints:  
FIFO  : <number_of_misses>  
LRU   : <number_of_misses>  
OPTFF : <number_of_misses>
```
## Input Format
Each input file must have:
k m
r1 r2 r3 ... rm

where:
k — cache capacity (k >= 1)
m — number of requests
r1 .. rm — sequence of integer IDs (space-separated; may span multiple lines after the first).

## Output Format
```
The program prints:  
FIFO  : <number_of_misses>  
LRU   : <number_of_misses>  
OPTFF : <number_of_misses>
```
## Written Component
https://github.com/aarithi123/COP4533_Programming_Assignment_2/blob/main/Q%26A%20Assignment%202.pdf
