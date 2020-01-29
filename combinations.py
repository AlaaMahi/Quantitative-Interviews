#!/usr/bin/env python

"""combinations.py: computing combinations."""

__author__      = "Alaa Eddine MAHI"
__copyright__   = "Copyright 2020, Quantitative Interviews"
__license__ = "GNU"
__version__ = "3.0"

# Brute force
def combinations(n, k):
	if k==0:
		return 1
	elif k > n:
		return 0
	return combinations(n-1, k-1) + combinations(n, k-1)

# Using factorial
def factorial(n):
	if n==0:
		return 1
	return n*factorial(n-1)

def combinations(n, k):
	return factorial(n)/(factorial(n-k)*factorial(k))

# Minimize number of recursion calls
def combinations(n, k):
	return combinations(n-1, k)*(n/k)

# Using symmetry to make it even faster
def combinations(n, k):
	if k > n/2:
		k = n-k
	return combinations(n-1, k)*(n/k)

# For-loop with symmetry
def combinations(n, k):
	r = 1
	if k == 0:
		return 1
	elif k > n/2:
		k = n-k
	for i in range(k):
		r *= n-i
		r /= i+1
	return r
