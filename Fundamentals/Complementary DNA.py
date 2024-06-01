'''
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side.
DNA strand is never empty or there is no DNA at all (again, except for Haskell).
'''

def DNA_strand(dna):
    new_dna = ''
    for i in dna:
        if i == "A":
            new_dna += 'T'
        elif i == "T":
            new_dna += 'A'
        elif i == "G":
            new_dna += 'C'
        elif i == "C":
            new_dna += 'G'
    return new_dna

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand1(dna):
    return ''.join([pairs[x] for x in dna])

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

n = input()
print(DNA_strand(n))
