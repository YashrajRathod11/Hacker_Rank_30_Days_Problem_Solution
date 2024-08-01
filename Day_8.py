def create():
    input_s = input()
    pair = input_s.split()
    name_dict = {}
    for p in pair:
        name, number = p.split()
        name_dict[name.strip()] = int(number.strip())        
    return name_dict


n = int(input())
output = create()
print(output)