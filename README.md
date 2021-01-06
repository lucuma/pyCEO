<h1>
<img alt="pyceo" src="pyceo.png"> pyceo
</h1>

Pyceo is a Python package for creating beautiful, composable, and ridiculously good looking command-line-**user**-interfaces without having to write any extra code.

- Made for interfacing with humans.
- Arbitrary nesting and composition of commands.
- Automatic help page generation.
- No need to redeclare paramaters and options with decorators, just write Python methods.
- The help of a command is its docstring.


## Usage

Declare a class that inherits from `pyceo.Cli`. Every method/attribute that does not starts with an underscore will be a command.

```python
from pyceo import Cli

class Manage(Cli):
    def first_command(self, arg1, arg2=3):
        pass

    def second_command(self):
        pass

    def _not_a_command(self):
        pass
```

Then, instance that class and call it.

```python
cli = Manage()

if __name__ == "__main__":
    cli()
```

The class dosctring will be printed at the beginning of the help page.

### Subcommands

If an attribute is a subclass of `pyceo.Cli`, it will be a subcommand:

```python
from pyceo import Cli

class DBSub(Cli):
    def migrate(self):
        pass

class Manage(Cli):
    # A subcommand
    db = DBSub  # NOT `DBSub()`
```

### Context

You can pass any named argument as context to be used by your commands. This will be stored at the `_env` attribute.

Example:

```python
>>> cli = Manage(lorem="ipsum")
>>> print(cli._env)
{"lorem": "ipsum"}
```


## An example

![pyceo output](https://raw.githubusercontent.com/jpsca/pyceo/master/output.png)

This autogenerated help message is the result of running the example below:

```python
# example.py
from pyceo import Cli


class DBCli(Cli):
    """Database-related commands
    """

    def migrate(self, message):
        """Autogenerate a new revision file.

        This is an alias for "revision --autogenerate".

        Arguments:

        - message: Revision message

        """
        pass

    def branches(self):
        """Show all branches."""
        pass


class MyCli(Cli):
    """Welcome to PyCeo 3
    """

    def new(self, path, quiet=False):
        """Creates a new Proper application at `path`.

        Arguments:

        - path: Where to create the new application.
        - quiet [False]: Supress all output.
        """
        pass

    def hello(count, name):
        """Simple program that greets NAME for a total of COUNT times."""
        pass

    # A subcommand!
    db = DBCli


cli = MyCli()

if __name__ == "__main__":
    cli()

```


## Helpers

Beyond the CLI builder, pyceo also includes some commonly-used helper functions

### `confirm(question, default=False, yes_choices=YES_CHOICES, no_choices=NO_CHOICES)`

Ask a yes/no question via and return their answer.

### `ask(question, default=None, alternatives=None)`

Ask a question via input() and return their answer.

### `echo(text)`

Renders a text (possibly decorated with pyceo markup) to the terminal.


## Markup system

Pyceo uses a simple markup system for producing colored terminal text. Any text between a tag is printed with its style, and you can combine styles by using nested brightness, foreground, and background tags (only one for each category).

### Brightness

- `<op:bright> ... </op>`
-  `<op:dim> ... </op>`

### Foreground color

- `<fg:COLOR> ... </fg>`

Possible colors are `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `lblack`, `lred`, `lgreen`, `lyellow`, `lblue`, `lmagenta`, `lcyan`, and `lwhite`.

### Background color

- `<bg:COLOR> ... </bg>`

Possible colors are `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `lblack`, `lred`, `lgreen`, `lyellow`, `lblue`, `lmagenta`, `lcyan`, and `lwhite`,


## FAQ

### Why don't just use optparse or argparse?

Are you kidding? Because this is way easier to use and understand.

### Why don't just use click?

Because this looks better and is easier to use and understand.

### Why don't just use...?

Because this library fits better my mental model. I hope it matches yours as well.
