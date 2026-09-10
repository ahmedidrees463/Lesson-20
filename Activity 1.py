# 01-big-o-notation.py
# Topic: Big - O Noatation - each grotwh pattern has an officaial name
# Last class: Formula, Loop, Double loop. Today  each gets its Big - O name.

n = 10

guess = input("Double Loop at n = 10 checks n x n pairs. How many?")

input("Formula: one calculation, done. Press Enter to run " )
steps = 1
print("  steps=,", steps, " ->  0(1)  constant time  -> steps never change")

input("Loop: one step per item.   Press Enter to run")
steps = 0
for i in range(n):
    steps += 1
print("  steps =", steps, "->  0(n  linear time -> steps grow with n")

input(" Double Loop: checks every pair.  Presss Enter to run  ")
steps = 0
for i in range (n):
    for j in range(n):
        steps += 1
print("   steps =", steps, "  your guess:", guess, " -> O(n^2) quadratic time")

input ("Two more notations.  Press Enter")
print("  Big Omega  Ω ->  best case lower bound")
print("  Big Theta  Θ -> exact bound  (worst = best)")

