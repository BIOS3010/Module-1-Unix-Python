# Python exercises (repetition)
In the exercises below, you will repeat some of the Python you learned in BIOS1100. Skip this exercise aif you feel comfortable coding in Python.

Write your answers to these exercises as Python code using a text editor like Notepad++ or Atom. Try to solve everything first before looking at the solution. If you are stuck, have a look at the slides or other material online.



## Exercise 1.5.1
```diff
! Write a program that stores the two sequences `ACTG` and `TCCG` in two separate variables.
! Write Python codes that prints these two sequences joined into one sequence (`ACTGTCCG`)
! Write Python code that prints the length of the resulting sequence.
```

## Exercise 1.5.2 
```diff
! What gets printed in the following program?
```

```python
a = 5
a += 10

if a < 15:
    print("Hi")
elif a + 10 > 100:
    print("Hello")
elif "ACTG" in "AAACTGGGG":
    if a / 3 == 5:
        print("Hi")
    elif a < 15:
        print("Hei")
else:
    print("Heisann")
```

## Exercise 1.5.3
The formula for DNA melting temperature is `4(G+C) + 2(A+T)` where G, C, A and T are the number of times the bases occur in the sequence.
Assume you start with the following code:
```python
A = 2
C = 4
G = 3
T = 5
# add your code here ...
```
```diff
! Add a line that computes the melting temperature
! And another line that prints the melting temperature
```

## Exercise 1.5.4
Now,
```diff
! Create a function that takes four arguments, A, C, G, and T and returns the melting temperature. 
! The name of your function should be `compute_melting_temperature`.
```

```diff
! Call your function with the values for A, C, G, and T given in the previous exercise
! Verify that you get the same melting temperature as in the previous exercise.
```

## Exercise 1.5.5
The following function is supposed to return True if a DNA sequence is valid DNA and False if not. However, there is something wrong this code:

```python
def sequence_is_valid_dna(sequence):
    for base in sequence:
        if base is not "A" and base is not "C" and base is not "G" and base is not "T" and base is not "N":
            return False
            
        return True
``` 

```diff
! Find the error and make the code work.
```

If you find this difficult, try testing the code with a few sequences, and insert print statements in the code that can help you understand what happens.

PS: We allow A, C, T, G and N (since N is commonly used to denote unknown nucleotide).

Bonus task: 
```diff
! The if-sentence is a bit clumsy. Try to make it more concise? Hint: Lists
```

## Exercise 1.5.6
GC-content is the ratio of number of `G`s and `C`s in a DNA sequence. For instance, the GC-content of `ACTG` is 50%.

```diff
! Write a function that takes a sequence as input and returns the GC-content. 
! Test the function with a few sequences of your choice.
```

## Exercise 1.5.7
In this exercise you will write a small program that reads a BED file.
First, use Bash to check that the file `open_chromatin_chr6.bed` is available for you:
```bash
ls ~/BIOS3010/data/
```
This is a BED file with open chromatin regions on chromosome 6 in human (regions with accessible DNA). The second column is the start position and the third column is the end position.

```diff
! Write a Python program that reads this file and:
! prints the start and end position of all regions that are larger than 5000 base pairs.
```

```diff
! How many such regions are there?
```



