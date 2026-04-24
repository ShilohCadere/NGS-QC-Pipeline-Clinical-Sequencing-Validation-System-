# NGS QC Pipeline

QC validation module for clinical NGS pipelines performing sequencing quality assessment, threshold-based filtering, and PASS/FLAG/FAIL classification of genomic data.

## System Context
This pipeline is part of a broader clinical bioinformatics data system:

- Sample tracking and metadata management (LIMS database)
- Sequence processing utilities (genomic-toolkit)
- QC validation and filtering (this pipeline)

Together, these components simulate an end-to-end NGS data handling workflow.

## QC Workflow
```
Sequence Input
→ Parsing
→ QC Metric Calculation
→ Threshold Evaluation
→ PASS / FLAG / FAIL Classification
→ Summary Output
```

## QC Metrics
- GC content distribution
- AT content balance
- N-base frequency (ambiguous bases)
- Sequence length validation
- Quality flag assignment


## QC Decision Logic

Samples are evaluated using simple threshold-based rules:

- GC content outside expected range → FLAG
- High N content (> threshold) → FAIL
- Sequence length below minimum → FLAG

## How to Run
```
python src/cli.py --file data/sequence.fasta --gc
python src/cli.py --file data/sequence.fasta --at
python src/cli.py --file data/sequence.fasta --composition
```

## Output Example
```
Sample QC Report
-----------------
GC Content: 48.2%
AT Content: 51.8%
N Content: 0%
Status: PASS
```

## Input/Output Behavior
**Input:**
- FASTA file containing one or more nucleotide sequences
- Assumes standard nucleotide alphabet (A, T, C, G, N)

**Pipeline outputs:**
- QC metrics per sequence
- PASS / FLAG / FAIL status, where:
    - PASS → meets all QC thresholds
    - FLAG → review recommended
    - FAIL → sequencing failure likely
- Optional saved results file (CSV or TXT)

## Design Philosophy
This project prioritizes:

- Reproducible QC logic
- Transparent threshold-based evaluation
- Modular pipeline structure
- Clinical-style data validation workflows

## Use Case

This pipeline simulates a simplified clinical QC step used in:
- NGS sequencing validation workflows
- Pre-analysis sample screening
- Data quality filtering prior to variant analysis

It models early-stage QC checks commonly performed before downstream bioinformatics analysis.

## Author
### Shiloh Cadere
### Bioinformatics Analyst | Clinical NGS Pipelines | Python / R / SQL
