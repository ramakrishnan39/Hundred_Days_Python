travel_log = [
    {
        "country":"France",
        "visits":12,
        "cities":["Paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits": 5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    }
]

def add_new_country(ps_country,pi_num_visit,pl_cities):
    travel_log.append({"country":ps_country,"visits":pi_num_visit,"cities":pl_cities})
add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)

print("Welcome")
