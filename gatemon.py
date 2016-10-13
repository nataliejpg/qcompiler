import math

num_qubit = 0


def applyCNOT(q1, q2):
    applyH(q2)
    applyCPhase(q1, q2)
    applyH(q2)


def applyH(q):
    raise NotImplementedError


def applyRz(theta=math.pi, q):
    raise NotImplementedError


def applyRx(theta=math.pi, q):
    raise NotImplementedError


def applyCPhase(theta=math.pi, q1, q2):
    raise NotImplementedError


def allocateQubit(init_val):
    global num_qubit
    print("this should allocate and initialise a qubit")
    num_qubit = num_qubit + 1
    return num_qubit


def measure(qubit):
    raise NotImplementedError


def measureQubits(qubits):
    result = []
    for q in qubits:
        result.append(measure(q))
    return result
