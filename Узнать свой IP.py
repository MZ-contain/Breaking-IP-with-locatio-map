import socket   
from pyfiglet import Figlet 
def main():
    preview_text = Figlet(font='jazmine')
    print(preview_text.renderText('Serkilo'))
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    print("Your Computer Name is:" + hostname)    
    print("Your Computer IP Address is:" + IPAddr) 
    
if __name__ == '__main__':
    main()