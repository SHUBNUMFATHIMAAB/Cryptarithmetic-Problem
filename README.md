<h1>ExpNo 8 : Solve Cryptarithmetic Problem,a CSP(Constraint Satisfaction Problem) using Python</h1> 
<h3>Name: SHUBNUM FATHIMA AB             </h3>
<h3>Register Number: 212225240147       </h3>

<H3>Aim:</H3>
<p>
    To solve Cryptarithmetic Problem,a CSP(Constraint Satisfaction Problem) using Python
</p>
<h3>Procedure:</h3>
Input and Output
<br>Input:
This algorithm will take three words.
<br> B A S E<br>
    B A L L<br>
           ----------<br>
           G A M E S<br>

Output:
It will show which letter holds which number from 0 – 9.
For this case it is like this.

              B A S E                         2 4 6 1
              B A L L                         2 4 5 5
             ---------                       ---------
            G A M E S                       0 4 9 1 6
Algorithm
For this problem, we will define a node, which contains a letter and its corresponding values.<br>

isValid(nodeList, count, word1, word2, word3)<br>

Input − A list of nodes, the number of elements in the node list and three words.<br>

Output − True if the sum of the value for word1 and word2 is same as word3 value.<br>

Begin<br>
   m := 1<br>
   for each letter i from right to left of word1, do<br>
      ch := word1[i]<br>
      for all elements j in the nodeList, do<br>
         if nodeList[j].letter = ch, then<br>
            break<br>
      done<br>
      val1 := val1 + (m * nodeList[j].value)<br>
      m := m * 10<br>
   done<br>

   m := 1<br>
   for each letter i from right to left of word2, do<br>
      ch := word2[i]<br>
      for all elements j in the nodeList, do<br>
         if nodeList[j].letter = ch, then<br>
            break<br>
      done<br>

      val2 := val2 + (m * nodeList[j].value)
      m := m * 10
   done<br>

   m := 1<br>
   for each letter i from right to left of word3, do<br>
      ch := word3[i]<br>
      for all elements j in the nodeList, do<br>
         if nodeList[j].letter = ch, then<br>
            break<br>
      done<br>

      val3 := val3 + (m * nodeList[j].value)
      m := m * 10
   done<br>

   if val3 = (val1 + val2), then<br>
      return true<br>
   return false<br>
End<br>
<hr>
<h2>Sample Input and Output:</h2>
SEND = 9567<br>
MORE = 1085<br>
<hr>
MONEY = 10652<br>
<hr>
<h2>Program:</h2>

```
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
```
<h2>Output:</h2>
<img width="318" height="110" alt="image" src="https://github.com/user-attachments/assets/83214183-d410-4c9d-b34c-507139088c47" />

<h2>Result:</h2>
<p> Thus a Cryptarithmetic Problem was solved using Python successfully</p>
