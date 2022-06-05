# Написать функцию провреки "Силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов то вернуть Too Weak
# - если пароль содержит только цифры , только строчные, только заглавные то вернуть Weak
# - если пароль содержит символы любых 2 наборов вернуть Good
# - если пароль содержит символы любых 3 наборов вернуть Very Good

import string


def password_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = lowers.upper()
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue
    if count == 3:
        return 'Very Good'
    return 'Weak' if count == 1 else 'Good'



# Есть счетчик пароля count. Если он 1 то возвращаем что слабый, если 3 (значит что все три символа там присутствуют)
# то возвращаем очень хороший, в остальных случаях хороший

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
    assert password_strength('123asdDGNnI') == 'Very Good'
    assert password_strength('1234567Zz') == 'Very Good'
    assert password_strength('asdfghhjC2') == 'Very Good'
    assert password_strength('ASDDFGBG1a') == 'Very Good'
