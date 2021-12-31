from data_input import data_endog, data_exogs

# variables {
# =============================================================================

variable_ = list(data_endog.columns.values.tolist())[0]
variable = variable_.replace("_", ' ').upper()

# x13 arima path
#path_x13_arima = "/home/edu/x13as/"
path_x13_arima = "C:/Program Files (x86)/x13as/0_x13as"

# p-value
p_value_accepted = 0.05

# set parameters manually {
# --------------------------------------------------------------------------
p = 1 #1
d = 1 #1
q = 1 #1
P = 1 #1
D = 1 #1
Q = 1 #1

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
