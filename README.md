# Week 6 Assignment: Times Tables, Skip Counting & Loop Hospital

This repository contains my Week 6 Python assignment on `range()` and loop debugging.

## Files

- `times_table.py` — Asks the user for a number and prints its times table from 1 to 10 using a `for` loop and f-strings.
- `skip_counter.py` — Uses `range()` with a step to print even numbers from 0 to 20, and a negative step to count down from 10 to 0.
- `loop_hospital.py` — Contains three buggy loops that have been fixed, each with a `# FIXED:` comment explaining the bug.

## Reflection

An off-by-one error happens when a loop runs one time too many or one time too few — usually because of a wrong `range()` boundary, like using `range(1, 10)` when you actually need numbers up to and including 10. A good habit to avoid this is remembering that `range(start, stop)` never includes `stop`, so if you want a number included, the `stop` value should be one more than it.