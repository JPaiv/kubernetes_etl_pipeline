
### s3 tools

This folder contains the ready code scripts for s3. These tools allows the programme to upload, download and remove data from WS S3.


### AWS S3 explained

AWS S3 is an object storage.


### How s3 works

S3 is based on buckets where the data objects are stored. S3 must have a bucket, otherwise you cannot save data to s3.

Vainu operates on multiple buckets though it's recommended to use existing buckets as often as possible tp keep S3 simple and clean.


### How to upload regular data to S3

To save an object to S3 the user needs to to use a script for specific types of data. With regular data such as csv, excel and pdf etc the following script is the used in Python3:

nightcrawlers.utils.s3.s3_tools.upload_to_s3

upload_to_s3 is a preset function which takes following arguments:

source: define the source where data comes from eg. netherlands_creditsafe. Source name isn't limited to specific data source name but can be anything. In this context the source name functions as a directory name where data can be stored.

source example:
'netherlands_creditsafe', 'financial_pdf_netherlands_2018'

file_name: path to the file you wish to upload to s3. Remember to give the data as a path so the script will find it!

file_name example:
file_name = /user/vainu_backend/financial_pdf_netherlands/mederjedels_software_annual_report_2018.pdf

key_location_data_type: specify the name and data type you wish the save the file as.

key_location_data_type example:
key_location_data_type = 'mederjedels_software_annual_report_2018.pdf'

Default bucket for nightcrawlers data is 'vainu-us-states-crawled'. Unless you specify other bucket all the data is saved there!

upload_to_s3('financial_pdf_netherlands_2018', '/user/vainu_backend/financial_pdf_netherlands/mederjedels_software_annual_report_2018.pdf', 'mederjedels_software_annual_report_2018.pdf')

This will store the data as following:

vainu-us-states-crawled/financial_pdf_netherlands_2018/mederjedels_software_annual_report_2018.pdf


### How to upload nested directories to S3

If you wish to store directories inside directories it needs to be specified in the key_location_data_type argument:

key_location_data_type nested directory example:
upload_to_s3('financial_pdf_netherlands_2018', '/user/vainu_backend/financial_pdf_netherlands/mederjedels_software_annual_report_2018.pdf', '/mederjedels_software/mederjedels_software_annual_report_2018.pdf')

This will store the data as following to S3:
vainu-us-states-crawled/financial_pdf_netherlands_2018/mederjedels_software/mederjedels_software_annual_report_2018.pdf

You can upload multiple files to this directory:
vainu-us-states-crawled/financial_pdf_netherlands_2018/mederjedels_software/


### Shell script commands

If you upload a directory to S3 with shell scripting.

AWS CLI will synchronize the current working directory contents with the AWS bucket and key:
aws s3 sync ./ s3://bucket_name/key_folder/stored_data.csv
