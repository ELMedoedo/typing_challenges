from constants import ___
from typing import TypedDict, List

def calculate_total_spent_for_user(user: TypedDict('user', {'name': str, 'age': int, 'transactions_sums': List[int]})) -> int:
    return sum(user["transactions_sums"])

# не уверен в решении. по методичкам это решение должно работать на версии 3.12. 
#  Так же на хабре: https://habr.com/ru/companies/otus/articles/888974/
# советуют сделать классю Вот такой: 
# class User(TypedDict):
#     name: str
#     age: int
#     transactions_sums: List[int]


if __name__ == "__main__":
    assert calculate_total_spent_for_user(
        user={
            "name": "Ilya",
            "age": 32,
            "transactions_sums": [102, 15, 63, 12],
        },
    ) == 192
