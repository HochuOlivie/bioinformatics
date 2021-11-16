#!/bin/bash

fastqc SRR15859207.fastq
minimap2 -d ref.mmi ref.fna                       # indexing
minimap2 -a ref.mmi SRR15859207.fastq > SRR15859207.sam   # alignment
samtools flagstat SRR15859207.sam > SRR15859207_flagstat.txt
python main.py 
