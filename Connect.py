import socket, pickle, ping3

# VARIABLES GOBLALES
PORT=4445


class TimeMachines:

    @classmethod
    def ping_machine(self, ip):
        very_ping_machine = ping3.ping(ip, timeout=0.29)
        return very_ping_machine
    
    @classmethod
    # time es una lista con los valores de H(horas) y M(minutos)
    def connect_machine(self, ip, opcion):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as admin_socket:

                admin_socket.settimeout(2)
                admin_socket.connect((ip, PORT))

                send_date = pickle.dumps(opcion)
                admin_socket.sendall(send_date)
                admin_socket.close()

                return True
        except Exception as ex:
            print(ex)