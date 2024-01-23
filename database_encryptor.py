from cryptography.fernet import Fernet


def encrypt_dict(database):
    """
    This function takes database as argument in string format,
     then by using encrypt() method from Fernet class,
      encrypts it and save the filekey.key to disk and return the encrypted data
      """

    key = Fernet.generate_key()
    fernet = Fernet(key)
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    data = fernet.encrypt(database.encode())
    return data