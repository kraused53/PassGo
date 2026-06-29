import DictionaryEncryption
import FileIO

class AppData:
    def __init__(self):
        self._user_login = False
        self._master_password = ""
        self.user_passwords = {}

    def add_password(self, organization: str, password: str, date):
        self.user_passwords[organization] = [password, date]

    def is_user_logged_in(self)->bool:
        return self._user_login

    def set_user_logged_in(self) -> None:
        self._user_login = True

    def set_master_password(self, master_password: str):
        self._master_password = master_password

    def get_passwords(self):
        return self.user_passwords

    def load_passwords(self) -> bool:
        ciphertext = FileIO.read_byte_array_from_file()
        if ciphertext is None:
            print('Error: Could not load data file!')
            return False

        passwords = DictionaryEncryption.decrypt_dictionary(self._master_password, ciphertext)

        if passwords is None:
            print('Error: Could not decrypt file!')
            return False
        
        p = passwords.keys()
        for k in p:
            self.add_password(k, passwords[k][0], passwords[k][1])
            
        self._user_login = True
        return True

    def save_passwords(self) -> bool:
        if not self._user_login:
            return False
        cipher_text = DictionaryEncryption.encrypt_dictionary(self._master_password, self.user_passwords)
        if cipher_text is None:
            print("Error: Could not save passwords!")
            return False
        FileIO.write_byte_array_to_data_file(cipher_text)
        return True

    def get_passwords(self):
        return self.user_passwords

    def generate_passwords_json(self):
        pass

if __name__ == "__main__":
  if FileIO.is_data_file_present():
    user_input = input("Enter your password: ")
    data = DictionaryEncryption.decrypt_dictionary(user_input, FileIO.read_byte_array_from_file());
    print(data)
  else:
      print("data.dat not found. PLease run program to generate one")
