from cqc.pythonLib import CQCConnection

with CQCConnection("Alice") as cqc:

    # Create Alice-Bob Bell pair and hold on the Alice half of it
    q = cqc.createEPR("Bob")

    # Wait for the confirmation from Charlie that the end-to-end entanglement is complete
    data = cqc.recvClassical()

    # Print local qubit measurement; should be random but same as Charlie's
    print(f"Alice: qubit measurement = {q.measure()}")
