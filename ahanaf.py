def sqrt(number: float):
    ans = number ** 0.5
    return ans


def happyBirthday(name: str):
    r = 'Happy Birthday! Dear {}!. May ALLAH bless you.'
    abcd = r.format(name)
    print(abcd)


def list_printer(name: list):
    for i in range(0, len(name)):
        print(name[i].text)