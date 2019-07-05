from cqc.pythonLib import CQCConnection, qubit

with CQCConnection("Charlie") as connection:
    q = qubit(connection)
    q.H()
    m = q.measure()
    print(f"Charlie: {m}")
