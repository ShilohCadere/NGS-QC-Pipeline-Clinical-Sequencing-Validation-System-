def gc_content(seq):
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100 if len(seq) > 0 else 0


def n_content(seq):
    return (seq.count("N") / len(seq)) * 100 if len(seq) > 0 else 0


def sequence_length(seq):
    return len(seq)


def qc_summary(sequences):
    results = []

    for seq in sequences:
        results.append({
            "length": sequence_length(seq),
            "gc": gc_content(seq),
            "n": n_content(seq)
        })

    return results