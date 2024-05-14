def state_executed(data):
    items = [payment for payment in data if payment.get("state") == "EXECUTED"]
    return items

def sort_operations(items):
    return sorted(items, key=lambda x: x.get("date"), reverse=True)


def output_format(item):
    date = item.get("date")
    desc = item.get("description")
    from_ = mask_from_to(item.get("from"))
    to = mask_from_to(item.get("to"))
    amo = item.get("operationAmount").get("amount")
    curr = item.get("operationAmount").get("currency").get("name")

    if from_:
        from_ += " -> "
    else:
        from_ = ""

    return (f'{raw_date(date)} {desc} \n{from_}{to}\n{amo} {curr}')


def raw_date(date):
    date_raw = date[0:10].split(sep="-")
    return f"{date_raw[2]}.{date_raw[1]}.{date_raw[0]}"

def mask_from_to(number):
    if number is None:
        return ""
    msg = number.split()

    if msg[0] == "Счет":
        number_hidden = mask_account(msg[-1])
    else:
        number_hidden = mask_card_number(msg[-1])
    return ' '.join(msg[:-1]) + '' + number_hidden
def mask_account(number):
    return f" **{number[-4:]}"

def mask_card_number(number):
    return f" {number[:4]} {number[4:6]}** **** {number[-4:]}"