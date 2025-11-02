In order to run our algorithm on an input file, only a Python 3 interpreter is required. We use only the standard library.
The `.swe` file must be given on stdin:

```sh
$ python3 ./sswe_group23.py < test01.swe
```

The first line of the output is either YES or NO, depending on whether there is a solution or not.
The next lines show the chosen expansion of each uppercase letter, e.g. `A --> b`.
The execution time is printed on stderr.
