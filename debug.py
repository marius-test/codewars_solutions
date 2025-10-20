# for testing and debugging code

dna1 = "GCAT"


def dna_to_rna(dna):
    rna = dna.replace("T", "U")
    return rna


if __name__ == "__main__":
    print(dna_to_rna(dna1))
    