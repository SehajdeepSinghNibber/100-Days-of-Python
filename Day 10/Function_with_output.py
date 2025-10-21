def format_name(f_name,l_name):
    formatted_f_name=f_name.title()
    formatted_l_name=l_name.title()
    return f"{formatted_f_name} {formatted_l_name}."

formated_string = format_name("angela","yu")
print(formated_string)
print(format_name("AnGela","YU"))
format_name("angela","yu")#will return nothing
