# 1a
sequence1 = "ACTG"
sequence2 = "TCCG"
joined_sequences = sequence1 + sequence2
print(joined_sequences)
print("Length: ", len(joined_sequences))



# 1b
A = 2
C = 4
G = 3
T = 5

melting_temperature = 4 * (G + C) + 2 * (A + T)

print("Melting temperature: ", melting_temperature)


# 1c

def compute_melting_temperature(A, C, G, T):
    return 4 * (G + C) + 2 * (A + T)

print("Melting temperature: ", compute_melting_temperature(2, 4, 3, 5))


# 1 d
# Corrected function below
# The error was that the return True was intented one step too much.
# The idea here is that we want to return False if any of the bases are invalid. The code inside the function will then stop being executed.
# We only want to return True if we are done checking all bases and have not returned False
def sequence_is_valid_dna(sequence):
    for base in sequence:
        if base is not "A" and base is not "C" and base is not "G" and base is not "T" and base is not "N":
            return False

    return True

print(sequence_is_valid_dna("ACTG"))
print(sequence_is_valid_dna("YACT"))


# The if sentence can be written has
# if base not in ["A", "C", "T", "G", "N"]:


# 1e

def compute_gc_content(sequence):
    number_of_g_and_c = 0
    for base in sequence:
        if base == "G" or base == "C":
            number_of_g_and_c += 1

    return number_of_g_and_c / len(sequence)

print(compute_gc_content("CCCTTT"))
print(compute_gc_content("ACA"))
print(compute_gc_content("ACTACACTTAGGACCAC"))



# 1f

f = open("open_chromatin_chr6.bed")
n_big_regions = 0
for line in f:
    splitted_line = line.split()
    start = int(splitted_line[1])
    end = int(splitted_line[2])

    if end - start > 5000:
        n_big_regions += 1
        print(start, end)

print("N big regions: ", n_big_regions)

# There are 60 regions larger than 5000 base pairs
