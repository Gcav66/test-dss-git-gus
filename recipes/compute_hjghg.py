# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
customers_base_prepared = dataiku.Dataset("customers_base_prepared")
customers_base_prepared_df = customers_base_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

hjghg_df = customers_base_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
hjghg = dataiku.Dataset("hjghg")
hjghg.write_with_schema(hjghg_df)
