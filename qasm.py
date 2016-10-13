num_qubit = 0


def applyCNOT(q1, q2):
    print("cnot ", q1, ",", q2)


def applyH(q):
    print("h ", q)


def applyRz(theta=None, q):
    if theta is not None:
        print("rz(", theta, ") ", q)
    else:
        print('z')


def applyRx(theta=None, q):
    if theta is not None:
        print("rx(", theta, ") ", q)
    else:
        print('x')


def allocateQubit(init_val):
    global num_qubit
    num_qubit = num_qubit + 1
    print("qubit ", num_qubit, ",", init_val)
    return num_qubit


def measure(qubit):
    print("measure ", qubit)


def measureQubits(qubits):
    raise NotImplementedError(" to do: outsource this function ")
    result = []
    for q in qubits:
        result.append(measure(q))
    return result
