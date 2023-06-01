This repo is a sample skeleton of a command-line tool in Python with subcommands.

## Getting Started

1. Install dev dependencies.
```
pip install '.[quality]'
```

2. Install the current package as an editable package.
```
pip install -e .
```

3. Run the command line tool and experiment.
```
sample_cli --help
```

## Developing

Run the following commands on your code before committing.

```
mypy . \
  && black . \
  && ruff . --fix
```
