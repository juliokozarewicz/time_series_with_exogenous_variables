
# variables {
# =============================================================================

# date filter {
# --------------------------------------------------------------------------
date_train_init = "2000-01"
date_train_end = "2021-11"

date_predict_init = date_train_end
date_predict_end = "2022-11"

# amount of extra data in the independent variables
fore_period = 12
# --------------------------------------------------------------------------
#   }

# x13 arima path
#path_x13_arima = "/home/edu/x13as/"
path_x13_arima = "C:/Program Files (x86)/x13as/0_x13as"

# p-value
p_value_accepted = 0.05

# set parameters manually {
# --------------------------------------------------------------------------3p = 1 #1
p = 2 #2
d = 0 #0
q = 1 #1
P = 0 #0
D = 0 #0
Q = 0 #0

# inform the periodicity of the series (D=365, M=12, Y=1)
s = 12
# --------------------------------------------------------------------------
#   }

# =============================================================================
# }

# style {
# =============================================================================

style_graph = "seaborn"
color1 = "royalblue"
color2 = "indigo"
color3 = "darkorange"
color4 = "black"
color5 = "red"

# =============================================================================
# }
