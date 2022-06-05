# Написать функцию провреки "Силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов то вернуть Too Weak
# - если пароль содержит только цифры , только строчные, только заглавные то вернуть Weak
# - если пароль содержит символы любых 2 наборов вернуть Good
# - если пароль содержит символы любых 3 наборов вернуть Very Good

import string


def password_strength(value: str) -> str:
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    if len(value) < 8:
        return 'Too Weak'
    # если все буквы в value содержат digits или lowers или uppers
    if all(e in digits for e in value) or all(e in lowers for e in value) or all(e in uppers for e in value):
        return 'Weak'
    if any(e in digits for e in value) and any(e in lowers for e in value) and any(e in uppers for e in value):
        return 'Very Good'
    if (any(e in digits for e in value) and any(e in lowers for e in value)) or (
            any(e in digits for e in value) and any(e in uppers for e in value)) or (
            any(e in lowers for e in value) and any(e in uppers for e in value)):
        return 'Good'



if __name__ == '__main__':
    assert password_strength('') == 'Too Weak'
    assert password_strength('1234567') == 'Too Weak'
    assert password_strength('asdewe') == 'Too Weak'
    assert password_strength('QAZXDDF') == 'Too Weak'
    assert password_strength('QAzX1D5') == 'Too Weak'
    assert password_strength('12345678') == 'Weak'
    assert password_strength('1333332345678') == 'Weak'
    assert password_strength('asdfghjk') == 'Weak'
    assert password_strength('asdasdgdfghjk') == 'Weak'
    assert password_strength('ASDFGHJK') == 'Weak'
    assert password_strength('1234asdf') == 'Good'
    assert password_strength('1234ASDF') == 'Good'
    assert password_strength('asdfASDF') == 'Good'
    assert password_strength('asdfdasdfASDF') == 'Good'
    assert password_strength('12asdDGN') == 'Very Good'
    assert password_strength('DBNMasddsad321') == 'Very Good'
    assert password_strength('123NRJDKdngjd') == 'Very Good'
