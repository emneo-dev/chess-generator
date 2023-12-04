# Chess board generator

Chess board generator for Epitech students

The code is absolutely terrible but at least it works

The board can not be a classical board (As in there can be moments where a
side has 14 pawns for example), but it shouldn't matter for the neural network
project.

## Output formating

Each line is composed of a simplified FEN notation (It only gives the board and
who is next to play), followed by 3 characters specifying if the given board is
in a stalemate, a check, or a checkmate.

## Notes

 - On lines with a checkmate there will always be a check.
 - Stalemates are fairly rare -> Do a PR if you want to change that :)

## How to launch

Don't forget to install the one dependency this script needs!

```sh
$ ./generator.py nb_moves_to_generate
```

For example if you want to generate 10 million positions directly in a
compressed format you can do this:

```sh
$ ./generator.py 10_000_000 | gzip -c - > dataset.gz
```
