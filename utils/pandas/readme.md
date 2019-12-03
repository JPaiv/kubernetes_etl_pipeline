
### Pandas tools

These utility tools contain functions to create dataframe, parse dataframe, map dataframe iteration row, chunk dataframe to smaller pieces and start kubejob for each dataframe row.


### Dataframe chunkers

Dataframe chunkers python file contains functions used to cut the pandas dataframe into smaller pieces. 

chunk_to_csv_upload_s3_create_kubejob is used when the script itself chunks the dataframe into smaller pieces. Use this for small data processing.

chunk_csv_to_s3_create_kubejob_for_each_chunk does everything for you. It should be used with dask multiprocessing when the kubejob will parse the chunked data file.

By default the chunker has the most common pandas dataframe options suchs as encoding in the most common values.

Remember to give the kubernetes arguments as a list! 

It is not necessary to start the arguments with "python/python3"-call because the command is already implemented in the kubejob script that actually creates new kubejob.
 
By default the script limits number of kubejobs to 15 paraller kubejobs so the kubenetes can handle the load without much effort.

The limits and requests are for kubejob and there you can determine how much processing power your script needs. Try to keep these to a minimum because way pay for all the extra capasity anyway. By default the limits and the requests are at their lowest known working numbers but if you need more give it as following

Example:
limits={'cpu': '4', 'memory': '6Gi'}, requests={'cpu': '2', 'memory': '3Gi'}

The example had capasity for serious data processing. Amount of CPUs should not be above 4 and memory should not go above 8Gi. 


### Dataframe tools

map_row_values is used to rename pandas dataframe rows header names during iteration. This will help processing when header keys/names are the same as in Vainu database.

create_dataframe and create_dataframe_from_chunked_csv are used to download data file from s3 and then create a very basic dataframe from it. They will also replace all numpy nan values to empty strings.

pandas_dataframe is preset dataframe creation. Currently it has very little parameter options. It will also replace all numpy nan values to empty strings.

