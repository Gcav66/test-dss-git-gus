# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
hjghg = dataiku.Dataset("hjghg")
hjghg_df = hjghg.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

dfadaf_df = hjghg_df # For this sample code, simply copy input to output


# Write recipe outputs
dfadaf = dataiku.Dataset("dfadaf")
dfadaf.write_with_schema(dfadaf_df)
