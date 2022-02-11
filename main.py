import hashlib

def encrypt_with_md5(word_to_encrypt):
    encrypted_word = hashlib.md5(word_to_encrypt.encode('utf-8'))
    return encrypted_word.hexdigest()

def encrypt_with_sha1(word_to_encrypt):
    encrypted_word = hashlib.sha1(word_to_encrypt.encode('utf-8'))
    return encrypted_word.hexdigest()

group_of_encryption_methods = {
    "MD5": encrypt_with_md5,
    "SHA1": encrypt_with_sha1,
}

word_to_encrypt = input('Введите слово или фразу для шифрования:\n')
user_encryption_method = input('Каким способом зашифровать:\n1. MD5\n2. SHA1\n> ')

print(group_of_encryption_methods[user_encryption_method](word_to_encrypt))


print('Что-нибудь новое, добавленное с другой ветки.')