from pandas import to_datetime
from pandas import read_csv

# data input {
# =============================================================================

# training data {
# -----------------------------------------------------------------------------
data_entry = read_csv("3_working/data_base.csv", sep=",", decimal=".")
data_entry["index_date"] = to_datetime(data_entry["index_date"])
data_entry = data_entry.sort_values("index_date")

# date filter
data_select = data_entry[ (data_entry.iloc[:,0] >= '2010-01') &
                          (data_entry.iloc[:,0] <= '2020-12') ]

# variable for executing the model estimation
data_select = data_select.set_index("index_date")

# variables
data_endog = data_select.iloc[ : , 0 : 1 ]
data_exogs = data_select.iloc[ : , 1 :   ]
# -----------------------------------------------------------------------------
#   }

# exogs for forecast
# -----------------------------------------------------------------------------
data_exogs_fore = data_entry[ (data_entry.iloc[:,0] >= '2010-01') &
                              (data_entry.iloc[:,0] <= '2021-12') ]

data_exogs_fore = data_exogs_fore.set_index("index_date")
data_exogs_fore = data_exogs_fore.iloc[ : , 1 :   ]
print(data_exogs_fore)
# -----------------------------------------------------------------------------
#   }

# =============================================================================
# }
