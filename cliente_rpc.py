import rpyc

HOST = "localhost"
PORTA = 18861

conn = rpyc.connect(HOST, PORTA)
try:
    horario = conn.root.get_horario()
    print(f"Horário do servidor: {horario}")
finally:
    conn.close()