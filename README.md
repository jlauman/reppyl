# reppyl
A Python REPL development experience.

Enjoy a REPL-like experience with a split terminal. For example,
the Helix editor open in the left pane and `./repl.sh` running in
the right pane.

The read-eval-print-loop development experience is:
* Edit and save a `src` Python file and the REPL will load it.
* Run a function in the Python REPL to manually test.
* Copy the file into a package folder (with an `__init__.py` file).
* Add a test file and have pytest run it on every save.

Use the `if __name__ == "__main__":` pattern to control what is
run when a Python file is reloaded by the REPL. See the
`some_code.py` file for how pytest is triggered when a package
file is saved.
