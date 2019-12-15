#!/bin/bash
echo 'iterative'
python3 ./mergesort_iter.py < number.in

echo 'recursive'
python3 ./mergesort_recur.py < number.in
