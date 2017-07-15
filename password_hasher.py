import hashlib

def hashing_method(passwd_hash):
	hash1 = hashlib.md5(passwd_hash)
	print('Your Hashed Password Is: {}'.format(hash1.hexdigest()))

def main():
	print('Password Hashing Script')
	passwd_hash = raw_input('Enter Your Password: ')
	hashing_method(passwd_hash)

if __name__ == '__main__':
	main()