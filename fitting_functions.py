def linear_fun(m, x, b):
    y = m * x + b
    return y

def slope_units(x_units, y_units):
    x_u = x_units.rstrip('s')
    y_u = y_units.rstrip('s')
    return f"{y_u}/{x_u}"

def print_equation(m, b, y_units, x_units):
        s_units = slope_units(x_units, y_units)
        print(f"the equation of the line is: y = {m}{s_units} x +{b}{y_units.rstrip('s')}")
    
