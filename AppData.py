import DictionaryEncryption
import FileIO

class AppData:
    def __init__(self):
        self._user_login = False
        self._master_password = ""
        self._user_passwords = {}

    def add_password(self, organization: str, password: str):
        self._user_passwords[organization] = password

    def is_user_logged_in(self)->bool:
        return self._user_login

    def set_user_logged_in(self) -> None:
        self._user_login = True

    def set_master_password(self, master_password: str):
        self._master_password = master_password

    def get_passwords(self):
        return self._user_passwords

    def load_passwords(self) -> bool:
        ciphertext = FileIO.read_byte_array_from_file()
        if ciphertext is None:
            print('Error: Could not load data file!')
            return False

        passwords = DictionaryEncryption.decrypt_dictionary(self._master_password, ciphertext)

        if passwords is None:
            print('Error: Could not decrypt file!')
            return False

        for k, v in passwords.items():
            self.add_password(k, v)
        print(passwords)
        print(self._user_passwords)
        self._user_login = True
        return True

    def save_passwords(self) -> bool:
        cipher_text = DictionaryEncryption.encrypt_dictionary(self._master_password, self._user_passwords)
        if cipher_text is None:
            print("Error: Could not save passwords!")
            return False
        return True

    def generate_passwords_json(self):
        pass

if __name__ == "__main__":
    data = AppData()
    print(data.get_passwords())

    data.add_password("google", "password_1")
    data.add_password("irs", "password_2")
    data.add_password("bank", "password_123")

    data.save_passwords()


    print(data.get_passwords())
