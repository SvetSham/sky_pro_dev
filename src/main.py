import processing
import widget

print(widget.mask_account_card("Maestro 1596837868705199"))
print(widget.mask_account_card("Счет 64686473678894779589"))
print(widget.mask_account_card("MasterCard 7158300734726758"))
print(widget.mask_account_card("Счет 35383033474447895560"))
print(widget.mask_account_card("Visa Classic 6831982476737658"))
print(widget.mask_account_card("Visa Platinum 8990922113665229"))
print(widget.mask_account_card("Visa Gold 5999414228426353"))
print(widget.mask_account_card("Счет 73654108430135874305"))

print(widget.get_date("2024-03-11T02:26:18.671407"))

transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(processing.filter_by_state(transactions))
print(processing.filter_by_state(transactions, "CANCELED"))
