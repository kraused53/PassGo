# PassGo
A python-based password generator written for UofL's CSE 350 -> Summer 2026

---

This is the repo for PassGo, our CSE 350 project

I have added a basic program skeleton to illustrate how to link python files together as usable libraries, and how 
to add standard doc-strings to functions. Once the program is further along, we should change this README to 
something more interesting

---
### The Basic Idea

I think that the easiest way to keep everything straight while building this project will be to group like functions 
together into files: all GUI functions go together, all pass word functions go together ...

This will make it easier to document in the report and to know where to look when testing / updating functionality.

# DO NOT DO WORK ON THE MAIN BRANCH!!!

When you are working on a new module for the project, make a new branch to test it out. Once you know it works and does
not break the work someone else has done, then you can merge it to the main branch.

---
### Doc Strings

If we add comments like this to each function it will make it a lot easier to understand each-other's work.  If you are 
using PyCharm, adding 3x " on the line under a function header should auto-generate a doc-string outline for you to 
fill out


### Type safety

Also, I think it would be a good idea to add type safety to our functions. If you limit the input and output of your 
functions to a given type, it will be much easier to avoid bugs related to improper usage. In the function below, 
" : str " after msg means that the function will raise an error if you try to call get_user_int using a different 
data type ie. int, float, bool...

The " () -> int " means that the interpreter will complain if the function returns anything other than an int. This 
can help us catch bugs early when we start mixing lots of function calls together.

```Python
def get_user_int(msg: str) -> int:
    """
    This function prints the given message and waits for the user to enter an integer.

    :param msg: A message to be printed before prompting the user for an input
    :return: The integer the user entered.
    """
    while True:
        user_input = input(msg)
        try:
            user_input = int(user_input)
            break
        except ValueError:
            print("That is not an integer. Try again...")

    return user_input
```