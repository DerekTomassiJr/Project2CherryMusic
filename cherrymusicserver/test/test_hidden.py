from cherrymusicserver.cherrymodel import filter_hidden_files

name_1 = '.0hidden.txt'

name_2 = "._hidden.py"

name_3 = ".nothidden.txt"

name_4 = ".nothidden.py"


def test_hidden_files():

    assert not filter_hidden_files(name_1)

    assert not filter_hidden_files(name_2)

    assert filter_hidden_files(name_3)

    assert filter_hidden_files(name_4)


if __name__ == "__main__":
    test_hidden_files()
