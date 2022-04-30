'''
https://leetcode.com/problems/rotate-string/
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
'''
def rotateString( A, B):
		return any(A[i:] + A[:i] == B for i in range(len(A))) or A == B == ""

rotateString("hello","hi")