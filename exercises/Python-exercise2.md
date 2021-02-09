

# Python exercises (more practice)
Do these exercises if you have already done the [first exercises](Python-exercise1.md) and want more practice.

## Exercise 1.6.1
Write a function `find_sequences_with_match` that takes two arguments:
1) A list of sequences
2) A query sequence (string).

The function should find the sequences that contain the query sequence and return a new list of sequences containing only those sequences.

Test your function like this, and feel free to make a few more test cases:
```python
sequences = ["AAA", "AAT", "TAT", "CTTAT"]
query_sequence = "AT"

matching_sequences = find_sequences_with_match(sequences, query_sequence)
print(matching_sequences)

# Should print:
# ['AAT', 'TAT', 'CTTAT']
```


## Exercise 1.6.2
Write a function `average_gc_content` that takes a list of sequences as argument.

The function should return the average GC-content per sequence and you call the function you wrote in Exercise 1.5.6 to do the calcuations (i.e. do not re-implement the computation of GC-content, but instead call the function you wrote in 1.5.6. to compute the GC-content for each sequence, and then compute the average of these numbers).


## Exercise 1.6.3

Write a function `get_kmers` that takes two arguments:
1) A sequence
2) A number k

The function should return a list containing all the "kmers" of length k.

A kmer is a subsequence of k length. For instance, given the sequence `ACTGACTG` all the 3mers are `ACT`, `CTG`, `TGA`, `GAC`, `ACT`, `CTG`.

Test that `get_kmers` works before you continue.

Write a function `print_sequence_signature` that takes two parameters (sequence, k) and prints the "signature" of the sequence. The signature is all the unique kmers in the sequence and for each kmer a number saying how often the kmer occurs. Print every kmer together with its frequency on a new line.

For instance, given the sequence `ACTGACTG` and `k=3`, something like this should be printed (the order of the lines is not important):

```
ACT 2
CTG 2
TGA 1
GAC 1
```

