def parse_fasta(file_path):
    sequences = []

    with open(file_path, "r") as f:
        seq = ""

        for line in f:
            line = line.strip()

            if line.startswith(">"):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line

        if seq:
            sequences.append(seq)

    return sequences