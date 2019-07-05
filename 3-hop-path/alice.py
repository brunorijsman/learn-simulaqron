from cqc.pythonLib import CQCConnection, qubit

with CQCConnection("Alice") as connection:
    q = qubit(connection)
    q.H()
    m = q.measure()
    print(f"Alice: {m}")
