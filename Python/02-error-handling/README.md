# Password Generator

## Overview
A simple password generator that creates random passwords following these criteria:
- Minimum of 4 characters
- At least 1 number, 1 letter and 1 special character per password

The main goal of this program was to practice error handling using the full `try/except/else/finally` structure, and to use the `string` and `secrets` modules for the first time.

## Tools
- **Language:** Python
- **Libraries:**
  - `string`: provides the character sets (digits, letters and punctuation) used to build the passwords.
  - `secrets`: randomly chooses the characters with `secrets.choice()` and shuffles them with `secrets.SystemRandom().shuffle()`.
  - `IPython.display`: `clear_output()` keeps the screen clean between attempts.

## What Was Done
1. Imported the libraries.
2. Created a custom exception, `MinimumCharsError`.
3. Created the `generate_password()` function, which:
   1. Starts an empty list for the password;
   2. Gets and stores the required characters;
   3. Selects one character from each required group, then fills the remaining length with random characters;
   4. Shuffles the characters;
   5. Joins them into a string.
4. Created a `while` loop that requests and validates the user's input using `try/except/else/finally`. The program handles two errors: length too short and length not an integer. If no error occurs, the password is generated and printed. In every case, whether an error occurred or not, the total number of attempts is counted.

## How to Run
This program uses `clear_output` from IPython, so it must be run in a Jupyter environment (Jupyter Notebook, JupyterLab or VS Code). Open `password-generator.ipynb` and run the cell.

## Output
```
The generated password is: 4^6KM
A total of 5 attempts were made...
```

## What I Learned
- How to handle specific errors, not only by using `except`, but also by choosing which types of errors to expect and in what order.
- How to create my own exception, which is useful for specific situations such as the minimum number of characters.
- What each block of `try/except/else/finally` is for, including that `finally` runs in every case.