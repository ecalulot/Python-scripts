import sys
import socket
import threading

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        err = sock.connect_ex((host, port))
        if err == 0:
            sock.close()
            print("%s has port %d open." % (host, port))
        return err
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return -111
    except socket.error:
        print("Could not connect to server.")
        return -1111
    except KeyboardInterrupt:
        return -111

def print_help():
    print("Usage: %s <hostname> <maximum port>")
    sys.exit()

def main():
    remoteserver = ""
    maxport = ""
    if len(sys.argv) > 1 and len(sys.argv) < 4:
        remoteserver = sys.argv[1]
        try:
            maxport = int(sys.argv[2])
        except ValueError:
            print("<maximum port> must be an integer.")
            print_help()
    else:
        remoteserver = input("Please input a host as an IPv4 or hostname:")
        maxport = ""
        nub = False
        while not nub:
            maxport = input("Please limit the uppermost port: ")
            try:
                maxport = int(maxport)
            except ValueError:
                print("This is not a number.")
            else:
                if maxport > 1 and maxport <= 65535:
                    nub = True
    host = socket.gethostbyname(remoteserver)
    threads = []
    try:
        for prt in range(1, maxport + 1):
            t = threading.Thread(target=scan_port, args=(host,prt,))
            threads.append(t)
            t.start()
            #err = scan_port(host, prt)
            #if err == 0:
                #print("%s has port %d open!" % (remoteserver, prt))
            #elif err == -111:
                #return err
            #elif err == -1111:
                #return err
    except KeyboardInterrupt:
        return -1
    for e in range(0, len(threads)):
        threads[e].join()

if __name__ == "__main__":
    main()
