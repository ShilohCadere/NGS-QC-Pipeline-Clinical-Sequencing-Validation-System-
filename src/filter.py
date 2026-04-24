def filter_sequences(sequences, min_length=30, max_n_percent=20):
    filtered = []

    for seq in sequences:
        n_percent = (seq.count("N") / len(seq)) * 100 if len(seq) > 0 else 0

        if len(seq) >= min_length and n_percent <= max_n_percent:
            filtered.append(seq)

    return filtered