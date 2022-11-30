import urwid


def is_very_long(word):
    return len(word) > 12


def has_digit(word):
    return any(char.isdigit() for char in word)


def has_letters(word):
    return any(char.isalpha() for char in word)


def has_upper_letters(word):
    return any(char.isupper() for char in word)


def has_lower_letters(word):
    return any(char.islower() for char in word)


def has_symbols(word):
    return any(not char.isalpha() and not char.isdigit() for char in word)


def get_score(password):
    functions = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    score = 0
    for function in functions:
        if function(password):
            score += 2
    return score


def on_ask_change(edit, password, reply):
    reply.set_text(f"Рейтинг этого пароля: {get_score(password)}")


def main():
    reply = urwid.Text("")
    ask = urwid.Edit('Введите пароль: ', mask='*')
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change, reply)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    main()
