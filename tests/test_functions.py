from functions import raw_date, mask_account, mask_card_number, mask_from_to

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