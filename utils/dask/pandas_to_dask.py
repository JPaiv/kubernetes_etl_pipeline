import dask.dataframe as ddf


def iterate_dataframe(dataframe, parse):
    """
        Turn a pandas dataframe into a dask dataframe which is iterated with multiprocess. Every row in the dataframe should be parsed so remember to give a data parser function! Results is a set of dicts.
    """

    df_dask = pandas_to_dask_dataframe(dataframe)
    return df_dask.apply(lambda x: parse(x), axis=1, meta=('str')).compute(scheduler='multiprocessing')


def pandas_to_dask_dataframe(dataframe):
    return ddf.from_pandas(dataframe, npartitions=8)
