from datetime import datetime
from pmdarima.arima import auto_arima
from pandas import DataFrame
from pandas import read_csv
from statsmodels.tsa.statespace.sarimax import SARIMAX
from matplotlib import pyplot as plt
from matplotlib.pyplot import fill_between
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from sklearn.metrics import r2_score
from numpy import arange


class Model_execute:
    """
    Class responsible for estimating the model.
    Required settings:
    - data (input data)
    - variable (formatted dependent variable - "NAME VARIABLE")
    
    Optional settings:
    - style (graphic style)
    - color1 (color setting)
    - color2 (color setting)
    - color3 (color setting)
    - color4 (color setting)
    - color5 (color setting)
     
    Syntax: Model_execute(data, variable, style_graph,
                                          color1, color2, color3, color4, color5)
    """

    def __init__(self, data, variable, 
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
            self.data_endog = data.iloc[ : , 0 : 1 ]
            self.data_exogs = data.iloc[ : , 1 :   ]
            
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


    def auto_arima(self, s):
        """
        Function that uses auto arima to find the best parameters for the model.
        """
        
        # Best model with auto arima
        model_select = auto_arima(self.data_endog,
                                  seasonal=True,
                                  error_action="ignore",
                                  supress_warnings=True,
                                  trace=False)
        
        # Data frame
        model_select = str(model_select)
        paramet = [datetime.now(),
                   int(model_select[7]),
                   int(model_select[9]),
                   int(model_select[11]),
                   int(model_select[14]),
                   int(model_select[16]),
                   int(model_select[18])]
        
        df_paramet = DataFrame(paramet).T
        
        df_paramet.columns=["time", "p", "d", "q", "P", "D", "Q"]
        
        df_paramet["s"] = s
        
        df_paramet.to_csv("3_working/auto_arima_parameters.csv",
                          decimal=".",
                          sep=",",
                          index=False)
        
        return


    def model_execute(self, p, d, q, P, D, Q, s):
        """
        Model estimation.
        
        p = Order of the AR term
        q = Order of the MA term
        d = Number of differencing required to make the time series stationary
        P = Seasonal order of the AR term
        D = Seasonal order of the MA term
        Q = Seasonal difference number
        """
        
        model = SARIMAX(endog=self.data_endog,
                        exog=self.data_exogs,
                        order=(p, d, q), 
                        seasonal_order=(P, D, Q, s), 
                        trend="c")
        
        self.model_fit = model.fit(disp=False)
        model_result = self.model_fit.summary()
        
        with open('4_results/9_model_summary.txt', 'w') as desc_stat:
            desc_stat.write(str(model_result))
        
        return


    def acf_pacf_residuals(self):
        """
        Residuals ACF and PACF.
        """
        
        fig, ax = plt.subplots(2, 1, sharex=False, figsize=( 12 , 6), dpi=300)
        
        resid = DataFrame(self.model_fit.resid, columns=[f"{self.variable}"])
        
        acf = plot_acf(resid.values.squeeze(),
                            lags = len(resid) / 3,
                            use_vlines = True,
                            title = f"{self.variable} - ACF (RESIDUALS)",
                            color = self.color1,
                            vlines_kwargs = {"colors": self.color1},
                            alpha=0.05,
                            zero=False,
                            ax=ax[0])
        
        pacf = plot_pacf(resid.values.squeeze(),
                            lags = len(resid) / 3,
                            use_vlines = True,
                            title = f"{self.variable} - PACF (RESIDUALS)",
                            color = self.color2,
                            vlines_kwargs = {"colors": self.color2},
                            alpha=0.05,
                            zero=False, 
                            ax=ax[1])
        
        ax[0].set_ylim(-0.4, 0.4)
        ax[1].set_ylim(-0.4, 0.4)
        plt.tight_layout()
        
        plt.savefig(f"4_results/10_residuals (acf and pacf).jpg")
        
        return


    def residuals_analysis(self):
        """
        Analysis of model residuals.
        """
        
        fig, ax = plt.subplots(1, 1, sharex=True, dpi=300)
        plt.rcParams.update({'font.size': 12})
        plt.style.use(self.style_graph)
        
        resid = DataFrame(self.model_fit.resid, columns=[f"{self.variable}"])
        
        resid_plot_fd = resid.hist(color=self.color2,
                                   legend=False,
                                   density=True,
                                   figsize=(12, 6))
        
        plt.title(f"{self.variable.upper()} - RESIDUALS")
        
        plt.tight_layout()
        
        plt.savefig(f"4_results/11_residuals (frequency distribution).jpg")
        
        return


    def ts_residuals_plot(self):
        """
        Residuals time serie plot.
        """
        
        resid = DataFrame(self.model_fit.resid, columns=[f"{self.variable}"])
        
        fig, ax = plt.subplots(1, 1, sharex=False, figsize=( 12 , 6), dpi=300)
        
        resid_plot = resid.plot(title=f"RESIDUALS - {self.variable}",
                                color=self.color2,			
                                legend=False,
                                xlabel="",
                                ylabel="")
        
        plt.tight_layout()
        resid_plot.figure.savefig(f"4_results/12_residuals (time serie).jpg")
        
        return


    def adjust_predict(self):
        """
        Effective x fitted + predict plot.
        """
        
        # plot config
        fig, ax = plt.subplots(1, 1, sharex=True, figsize=( 12 , 6), dpi=300)
        plt.rcParams.update({'font.size': 12})
        plt.style.use(self.style_graph)
        
        # fit model
        init_fitted = 24
        self.data_endog[f"{self.variable_}_fitted"] = self.model_fit.predict(start=init_fitted,
                                                                             dynamic=False)
        
        self.data_endog.to_csv("3_working/3_data_base_fitted.csv", sep=",")
        
        # plot observed
        effective = self.data_endog.iloc[ : , 0 ].plot(title=f"{self.variable}",
                                                        xlabel="",
                                                        ylabel="",
                                                        color=self.color1,
                                                        figsize=(12, 6))
        
        # plot fitted
        adjustment = self.data_endog.iloc[ : , 1 ].plot(xlabel="",
                                                        ylabel="",
                                                        color=self.color2)
        
        # r-squared
        r2_fit = init_fitted - len(self.data_endog)
        r2 = r2_score(self.data_endog.iloc[ r2_fit : -1 , 0 ],
                      self.data_endog.iloc[ r2_fit : -1 , 1 ])
        
        plt.legend(["observed",
                    f"fitted model (R² = {r2:.2f}%)"])
        
        # forecast
        #forecast = self.model_fit.get_forecast(12)

        # predict
        #predict = forecast.predicted_mean
        
        
        
        # save
        plt.tight_layout()
        plt.savefig(f"4_results/13_observed_fitted_predict.jpg")
        
        return

