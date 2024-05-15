from functions import raw_date, mask_account, mask_card_number, mask_from_to, output_format

def test_raw_date():
    assert raw_date("2019-08-26T10:50:58.294041") == "26.08.2019"

def test_mask_account():
    assert mask_account("64686473678894779589") == " **9589"

def test_mask_card_number():
    assert mask_card_number("1596837868705199") == " 1596 83** **** 5199"

def test_mask_from_to():
    assert mask_from_to("Счет 64686473678894779589") == "Счет **9589"
    assert mask_from_to(None) == ""
    assert mask_from_to("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_output_format():
    item = {
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {
      "amount": "97853.86",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612"
  }
    assert output_format(item) == "13.07.2019 Перевод с карты на счет \n""Maestro 1308 79** **** 7170 -> Счет **8612\n"\
    "97853.86 руб."

def test_output_format_1():
    item =   {
    "id": 207126257,
    "state": "EXECUTED",
    "date": "2019-07-15T11:47:40.496961",
    "operationAmount": {
      "amount": "92688.46",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 35737585785074382265"
  }
    assert output_format(item) == """15.07.2019 Открытие вклада \nСчет **2265\n92688.46 USD"""