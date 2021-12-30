from data_input import data_endog, data_exogs

# variables {
# =============================================================================

variable_ = list(data_endog.columns.values.tolist())[0]
variable = variable_.replace("_", ' ').upper()

# x13 arima path
path_x13_arima = "C:/Program Files (x86)/x13as/0_x13as"

# p-value
p_value_accepted = 0.05

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
