#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Experiment No: 8
# Solve Cryptarithmetic Problem using CSP

from itertools import permutations

def solve_cryptarithmetic(word1, word2, word3):

    # Get all unique letters
    letters = set(word1 + word2 + word3)

    # Check maximum number of unique letters
    if len(letters) > 10:
        print("No solution possible!")
        return

    # Letters that cannot be zero
    first_letters = {
        word1[0], word2[0], word3[0]
    }

    # Try all possible digit assignments
    for perm in permutations(range(10), len(letters)):

        # Create letter-to-digit mapping
        mapping = dict(zip(letters, perm))

        # First letters cannot be zero
        if any(mapping[ch] == 0 for ch in first_letters):
            continue

        # Convert words into numbers
        num1 = int(''.join(str(mapping[ch]) for ch in word1))
        num2 = int(''.join(str(mapping[ch]) for ch in word2))
        num3 = int(''.join(str(mapping[ch]) for ch in word3))

        # Check arithmetic condition
        if num1 + num2 == num3:

            print("\nSolution Found!")
            print(word1, "=", num1)
            print(word2, "=", num2)
            print("-" * 15)
            print(word3, "=", num3)

            print("\nLetter to Digit Mapping:")
            for letter in sorted(mapping):
                print(letter, "=", mapping[letter])

            return mapping

    print("No solution found!")


# Main program
print("CRYPTARITHMETIC PUZZLE")
print("Example: SEND + MORE = MONEY")

word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
word3 = input("Enter result word: ").upper()

solve_cryptarithmetic(word1, word2, word3)


# In[ ]:




