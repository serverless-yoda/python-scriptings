import hashlib
import configparser
import utility

class PasswordChecker():
    '''A password checker using pwnedpasswords api'''
    def __init__(self,password):

        # read configuration
        parser = configparser.ConfigParser()
        parser.read('config.conf')

        self.url = parser.get('default','api_url')
        self.passwordToCheck = password

    def check_your_password(self):
        #convert password to SHA1
        sha1password = hashlib.sha1(self.passwordToCheck.encode('utf-8')).hexdigest().upper()
        
        #pass the first 5 characters of SHA1
        response = utility.get_apidata(self.url,sha1password[:5]) 

        #compare the last 5 characters againt the password returned by the API
        return utility.get_leakpassword_count(response,sha1password[5:])
        

def main(*args):
    for password in args:
        checker = PasswordChecker(password)
        count =  checker.check_your_password()
        if count:
          print(f'\'{password}\' was found {count}. Please change  your password') 
        else:
            print(f'\'{password}\' was not found. Very good')
    
    print('Checking completed')

main('qwerty!@#')