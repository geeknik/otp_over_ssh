import os
import re
import sys
import hashlib
import random

class SecureLoginToken(object):
    """Class to create secure login token"""
    def __init__(self, email_address):
        self.email_address = email_address
        self.token = None
        self.random_salt = None

    def set_token(self):
        """Create a secure login token"""
        self.random_salt = os.urandom(32)
        hasher = hashlib.sha512(self.random_salt)
        hasher.update(self.email_address.encode())
        self.token = hasher.hexdigest()

    def get_token(self):
        """Return secure login token"""
        return self.token

    def get_random_salt(self):
        """Return random salt used to create the secure login token"""
        return self.random_salt

def clear():
    """Clear screen and cursor position"""
    sys.stderr.write("\x1b[2J\x1b[H")

def main():
    """Main function"""
    clear()
    user = input("Please enter your email address\n> ")
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", user):
        print("Invalid email address")
        sys.exit(1)
    token = SecureLoginToken(user)
    token.set_token()
    print("Secure Login Token: {}".format(token.get_token()))

if __name__ == '__main__':
    main()
