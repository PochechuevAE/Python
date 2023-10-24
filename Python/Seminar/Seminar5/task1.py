def print_dict(some_dict: dict) -> str:
    if not isinstance(some_dict, dict):
        raise ValueError("На входе должен быть именно словарь!")
    res = ""
    for key, value in some_dict.items():
        res += f"{key} - {value}\n"
    return res



d = {"дядя Ваня": 849848948, "дядя Вася": 1111111}
sp = [88888, "Привет"]
try:
    print(print_dict(sp))
except:
    print("Что-то пошло не так")