from cqc.pythonLib import CQCConnection, qubit

with CQCConnection("Bob") as connection:
    q = qubit(connection)
    q.H()
    m = q.measure()
    print(f"Bob: {m}")
