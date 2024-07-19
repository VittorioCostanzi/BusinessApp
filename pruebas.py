def str_int(variable_var):
    try:
        valor = int(variable_var)
    except:
        valor = str(variable_var)
    return valor

print(type(str_int("holis")), str_int("holis"))
print(type(str_int("64")), str_int("64"))