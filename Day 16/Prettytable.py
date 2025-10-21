from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name", "Age", "City"]

table.add_row(["Alice", 25, "New York"])
table.add_row(["Bob", 30, "San Francisco"])
table.add_row(["Charlie", 22, "Los Angeles"])

table.add_row(["-"*5, "-"*3, "-"*11])
table.add_row(["Total", "3", ""])

print(table)