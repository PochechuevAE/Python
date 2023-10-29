""" 
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1

"""

def change_max_on_min(scores_list: list, ind: int):
    max_score = max(scores_list)
    min_score = min(scores_list)
   
    
    if ind == len(scores_list):
        return scores_list
    if scores_list[ind] == max_score:
        scores_list[ind] = min_score
    change_max_on_min(scores_list, ind + 1)
    
    


input_list = [1, 3, 5, 3, 4]
print(input_list)
change_max_on_min(input_list, 0)
print(input_list)

