import pytest


@pytest.fixture
def smtp_connection():
    import smtplib
    connection = smtplib.SMTP_SSL("smtp.163.com", 465, timeout=5)
    yield connection
    print("teardown smtp")
    connection.close()


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0
