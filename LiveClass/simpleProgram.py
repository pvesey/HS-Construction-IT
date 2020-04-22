# number for employee: Use a Dictionary:  key value pair:
employee_lookup = {
"emp001": ("Paul Vesey", "20-12-2020", "Scaff Inspector", "Holiday Info"),
"emp002": ("Joe Blogs", "20-12-2021", "Scaff Inspector"),
"emp003": ("Alice Wonderland", "20-12-2021", "Scaff Inspector"),
"emp004": ("Bobb Buffer", "20-12-2021", "Scaff Inspector"),
"emp005": ("Jane Doe", "20-12-2022", "Scaff Inspector")
}

scaff_checks = [
("10-2-20", "Scaffolding Check", True, employee_lookup["emp001"][0]),
("17-2-20", "Scaffolding Check", False, employee_lookup["emp002"][0]),
("22-2-20", "Scaffolding Check", True, employee_lookup["emp003"][0])
]

count_of_pass = 0

for scaff_check in scaff_checks:
    print(scaff_check)
    if(scaff_check[2]):
        count_of_pass = count_of_pass + 1

print(count_of_pass)
