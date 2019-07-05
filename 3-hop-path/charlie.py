from cqc.pythonLib import CQCConnection

with CQCConnection("Charlie") as cqc:

    # Receive Charlie half of Bob-Charlie Bell pair created by Charlie
    q = cqc.recvEPR()

    # Wait for the Bell measurement correction bits from Bob (who did a swap)
    data = cqc.recvClassical()
    message = list(data)
    m1 = message[0]
    m2 = message[1]

    # Perform Pauli corrections on Charlie's qubit
    if m2:
        q.X()
    if m1:
        q.Z()

    # Report to Bob that end-to-end entanglement is complete
    cqc.sendClassical("Bob", b"done")

    # Print local qubit measurement; should be random but same as Alice's
    print(f"Charlie: qubit measurement = {q.measure()}")
