from parser import parse_fasta
from qc import qc_summary
from filter import filter_sequences


def run_pipeline(input_file, output_file):

    print("Parsing FASTA file...")
    sequences = parse_fasta(input_file)

    print(f"Total sequences: {len(sequences)}")

    print("Running QC metrics...")
    qc_results = qc_summary(sequences)

    print("Filtering sequences...")
    filtered = filter_sequences(sequences, min_length=30, max_n_percent=20)

    # Summaries
    avg_gc = sum(r["gc"] for r in qc_results) / len(qc_results) if qc_results else 0

    report = []
    report.append(f"Total sequences: {len(sequences)}")
    report.append(f"Passed QC: {len(filtered)}")
    report.append(f"Failed QC: {len(sequences) - len(filtered)}")
    report.append(f"Average GC content: {avg_gc:.2f}%")

    # Write output
    with open(output_file, "w") as f:
        f.write("\n".join(report))

    print("\n".join(report))
    print(f"Report saved to {output_file}")


if __name__ == "__main__":
    run_pipeline("data/sample.fasta", "outputs/report.txt")