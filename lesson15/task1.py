# Создайте метод класса с именем `validate`, который должен вызываться из метода` __init__`
# для проверки электронной почты параметра, переданного конструктору.
# Логика внутри метода `validate` может состоять в том,
# чтобы проверить, является ли переданный параметр электронной почты допустимой строкой электронной почты.

class Mail:
    MAIL = ['mail.ru', 'gmail.com', 'bk.ru', 'yandex.ru']
    SYMBOLS = "/.,?!@#$%^&*()-+=~`|'"

    def __init__(self, email: str):
        self.email = email
        Mail.validate(email)

    @classmethod
    def validate(cls, email):
        if email.count('@') != 1:
            return False, 'Invalid Syntax @!'
        [prefix, domain] = email.split('@')
        if domain not in cls.MAIL or domain.count('.') != 1:  # проверка домена
            for el in cls.SYMBOLS:
                if el in prefix or prefix[0] in cls.SYMBOLS or prefix[-1] in cls.SYMBOLS:  # проверка логина
                    return False, 'Invalid Syntax!'
        return email


if __name__ == '__main__':
    mail = input('Insert your mail: ')
    m = Mail(mail)
    print(m.validate(m.email))
