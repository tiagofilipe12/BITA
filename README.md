# BITA

Blast IT All

## Description

bita.py allows to blast mixed queries of proteins (tblastn) and nucleotides (blastn) against a custom nucleotide database or databases.

## Usage

```
-q; --query - Provide input queries (fastas). These queries can be protein fastas and nucleotide fastas. Mixed files won't work.

-d; --database - Provide databases to make queries

-t; --threads - Provide the number of threads to use

-e; --evalue - Provide the evalue to use

-of; --outfmt - Provide the output format type you want. For further information read blast+ documentation.

-st; --sequence_type - Indicate the sequence type. Options must be nucl or prot for nucleotide and protein queries, respectively.
```
