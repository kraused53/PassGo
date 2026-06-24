# venv tutorial

If you have not worked with a python virtual environment before, here is a quick intro on how to set up a python environment. First, in a terminal navigate to the directory of your project (.../PassGo/) and then run this command:

```Bash
python -m venv .venv
```

this will run the python module venv (Virtual ENVironment) and save it to a directory called .venv (.../PassGo/.venv)

Then, to activate the environment:

On windows:
```Bash
.venv\Scripts\activate

or

& .venv/Scripts/activate
```

Mac / Linux:
```Bash
source .venv/bin/activate
```

This will load the virtual environment. Now, instead of using your system's version of python / installed libraries it uses the interpreter found inside .venv

This protects your project when you update / install new python interpreters and libraries.

If the project has a requirements.txt file, you can use it to install all of the libraries needed to run the project. This step ensures that a venv on two separate machines will run the project using the same libraries and interpreter regardless of how python runs on that machine

```Bash
pip install -r requirements.txt
```

If you install a new library or update python for the project, you can generate a new requirements.txt by running the command:

```Bash
pip freeze > requirements.txt
```

This makes it so when someone else running your project runs pip install -r requirements.txt, they will now have the libraries you added.


To leave a virtual environment run:

```bash
deactivate
```

# First draft for encryption system

To use the encryption library, we need to update to a newer version of the python interpreter. This has tested using Python 3.14

Please take a look at these to get a feel for how to utilize them.

At the moment, these are set up to encrypt / decrypt a dictionary object. IDK what the plan for storing the user's passwords list while to program is running, but I think a dictionary is a natural choice

So, if passwords are stored in-memory in a dictionary like:

```Python
passwords = {
    'bank': 'bank_password',
    'google': 'google_password',
    'irs': 'irs_password'
}
```

then the encryption system can be used like:

```Python
# Somewhere inside save passwords screen???

passwords = { ... }
master_password = "user_master_password"

# Encrypt passwords using master_password
ciphertext = DictionaryEncryption.encrypt_dictionary(master_password, passwords)

# Handle case where ciphertext == None
if ciphertext == None:
    # do something

# Save encrypted passwords as a data file
FileIO.write_byte_array_to_data_file(ciphertext)
```

and the decryption system can be used like:

```Python
# Somewhere inside load passwords screen???

# Load encrypted data file
ciphertext = FileIO.read_byte_array_from_file(ciphertext)

# Handle case where ciphertext == None
if ciphertext == None:
    # do something

master_password = "user_master_password"
passwords = DictionaryEncryption.decrypt_dictionary(master_password, ciphertext)

# Handle case where passwords == None
if passwords == None:
    # do something

```

