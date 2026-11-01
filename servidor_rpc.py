import rpyc
from datetime import datetime
from rpyc.utils.server import ThreadedServer


class ServicoHorario(rpyc.Service):
    def on_connect(self, conn):
        print("Cliente conectado.")

    def on_disconnect(self, conn):
        print("Cliente desconectado.")

    # Métodos expostos devem começar com "exposed_"
    def exposed_get_horario(self):
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Horário solicitado: {agora}")
        return agora


if __name__ == "__main__":
    porta = 18861
    servidor = ThreadedServer(ServicoHorario, port=porta)
    print(f"Servidor RPyC escutando na porta {porta}...")
    servidor.start()
