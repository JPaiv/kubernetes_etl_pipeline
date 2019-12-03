

### This folder contains the scripts for French basic data

Basic data comes from a single source which is INSEE. INSEE is the French official research agency and they offer us an access to over 28 million prospects. Most of the prospects are not active and many prospects are not businesses.


### Source files

Data comes in two different files which are legale and etablissement. Legale data(fr_legale) contains the juridical information such as name, business_id and other relevant information.

Etablissement(fr_etablissement) data contains information about the prospect side and branch offices. Establishment data contains only information about the branch and side offices. It doesn't have any other prospect information.


### How to run the code

Run the code is as a module due to all the imports. Rememver to run the module in the root directory!

Commands for the code are these:

1) For French business establishment data:
python3 -m main.basic_data etablissement

2) For French business prospect data:
python3 -m main.basic_data legale


### The scripts do the following:

1) Download and unzip the file(fr_basic_data)

2) Chunk the data file and start kubejobs for each chunk(fr_basic_data) with imported helper function

3) Kubejob will parse the data with one of the parsers(establishment_parse or legale_parse) depending on the source

4) Kubejob sends the data to Vainu API automatically


### France main company headquarters

In France the files contain information in a very peculiar way. This is why we don't receive address information with the legal data file(fr_legale). This is why company address must be parsed from another file(fr_etablissement")

The etablissement parser takes the main head office from the industry code and uses the head office information the parse the headquarters office address and other information to prospect.


### Kubernetes cronjob

Code is set to run in kubernetes at the following dates:

fr_etablissement:
6th day of every month at 00:30

Cronjob name and file location:
kubernetes/cronjobs/france-download-establishment.yaml

fr_legale:
7th day of every month at 00:30

Cronjob name and file location:
kubernetes/cronjobs/france-download-legale.yaml
