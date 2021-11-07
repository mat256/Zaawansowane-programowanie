lista = [4,3,2,6,4]

def double_list_values_v1(values):
    for a in range(len(values)):
        values[a]*=2
    return values

print(double_list_values_v1(lista))

lista = [4,3,2,6,4]


def double_list_values_v2(values):
    values=[a*2 for a in values]
    return values

print(double_list_values_v2(lista))
