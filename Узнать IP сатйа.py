import socket
def get_ip_by_hostname():
    hostname = input('Введите url адрес сайта:')

    try:
        return f'Hostname: {hostname}\nIP adress: {socket.gethostbyname(hostname)}'
    except socket.gaierror as error:
        return f'Invalid Hostname - {error}'

def main():
    print(get_ip_by_hostname())

if __name__ == '__main__':
    main()