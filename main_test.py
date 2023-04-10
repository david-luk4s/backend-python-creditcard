"""Apply test for project"""

from datetime import date, datetime, timedelta
from application.card import CardSerializer

# Test for required fields cards

def test_should_fail_due_to_missing_exp_date():
    """this test should fail due to missing field exp_date"""
    body = b"""{
        "holder": "DVL",
        "number": "4539578763621486",
        "cvv": "123"
    }"""
    serializer = CardSerializer(body)
    assert serializer.is_valid() is False

def test_should_fail_due_to_missing_holder():
    """this test should fail due to missing field holder"""
    body = b"""{
        "exp_date": "02/2026",
        "number": "4539578763621486",
        "cvv": "123"
    }"""
    serializer = CardSerializer(body)
    assert serializer.is_valid() is False

def test_should_fail_due_to_missing_card_number():
    """this test should fail due to missing field card number"""
    body = b"""{
        "exp_date": "02/2026",
        "holder": "DVL",
        "cvv": "123"
    }"""
    serializer = CardSerializer(body)
    assert serializer.is_valid() is False

def test_must_not_fail_because_field_is_missing_cvv():
    """this test must not fail because the field is missing cvv"""
    body = b"""{
        "exp_date": "02/2026",
        "holder": "DVL",
        "number": "4539578763621486"
    }"""
    serializer = CardSerializer(body)
    assert serializer.is_valid() is True

# Test for length fields

def test_length_holder_less_or_equal_field():
    """If holder is less than or equal to 2 it must fail"""
    body = b"""{
        "exp_date": "12/2026",
        "holder": "DL",
        "number": "4539578763621486",
        "cvv": "123"
    }"""
    serializer = CardSerializer(body)
    assert serializer.is_valid() is False


# Test Format expire Date

def test_check_format_expire_date():
    """This test must fail due to an formart error date being passed."""

    data = {
        "exp_date": "12/02/2026",
        "holder": "DLS",
        "number": "4539578763621486",
        "cvv": "123"
    }
    serializer = CardSerializer(str(data).replace("\'", "\"").encode())
    assert serializer.is_valid() is False

# Test Expire Date

def test_check_expire_date():
    """This test must fail due to an expired date being passed."""
    today = date.today()
    date_expire = today - timedelta(days=today.day)

    data = {
        "exp_date": date_expire.strftime("%m/%Y"),
        "holder": "DLS",
        "number": "4539578763621486",
        "cvv": "123"
    }
    serializer = CardSerializer(str(data).replace("\'", "\"").encode())
    assert serializer.is_valid() is False

def test_check_not_expire_date_by_month():
    """This test must not fail because a valid date has been passed."""

    data = {
        "exp_date": date.today().strftime("%m/%Y"),
        "holder": "DLS",
        "number": "4539578763621486",
        "cvv": "123"
    }
    serializer = CardSerializer(str(data).replace("\'", "\"").encode())

    assert serializer.is_valid() is True

def test_check_not_expire_date_by_year():
    """This test must not fail because a valid date has been passed."""

    data = {
        "exp_date": "02/2026",
        "holder": "DLS",
        "number": "4539578763621486",
        "cvv": "123"
    }
    serializer = CardSerializer(str(data).replace("\'", "\"").encode())

    assert serializer.is_valid() is True

# Test cvv is valid case

def test_check_cvv_is_valid_if_passed():
    """Check cvv and validate if passed"""
    data = {
        "exp_date": "02/2026",
        "holder": "DLS",
        "number": "4539578763621486",
        "cvv": "12"
    }
    serializer = CardSerializer(str(data).replace("\'", "\"").encode())

    assert serializer.is_valid() is False

def test_check_cvv_is_valid_if_passed_with_length_reached():
    """Check cvv and validate if passed with length reached"""
    data = {
        "exp_date": "02/2026",
        "holder": "DLS",
        "number": "4539578763621486",
        "cvv": "12345"
    }
    serializer = CardSerializer(str(data).replace("\'", "\"").encode())

    assert serializer.is_valid() is False


# Test check card is valid with lib CreditCard

def test_check_card_is_valid_with_creditcard():
    """Check check card is valid with lib CreditCard"""
    data = {
        "exp_date": "02/2026",
        "holder": "DLS",
        "number": "0000000000000001",
        "cvv": "123"
    }
    serializer = CardSerializer(str(data).replace("\'", "\"").encode())
    assert serializer.is_valid() is False
