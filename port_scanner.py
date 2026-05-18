import socket


ip = input("input the ip you want to scan: ")
start_port = int(input("what port do you want to start the scan: "))
end_port = int(input("what port do you want to end the scan: "))

range_port = range(start_port, end_port)
for i in range_port:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, i)) 
    if(result == 0):
        print(f"port {i} is open")
    else:
        print(f"port {i} is closed")


sock.close()