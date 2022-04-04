def format_names(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""
    if (f_name == '' or l_name == ''):
        return f"You didn't provide any input."
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"


print(format_names(
    input("Enter the first name: "),
    input("Enter the last name: ")))
