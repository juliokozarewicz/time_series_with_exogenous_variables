
# variables {
# =============================================================================

# date filter {
# --------------------------------------------------------------------------
date_train_init = "2010-01"
date_train_end = "2020-12"

date_predict_init = date_train_end
date_predict_end = "2022-01"

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
# --------------------------------------------------------------------------
p = 1 #1
d = 0 #1
q = 1 #1
P = 0 #1
D = 0 #1
Q = 0 #1

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
color2 = "red"
color3 = "darkorange"
color4 = "black"
color5 = "red"

# =============================================================================
# }
