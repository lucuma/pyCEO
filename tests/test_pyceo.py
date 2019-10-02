import sys

from pyceo import Manager, param, option


def test_intro_in_help(capsys):
    intro = "This is my intro"
    cli = Manager(intro)

    sys.argv = ["manage.py", "help"]
    cli.run()

    captured = capsys.readouterr()
    print(captured.out)
    assert intro in captured.out


def test_error_too_many_args(capsys):
    cli = Manager()

    @cli.command()
    def hello():
        pass

    sys.argv = ["manage.py", "hello", "world"]
    cli.run()

    captured = capsys.readouterr()
    print(captured.out)
    assert "Too many arguments" in captured.out


def test_error_missing_args(capsys):
    cli = Manager()

    @cli.command()
    @param("path")
    def hello(path="/"):
        pass

    sys.argv = ["manage.py", "hello"]
    cli.run()

    captured = capsys.readouterr()
    print(captured.out)
    assert "Missing arguments" in captured.out


def test_error_wrong_option_type(capsys):
    cli = Manager()

    @cli.command()
    @option("port", type=int)
    def hello(port=1):
        pass

    sys.argv = ["manage.py", "hello", "--port", "world"]
    cli.run()

    captured = capsys.readouterr()
    print(captured.out)
    assert "Wrong argument for `port`" in captured.out


def test_type_option(capsys):
    cli = Manager()

    @cli.command()
    @option("port", type=int)
    def hello(port=1):
        print(f"Port is {type(port)}")

    sys.argv = ["manage.py", "hello", "--port", "123"]
    cli.run()

    captured = capsys.readouterr()
    print(captured.out)
    assert "Port is <class 'int'>" in captured.out
    assert "Port is <class 'str'>" not in captured.out
