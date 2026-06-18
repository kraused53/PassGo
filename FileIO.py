import os

def write_byte_array_to_data_file(to_write: bytes = None) -> None:
    """
    Writes the given byte array to a file

    :param to_write: The bytes to write. Default is None
    :return: Function does not return anything
    """
    if to_write is None:
        print('write_byte_array_to_file - Not given data to write')

    with open('./data.dat', 'wb') as file:
        file.write(to_write)

def read_byte_array_from_file() -> bytes | None:
    """
    Reads the PassGo data file into a bytes object. Checks to see if file exists before reading

    :return: Either the contents of the data.dat file as a bytes or an empty bytes object
    """
    file_data = bytes()

    # Check to see if the data.dat file exists
    try:
        # Try to open and read the data.dat file. Catch
        with open('./data.dat', 'rb') as file:
            file_data = bytes(file.read())
    except FileNotFoundError:
        print('read_byte_array_from_file - Error reading from file')
        return None

    # There was an error. Return an empty bytes. Returns None on error: Calling function should check for this case
    return file_data

def is_data_file_present() -> bool:
    """
    Checks if the PassGo data file exists

    :return: Returns True if the datafile exists, False otherwise
    """
    return os.path.isfile('./data.dat')

if __name__ == '__main__':
    write_byte_array_to_data_file(bytes(b'Wow, it works!!!'))
    data = read_byte_array_from_file()
    print(data.decode())