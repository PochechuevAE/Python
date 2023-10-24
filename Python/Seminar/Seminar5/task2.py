def get_symb (some_str: str) -> str:
    result = "" 
    input_str = some_str.split()
    count_dict = {}
    
    for item in input_str:
        if item in count_dict:
            count_dict[item] += 1
            result += f"{item}_{count_dict[item]} "
        else:
            count_dict[item] = 0
            result += f"{item} "
            
    return result.strip()



test_str = "a a a b c a a d c d d"
print(get_symb(test_str))

