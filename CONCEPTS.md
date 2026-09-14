# Concepts — In My Own Words

## Which PE2 module does each file draw on, and how?

- **models.py (Module 3)** — Describes the classes `Student` and `HonoursStudent`. In addition to a shared class variable called "total_students," which increases each time a new student is created, `Student` contains instance variables called "name," "student_id," and "score" that are set in `__init__`. Inheriting from `Student`, `HonoursStudent` overrides `get_grade()` to add an honours-level distinction band and uses `super().__init__()` to reuse the parent's setup.

- **data_tools.py (Modules 2 & 4)** — To read and write files safely, use `open(...)` inside of `with` blocks (they automatically close even if something goes wrong). The Module 2 string-cleaning process is applied by `load_and_clean_records()`. `.strip()` eliminates stray spaces, `.title()`/`.upper()` corrects uneven capitalization, and `int()` turns the score text into a real number.

- **analytics.py (Modules 1 & 4)** — As a generator, `filter_students()` uses `yield` to return one matching student at a time rather than creating and returning an entire list. Because it produces an inner `grade` function that maintains access to `pass_mark` even after `make_grader()` has completed its execution, it is a closure. Instead of utilizing a `for` loop, `iterate_scores()` demonstrates manual iteration with `iter()` and `next()`.

- **reporting.py (Modules 1 & 4)** — The operating system, Python version, working directory, and existence of the data file are reported using `platform` and `os`. reports the current date, a timestamp, whether the year is a leap year, the number of days in the current month, and (optionally) the number of days left till a user-specified date using `datetime` and `calendar`.

- **main.py (All modules + Module 1)** — Instead of having its own logic, it imports classes and functions from every other file (for example, `from models import Student`). In order to prevent the application from crashing due to incorrect input, it is mostly a `while True` menu loop with `try/except` surrounding each time a number is read from the user.
## Why is splitting the program across several files better than one big file?

Every file has a single, distinct function: `models.py` only specifies what a student *is*, `data_tools.py` only manages files, and `analytics.py` only does computations. This makes each component easier to test independently (I tested the functions of `analytics.py`'s functions directly in the terminal before ever touching `main.py`), easier to locate later, and easier to reuse. For example, I could import `models.py` and `analytics.py` without dragging the menu code with them if I wanted a second program that used students without the menu.
## A class vs an object

The class is called `Student`; it is the *blueprint* that specifies that each student will have a `name`, `student_id`, `score`, and a `get_grade()` method. One *object*—a real student according to the blueprint with its own unique values—is created when I write `Student ("Lisa", "S1", 72)`. I can create as many independent objects from a single class as I wish.

## A generator vs a normal function

A normal function completes its execution after returning a single result. Because it employs `yield` rather than `return`, `filter_students()` is a generator. Each time it yields, it pauses and returns one value, knowing precisely where it left off so that it may pick up where it left off the next time it's asked for another value. This implies that it can generate pupils one at a time without ever having to commit the entire list to memory beforehand.

## A closure

It defines and returns an inner function (`grade`) that maintains a reference to `pass_mark` from the scope of the outer function—even after `make_grader()` has completed running—`make_grader(pass_mark)` is a closure. Thus, two distinct grading functions, each "remembering" a distinct pass mark indefinitely, are produced by `make_grader(50)` and `make_grader(75)`.

## 'w' vs 'a' file modes

Before adding new material, `'w'` (write mode) opens a file and removes any existing content. I use this for `data/students.txt` and `data/report.txt`, as each should only represent the most recent run. I use `'a'` (append mode) for `data/activity.log` to add fresh stuff to the end of the file without affecting what's already there. This way, every action taken over the entire session accumulates in a single continuous history rather of being erased each time.

## What was the hardest part of combining four modules into one program, and how did you solve it?

Maintaining a thin `main.py` was the most challenging aspect. Although it was tempting to incorporate logic straight into the menu selections, doing so would have negated the purpose of separating the modules. In order to solve it, I made sure that each menu option was only one or two lines that called a function that I had previously written and tested separately in `analytics.py`, `data_tools.py`, or `reporting.py`; as a result, almost all of the menu loop and input handling were contained in `main.py`, with the actual work taking place in the other files.