
### s3 tools

This folder contains the ready code scripts for s3. These tools allows the programme to upload, download and remove data from WS S3.


### AWS S3 explained

AWS S3 is an object storage.


### How s3 works

S3 is based on buckets where the data objects are stored. S3 must have a bucket, otherwise you cannot save data to s3.

Vainu operates on multiple buckets though it's recommended to use existing buckets as often as possible tp keep S3 simple and clean.


### Shell script commands

If you upload a directory to S3 with shell scripting.

AWS CLI will synchronize the current working directory contents with the AWS bucket and key:
aws s3 sync ./ s3://bucket_name/key_folder/stored_data.csv
