#!/usr/bin/env python
# coding: utf-8

# In[15]:


#to run this code, it needs to be inside terminal and saved as .py. ie ECOLI.py and it runs with python3 ECOLI.py. Your computer will need to be updated with python3

import os
import argparse
from Bio import SeqIO
#this is where the directory is set for the rest of the commands
dir = os.popen('pwd').read().rstrip()
#we make a currentPath so that these commands will work on any directory
currentPath = (dir +"/OptionA_Amanda_Wills/")
#set/change directy to the currentPath
os.system('mkdir ' +  currentPath)
#now that the system is changed to the right directory and the OptionA_Amanda_Wills will have our information put into it
os.chdir(currentPath)
 

#we need to get our test data from the backend of ncbi to run this code 
os.system("wget ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR818/SRR8185310/SRR8185310.sra")
    #SRR8185310.sra
#we need to put the information into a usable format so we are going to fastq dump the file 
os.system("fastq-dump -I SRR8185310.sra")
    #SRR8185310.fastq


#we need to annotate the assembly with the fastq file we just put into the folder
#spades is a de novo assembler, this step takes 8gb of ram!!
#it works well for Illuminia reads
os.system("spades -k 55,77,99,127 -t 2 --only-assembler -s SRR8185310.fastq      -o "  + currentPath)
 #saving this spades command as a variable to save it to the log file   
spadescommand = "spades -k 55,77,99,127 -t 2 --only-assembler -s SRR8185310.fastq      -o "  + currentPath
print(spadescommand)
    #contigs.fasta , contigs.path, scaffolds.fasta, scaffolds.paths, assembly_graph.fastg, assembly_graph_with_scaffolds.gfa, K55, K77, K99(these are the kmers)
    #the file we need for the next step is contigs.fasta
#this chunk is to write to the log file, we need the command to be stored in there
logfile = open(currentPath + "OptionA.log", "w+")
for l in range(1):
       logfile.write("The spades command is" + spadescommand + '\n')
    #inside the OptionA.log, the string "The spades command spades  -k 55,77,99,127 -t 2 --only-assembler -s SRR8185310.fastq      -o "  + currentPath" is there


#make an emply list
longboys=[]
#you have to import Bio again here if you are going to run the code in chunks 
from Bio import SeqIO
#using the parse function, the contigs are split in to id and record
for record in SeqIO.parse("contigs.fasta", "fasta"):
#find the length of each record and if they are over 1000 they are stored inside my list called longs boys
    if len(record)>1000:
my long boys store all the seqs over 1000
        longboys.append(record)
#here my variable b holds the strings that will get appended to the log.file
b = ("There are  " + str(len(longboys)) + " sequences > 1000 base pairs.")
#openig the log file to append the variable b inside 
logfile = open(currentPath + "OptionA.log", "a+")
for i in range(1):
       logfile.write(b + '\n')
# I take my list of the contigs over 1000 and put them into a new fasta file for the next step
SeqIO.write(longboys, "longcontigs.fasta", "fasta")



#we call in the fasta file we made in the last python scripts to find the length of the total assembly 
assemble = ('longcontigs.fasta')
#we make 2 seperate counters, one to hold the final length and 1 to hold the length of each record while we iterate through the whole file
total_length = 0
this = 0
from Bio import SeqIO
#using the same biopython parse function as the code above but if run in chunks, it needs to imported
for record in SeqIO.parse("longcontigs.fasta", "fasta"):
#this holds the length of each contig as it iterates
    this = (len(record))
  #this gets added to total_length   
    total_length += this
a = ("The total length of the assembly is " + str(total_length) + " base pairs")
#a is being stored as to be put in the log file
logfile = open(currentPath + "OptionA.log", "a+")
#
for i in range(1):
       logfile.write(a + '\n')
#The total length of the assembly is " + str(total_length) + " base pairs" is in the log file now



#this command runs prokka which is an assembly annotation, The Escherichia is a database that is on prokka upon intallation and the locus tag can be anything of your choosing
os.system("prokka  --outdir " +  currentPath+ "/Prokka_Results  --genus Escherichia --locustag ECLI longcontigs.fasta")
# prokka results are put into the Prokka_Results folder. You can cd in and look at all the files! 
#PROKKA_02262019.err  PROKKA_02262019.fsa  PROKKA_02262019.sqn
#PROKKA_02262019.faa  PROKKA_02262019.gbk  PROKKA_02262019.tbl
#PROKKA_02262019.ffn  PROKKA_02262019.gff  PROKKA_02262019.tsv
#PROKKA_02262019.fna  PROKKA_02262019.log  PROKKA_02262019.txt
prokkacommand = "prokka  --outdir " +  currentPath+ "/Prokka_Results  --genus Escherichia --locustag ECLI longcontigs.fasta"
    #contigs.fasta , contigs.path, scaffolds.fasta, scaffolds.paths, assembly_graph.fastg, assembly_graph_with_scaffolds.gfa, K55, K77, K99(these are the kmers)
    #the file we need for the next step is contigs.fasta
#this chunk is to write to the log file, we need the command to be stored in there
logfile = open(currentPath + "OptionA.log", "a+")
for l in range(1):
       logfile.write("The prokka command is " + prokkacommand + '\n')

#prokka creates a file specific to the day, which makes calling them in a little tricky, we are interested in the .txt file
import time
#date prints out as 02/24/19
date = (time.strftime("%x"))
#cast the date to a string so i can add in the 20 for 2019
date = str(date)
#print(date)
#remove all the unneeded characters
date = date.replace("/", "")
#the above chunck just creates the date so I can use the variable in my file calling 

#so i split up all the parts of the date into variables
#so each string number is seperate
a,b,c,d,e,f = date
g="2"
h="0"
todayDATE = (a + b +c + d + g + h + e +f)

#file_name is now a viable that has todayDATE that changes everyday so it will be able to call in the files
file_name = "PROKKA_" + todayDATE + ".txt"
#this rights the prokka txt file to the log file
with open(currentPath + "Prokka_Results/" + file_name) as f:
        with open("OptionA.log", "a+") as p:
                for line in f:
                        p.write(line + '\n')
#organism: Escherichia species strain
#contigs: 150
#bases: 4535677
#tmRNA: 1
#CDS: 4217
#tRNA: 52
#CRISPR: 2


                  
#now we want to anaylize the data from our prokka text file                  
data = open(currentPath+ "Prokka_Results/" + file_name)
#this numbers were given to us from the assignment sheet as a basis for the ref seq
CDS= 4140
TRNA = 89
#we go through the data and looks specifically for cds and trna and save those as variables 
for line in data:
    #this method is just saving lines that contain the string cds or trna and save everything after the index of 5 which is where the number string starts
    if line.startswith('CDS'):
        txt_cds = line[5:]
        
    if line.startswith('tRNA'):
        txt_trna = line[5:]


#the varibales are strings right now so we need to cast them as ints so we can put them into the log file

txt_cds = int(txt_cds)
txt_trna = int(txt_trna)
#i save a variable as the difference between the saved refseq cds and trna and compare it to the prokka results
cds_diff = CDS - txt_cds
trna_diff = TRNA - txt_trna

#this if loop figures out what the output sentence is going to be
if cds_diff >= 0:
    i = "less"
elif cds_diff <0:
    i = "additional"
 #the absolute value is used to make the numbers positive after we know if there is more or less of the cds or trna in the seq that we run prokka on   
    cds_diff = abs(cds_diff)
if trna_diff>=0:
    j = "less"
elif trna_diff<0:
    j = "additional"
    trna_diff = abs(trna_diff)

#saving the output sentence as a varibable to add the log file 
c = ("Prokka found " + str(cds_diff) + " " + i + " CDS and " + str(trna_diff) +  " " + j + " tRNA than the RefSeq." )

logfile = open(currentPath + "OptionA.log", "a+")
for i in range(1):
       logfile.write(c + "/n")
# in the log file "Prokka found " + str(cds_diff) + " " + i + " CDS and " + str(trna_diff) +  " " + j + " tRNA than the RefSeq."


#the last set of step
os.system("wget ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR141/SRR1411276/SRR1411276.sra")
# SRR1411276.sra

os.system("fastq-dump -I  SRR1411276.sra")
#SRR1411276.fastq

os.system("wget ftp://ftp.ncbi.nlm.nih.gov/genomes/archive/old_refseq/Bacteria/Escherichia_coli_K_12_substr__MG1655_uid57779/NC_000913.fna")
#NC_000913.fna 

#we use the refence we just wget in the fna. format and they are named EcoliK12 
os.system("bowtie2-build NC_000913.fna EcoliK12")
#EcoliK12.1.bt2, EcoliK12.2.bt2, EcoliK12.3.bt2, EcoliK12.4.bt2, EcoliK12.rev.1.bt2, EcoliK12.2.bt2    


####these last 2 steps take a very long time to run using 2 threads. If you can use more processors, I would highly recommend it
#aligns RNA-Seq reads to a genome in order 		to identify exon-exon splice junctions
#ignore warning messages the intron junction while it runs, there are no introns in bacteria and tophat warns you about this
os.system("tophat2 --no-novel-juncs -o " + currentPath + " EcoliK12 SRR1411276.fastq")
#tophat2 uses the index we built in the last index 
#this tophat commands makes an accepted_hits.bam for cufflinks to use

os. system("cufflinks -p 2 accepted_hits.bam")
#the output from this with be transcripts.gtf 

#an improvement on this project would be to successfully parse the gtf file to find gene id, start, end, FPKM and append it to a new file 

