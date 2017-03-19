# Lidando com exceptions

Algumas Exceptions nativas (https://docs.python.org/2/library/exceptions.html)

```python
# SyntaxError Wrong written code
# fav_number = int(in put('What is your favorite number?\n'))

# ValueError: Code waiting for a number, but user inserted a string

# ZeroDivisionError: Raised when the second argument of a division or modulo operation is zero
```


## Lidando com erros

```python
# Run the code over and over again, until the user inserts a number correctly
# If a number is inserted correctly break from the loop
while True:
    try:
        fav_number = int(input('What is your favorite number?\n'))
        print(18 / fav_number)
        break
    except ValueError:
        print('The input must be a number')
    except ZeroDivisionError:
        print('Don\'t pick zero')

    # To handle All exceptions
    except:
        print('Some unknown error')

    # Execute this line of code no matter what.
    # It occurs every single time in the loop
    finally:
        print('loop completed')
```
