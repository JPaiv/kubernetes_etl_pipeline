
### What is dask?

Dask is a multiprocessing framework to run data science operation in paraller.


### Example

import dask.dataframe as ddf

def iterate_dataframe(dataframe):
    '''
        This is a sample of how dask dataframe iteration works
    '''

    df_dask = ddf.from_pandas(dataframe, npartitions=8)#How many paraller processes
    prospects = df_dask.apply(lambda x: parse(x), axis=1, meta=('str')).compute(scheduler='multiprocessing')#pylint: disable=unnecessary-lambda


def parse(row):
    '''
        Data can be parsed directly during the iteration
    '''
    prospect = row['company_name']
    return prospect


### How it works

1. Create standard pandas dataframe

2. Mutate the pandas dataframe into a dask dataframe

3. Iterate trough the dask dataframe and parse the data to a set of dicts

4. Send the set of dicts to Vainu API

This operation iterates trough the dask dataframe one row at a time. The lambda function will then parse the data and append the dict to the set. The set will containt every dataframe row as parsed dicts if the operation is succesful. The entire operation should take less than 5 minutes.

Pylint hates dask so remember that dask import and lambda have to be disabled for pylint or else.


### Imports

There is a ready function in the dask tools folder in dask_tools python file. Import it to your code location.

from nightcrawlers.utils.dask.pandas_to_dask import iterate_dataframe
