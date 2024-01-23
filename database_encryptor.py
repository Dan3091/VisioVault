from cryptography.fernet import Fernet


def encrypt_dict(database):
    """
    This function takes database as an argument in string format,
     then by using encrypt() method from Fernet class,
      encrypts it and save the filekey.key to disk and return the encrypted data
      """

    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    data = fernet.encrypt(database.encode())
    return data

def decrypt_dict(database):
    """
    This function takes database as an argument in string format,
    open the filekey.key and save it to a key variable,
     then by using decrypt() method from Fernet class,
     decrypts it and return the data.
     """

    try:
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            data = fernet.decrypt(database).decode()
            return data
    except:
        pass
