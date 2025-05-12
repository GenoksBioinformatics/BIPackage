# BIPackage
Handles basic bioinformatics operations with a python package structure


## INSTALLATION

```shell
pip install bipackage
```

## USAGE

```shell
bip <subcommand> [params]
```

Note that `params` are the parameters for the __subcommand__.

## TAB AUTOCOMPLETION

To enable tab autocompletion, run the following command:

bashrc
run bip once and restart the shell
```shell
bip
```

add to zshrc
```shell
autoload -U bashcompinit
bashcompinit
eval "$(register-python-argcomplete bip)"
```

This will enable tab autocompletion for the `bip` command.