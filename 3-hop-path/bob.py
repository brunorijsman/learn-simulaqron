from cqc.pythonLib import CQCConnection

with CQCConnection("Bob") as cqc:

    # Receive Bob half of Alice-Bob Bell pair created by Alice
    q1 = cqc.recvEPR()

    # Create Bob-Charlie Bell pair and hold on the Bob half of it
    q2 = cqc.createEPR("Charlie")

    # Do an entanglement swap between the Bob half of Alice-Bob and the Bob half of Bob-Alice
    q1.cnot(q2)
    q1.H()
    m1 = q1.measure()
    m2 = q2.measure()

    # Send the correction meaurements to Charlie
    cqc.sendClassical("Charlie", [m1, m2])

    # Wait for the confirmation from Charlie that the end-to-end entanglement is complete
    data = cqc.recvClassical()

    # Report to Alice that end-to-end entanglement is complete
    cqc.sendClassical("Alice", b"done")


