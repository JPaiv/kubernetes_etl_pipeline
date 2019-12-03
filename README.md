

### This folder contains the scripts for French business data

Basic data comes from a single source which is INSEE. INSEE is the French official research agency and they offer us an access to over 28 million prospects. Most of the prospects are not active and many prospects are not businesses.


### WARNING!

This is a portfolio code so it wont work on your machine unless you have AWS s3 and kubernetes for the pipeline.


### Source files

Data comes in two different files which are legale and etablissement. Legale data(legale) contains the juridical information such as name, business_id and other relevant information.

Etablissement(etablissement) data contains information about the prospect side and branch offices. Establishment data contains only information about the branch and side offices. It doesn't have any other prospect information.


### How to run the code

Run the code is as a module due to all the imports. Rememver to run the module in the root directory!

Commands for the code are these:

1) For French business establishment data:
python3 -m main.basic_data etablissement

2) For French business prospect data:
python3 -m main.basic_data legale


### The scripts do the following:

1) Download and unzip the source file to s3

2) Chunk the source data file into smaller 1 million row chunks and start kubejobs for each chunk

3) Kubejob will parse the chunked data 
