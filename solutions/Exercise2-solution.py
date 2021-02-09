

# Exercise 1.6.1

def find_sequences_with_match(sequences, query_sequence):
    matching_sequences = []
    for sequence in sequences:
        if query_sequence in sequence:
            matching_sequences.append(sequence)

    return matching_sequences

sequences = ["AAA", "AAT", "TAT", "CTTAT"]
query_sequence = "AT"
matching_sequences = find_sequences_with_match(sequences, query_sequence)
print(matching_sequences)


# Exercise 1.6.2

# Included the function written in 1.5.6
def compute_gc_content(sequence):
    number_of_g_and_c = 0
    for base in sequence:
        if base == "G" or base == "C":
            number_of_g_and_c += 1

    return number_of_g_and_c / len(sequence)

def average_gc_content(sequences):
    sum = 0
    for sequence in sequences:
        gc_content = compute_gc_content(sequence)
        sum += gc_content

    return sum / len(sequences)

# Testing the function
sequences = ["GC", "AC"]  # 100% GC content and 50% gc-content. Should on average give 75%
print(average_gc_content(sequences))


# Exercise 1.6.3
def get_kmers(sequence, k):
    kmers = []
    for i in range(0, len(sequence)-k+1):
        subsequence = sequence[i:i+k]
        kmers.append(subsequence)

    return kmers

print(get_kmers("ACTGACTG", 3))

def print_sequence_signature(sequence, k):
    kmers = get_kmers(sequence, k)

    unique_kmers = set(kmers)
    for kmer in unique_kmers:
        print(kmer, kmers.count(kmer))

# Note: There are different ways to count the unique kmers. One option is to create a
# dictionary where the keys are the kmers and values are counts. Then one could
# iterate through the kmers add counts to the dictionary

print_sequence_signature("ACTGACTG", 3)

