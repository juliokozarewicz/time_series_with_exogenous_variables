from statsmodels.tsa.x13 import x13_arima_analysis as x13a
from pandas import DataFrame
from pandas import read_csv
from matplotlib import pyplot as plt
from sys import platform


class X13_arima_desaz:
    """
    X-13 ARIMA-SEATS, successor to X-12-ARIMA and X-11, is a set of statistical 
    methods for seasonal adjustment and other descriptive analysis of time 
    series data that are implemented in the U.S. Census Bureau's.
    
    Required settings:
    - data_endog (dependent variable)
    - data_exogs (independent variables)
    - variable (formatted dependent variable - "NAME VARIABLE")
    - path (Directory of the folder where x13 arima seats are located)
    
    Optional settings:
    - style (graphic style)
    - color1 (color setting)
    - color2 (color setting)
    - color3 (color setting)
    - color4 (color setting)
    - color5 (color setting)

    Syntax: X13_arima_desaz(data_endog, data_exogs,variable name, path, 
                            style_graph, color1, color2, color3, color4, color5)
    """

    def __init__(self, data_endog, data_exogs, variable, path,
                 style_graph="seaborn", 
                 color1="royalblue", 
                 color2="crimson", 
                 color3="darkorange", 
                 color4="black", 
                 color5="red"):
        """
        Settings for the outputs.
        """
        
        # data frame
        self.data_endog = data_endog
        self.data_exogs = data_exogs
        
        # configs
        self.variable = variable
        self.variable_ = variable.replace(" ", "_").lower()
        
        # style
        self.style_graph = style_graph
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
        self.color5 = color5
        
        # X13-ARIMA-SEATS CONFIG
        self.path = path
        self.x13_desaz = x13a(data_endog, x12path=self.path)


    def x13_results(self):
        """
        Results obtained with X13-ARIMA-SEATS (dependent variable)
        """
        
        # style
        fig, ax = plt.subplots(4, 1, sharex=True, figsize=( 12 , 6), dpi=300)
        plt.style.use(self.style_graph)
        plt.rcParams.update({'font.size': 12})
       
        # x13 results 
        x13_seasonal = DataFrame(self.x13_desaz.seasadj.values,
                                 index=self.data_endog.index.values,
                                 columns=[self.variable_])
        
        x13_trend = DataFrame(self.x13_desaz.trend.values,
                                 index=self.data_endog.index.values,
                                 columns=[self.variable_])
        
        x13_irregular = DataFrame(self.x13_desaz.irregular.values,
                                 index=self.data_endog.index.values,
                                 columns=[self.variable_])
        
        # plot
        x13_original = ax[0].plot(self.data_endog,
                                 color=self.color1)
        
        ax[0].set_ylabel("original")
        
        x13_desazonal = ax[1].plot(x13_seasonal, color=self.color1)
        
        ax[1].set_ylabel("seas. adjusted")
        
        x13_trend = ax[2].plot(x13_trend, color=self.color1)
        
        ax[2].set_ylabel("trend")
        
        x13_irreg = ax[3].plot(x13_irregular, color=self.color1)
        
        ax[3].set_ylabel("irregular")
        
        ax[0].set_title("X13-ARIMA RESULTS")
        
        plt.tight_layout()
        plt.savefig(f'4_results/5_x13_results.jpg')
        
        return


    def x13_seasonal_adjustment(self):
        """
        X13 Seasonal adjustment (dependent variable).
        """
        
        fig, ax = plt.subplots(1, 1, sharex=False, figsize=( 12 , 6), dpi=300)
        
        x13_seasonal = DataFrame(self.x13_desaz.seasadj.values,
                                 index=self.data_endog.index.values,
                                 columns=[self.variable_])
        
        x13_seasonal_plot_raw = plt.plot(self.data_endog,
                                         color=self.color1,
                                         label="original")
        
        x13_seasonal_plot = plt.plot(x13_seasonal,
                                     color=self.color2,
                                     label="seasonal adjustment")
        
        plt.legend(loc=0)
        plt.title("X13-ARIMA SEASONAL ADJUSTMENT")
        plt.tight_layout()
        plt.savefig(f'4_results/6_x13_seasonal_adjustment.jpg')
        
        # new data frame
        x13_seasonal.to_csv("3_working/1_seasonal_adjustment.csv",
                               index_label="index_date", sep=",")
        
        return


    def independent_desaz_x13(self):
        """
        Deseasonalization of independent variables.
        """
        
        df_seas_raw = read_csv("3_working/1_seasonal_adjustment.csv", sep=",")
       
        list_exog_col = self.data_exogs.columns.to_list()
        
        for col in list_exog_col:
            exec_x13_independ = x13a(self.data_exogs[col], x12path=self.path)
            df_seas_raw[col] = exec_x13_independ.seasadj.values
        
        df_seas_raw.to_csv("3_working/1_seasonal_adjustment.csv", sep=",", index=False)
        
        return
    
