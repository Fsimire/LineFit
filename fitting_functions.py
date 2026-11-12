

def linear(m,x,b):
    y= m* x + b
    return y
def slope_units(x_units,y_units):
    meters= x_units.rstrip('s')
    kg= y_units.rstrip('s')
    return kg+"/"+meters
def print_equations(m,b,x_units,y_units):
    print("The equation of the line is: y=", m,slope_units(x_units,y_units),"x +", b,y_units)
    
