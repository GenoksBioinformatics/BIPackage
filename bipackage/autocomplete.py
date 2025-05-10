import sys

# find the operating system
if sys.platform.startswith("linux"):
    print("Linux")
elif sys.platform.startswith("win"):
    print("Windows")
elif sys.platform.startswith("darwin"):
    print("MacOS")
else:
    print("Unknown OS")


def _tab_autocomplete_mac():
    """Tab autocomplete for macOS."""
    command = ""
    command += "autoload -U bashcompinit"
    command += "bashcompinit"
    command += 'eval "$(register-python-argcomplete bip)"'


def _tab_autocomplete_linux():
    """Tab autocomplete for Linux."""
    command = 'eval "$(register-python-argcomplete bip)"'
