#!/usr/bin/env python

'''
https://leetcode.com/problems/find-the-duplicate-number/
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Input: [1,3,4,2,2]
Output: 2

Input: [3,1,3,4,2]
Output: 3
'''

def find_dup(ns):
    if len(ns) <= 1:
        return -1

    slow, fast = ns[0], ns[ns[0]]
    while slow != fast:
        slow = ns[slow]
        fast = ns[ns[fast]]

    fast = 0
    while fast != slow:
        fast = ns[fast]
        slow = ns[slow]
    return slow
