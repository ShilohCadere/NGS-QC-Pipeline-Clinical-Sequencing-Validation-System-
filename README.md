# NGS QC Pipeline

QC module for clinical-style NGS workflows that performs sequencing quality assessment, threshold-based filtering, and PASS/FLAG/FAIL classification of nucleotide data.

## System Context
This module is part of an integrated clinical bioinformatics system:

- **LIMS Database** → sample tracking and metadata management
- **Genomic Toolkit** → sequence processing utilities
- **NGS QC Pipeline** (this module) → sequencing quality evaluation and validation

Together, these components represent an end-to-end NGS data processing workflow from sample tracking to QC decisioning.

## Pipeline Overview
```
FASTA Input
→ Sequence Parsing
→ QC Metric Calculation
→ Threshold Evaluation (clinical rules)
→ Quality Classification
→ QC Summary Output
```
## QC Metrics
- GC content (%)
- AT content (%)
- N-base frequency (ambiguous bases)
- Sequence length validation

## Quality Classification Logic
- PASS → meets all QC thresholds
- FLAG → borderline metrics; review recommended
- FAIL → QC failure (e.g., high N content, invalid length)

Rules are based on simplified clinical-style QC thresholds.

## How to Run
```
python src/cli.py --file data/sequence.fasta --gc
python src/cli.py --file data/sequence.fasta --at
python src/cli.py --file data/sequence.fasta --composition
```

## Example Output
```
Sample QC Report
-----------------
GC Content: 48.2%
AT Content: 51.8%
N Content: 0%
Status: PASS
```

## Input Requirements
- FASTA format input (single or multi-sequence)
- Standard nucleotide alphabet (A, T, C, G, N)

## Output
- Per-sequence QC metrics
- PASS / FLAG / FAIL classification
- Optional file export (CSV/TXT depending on CLI flags)

## Design Focus
- Deterministic QC logic
- Reproducible evaluation rules
- Modular pipeline design
- Clinical-style sequencing validation structure

## Role in System

This module functions as the quality control layer within a broader NGS data system, enabling standardized evaluation of sequencing outputs prior to downstream analysis.

## Author

### Shiloh Cadere
### Bioinformatics Analyst | Clinical NGS Pipelines | Python / SQL / R
