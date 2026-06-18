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