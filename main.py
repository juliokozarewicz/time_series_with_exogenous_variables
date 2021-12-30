import config
from descriptive_statistics import Time_serie_level
from x13arima_seas_adjust import X13_arima_desaz
from stationarity import Stationarity_diff
from pandas import read_csv, to_datetime
import warnings


# suppress warnings - sorry about that =(
warnings.filterwarnings("ignore")


# Time_serie_level (descriptive statistics) {
# ==========================================================================

descriptive_statistics = Time_serie_level(config.data_endog, config.variable,
			 config.style_graph, config.color1, config.color2, 
                         config.color3, config.color4, config.color5)

descriptive_statistics.time_serie_plot()
descriptive_statistics.acf_pacf_plot()
descriptive_statistics.periodogram_plot()
descriptive_statistics.descriptive_stat()

# ==========================================================================
# }


# seasonality {
# ==========================================================================

# x13-arima-seats {
# --------------------------------------------------------------------------
x13_desaz = X13_arima_desaz(config.data_endog, 
                            config.data_exogs,
                            config.variable,
                            config.path_x13_arima,
                            config.style_graph, config.color1, config.color2, 
                            config.color3, config.color4, config.color5)

x13_desaz.x13_results()
x13_desaz.x13_seasonal_adjustment()
x13_desaz.independent_desaz_x13()
# --------------------------------------------------------------------------

#   }

# ==========================================================================
# }


# stationarity {
# ==========================================================================

try:
    data_non_seasonal = read_csv("3_working/seasonal_adjustment.csv",
                                 sep=",", decimal=".")

    data_non_seasonal["index_date"] = to_datetime(data_non_seasonal["index_date"])
    data_non_seasonal = data_non_seasonal.sort_values("index_date")
    data_non_seasonal = data_non_seasonal.set_index("index_date")
    
    stationarity = Stationarity_diff(data_non_seasonal,
                                     config.data_exogs,
                                     config.variable, 
                                     config.p_value_accepted)

    stationarity.adf_teste()
    stationarity.diff_data()
    stationarity.independent_var_stationarity()

except:
    print(f"\n\n\n{'=' * 80}\n\n")
    print(">>> The file with non-seasonal data 'seasonal_adjustment.csv' does not exist in the folder '3_working'. You have the options:\n\n")
    print("• Copy, paste and rename the file 'data_base.csv' to 'seasonal_adjustment.csv' and work with the data without seasonality treatment;\n")
    print("• Activate X13-ARIMA-SEATS in the 'main.py' file;\n")
    print("• Use other methods, such as: decomposition, Hodrick–Prescott filter or seasonal dummies (don't forget to put the file in the '3_working' folder and rename the file to 'seasonal_adjustment.csv'.")
    print(f"\n\n{'=' * 80}\n\n")

# ==========================================================================
# }

