# Mutable Default Arguments Bug in Python

This repository demonstrates a common, yet subtle, bug in Python related to mutable default arguments in functions.  The issue arises because mutable objects (like lists or dictionaries) used as default arguments are created only once when the function is defined, not each time it's called.  This can lead to unexpected and hard-to-debug behavior.

The `bug.py` file shows the problematic code. The `bugSolution.py` file offers a solution and explanation.

**How to reproduce:**
1. Clone this repository.
2. Run `bug.py` using a Python interpreter.
3. Observe the unexpected output and the explanation for the fix.