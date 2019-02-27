# CompBio_Ecoli_Project

A brief desciption: The E. coli K12 strain was isolated in 1922. Using this pipeline, we will align the resquenced data against the original strain used in labs. Because the nature of bacteria is to mutate, we want to check how similar our sequence is to the original. This pipeline is set up to work from any directory. 

Tools to run this project
1) SPAdes v3.11.1
2) Prokka
3) tophat v2.1.1,
4) bowtie v1.2.2
5) cufflinks v2.2.1
6) SRA-toolkit
7) wget
8) Python3

The pipeline will not run unless these tools are installed. 

running the pipeline:
$ git clone https://github.com/AmandaKatherine/CompBio_Ecoli_Project.git

After the download is done, 
python3 COMPBIO_AMANDA_WILLS.py

The Steps are as following:
1) downloading the Ecoli data from ncbi and fastq dumping to a usable form
2) assembling the genome with spades and throwing out contigs under 1000 basepairs
3) putting all the contigs over 1000 basepairs into one long supercontig
4) annotating the genome with prokka 
5) anaylis of our genome after prokka against a ref seq to note differences
6) get more data from ncbi to align our sequence with and pulling in the refseq genome
7) building a index with bowtie2 to run our tophat commands 
8) using Tophat to aligns our sequence with the reference sequence(NC_000913.fna) 
9) cufflinks assembles the reads from tophat2

The whole pipeline is run with python3
If you want, the commands are set up to be run in chunks in my pipeline and it would be benefical to run them seperately if you want to see the individual actions of the commands. 

author- Amanda Wills
