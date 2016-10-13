# TODO: make so it allocates qubit in correct state
# TODO: measure multiple qubits


import re
from gatemon import applyCNOT, applyRz, applyRx, applyH
from gatemon import applyCPhase, allocateQubit, measure


assign_qubit_pattern = 'qubit\s+([a-z]\d)'
two_qubit_pattern = '([-\w]+)\s+([a-z]\d),([a-z]\d)'
single_qubit_pattern = '(\w+)\s+([a-z]\d)'


def parse_qasm(filename):
    qubits = {}
    f = open(filename)
    for line in f:
        print(line)
        m = re.search(assign_qubit_pattern, line)
        if m is not None:
            qubit = m.group(1)
            qubits[qubit] = allocateQubit(0)
            continue
        m = None
        m = re.search(two_qubit_pattern, line)
        if m is not None:
            gate = m.group(1)
            qubit1 = m.group(2)
            qubit2 = m.group(3)
            if gate.lower() == 'cnot':
                applyCNOT(qubit1, qubit2)
            else:
                applyCPhase(qubit1, qubit2)
            continue
        m = None
        m = re.search(single_qubit_pattern, line)
        if m is not None:
            gate = m.group(1)
            print(gate.lower())
            qubit = m.group(2)
            if gate.lower() == 'h':
                applyH(qubit)
            elif gate.lower == 'x':
                applyRx(qubit)
            elif gate.lower == 'z':
                applyRz(qubit)
            elif gate.lower() == 'measure':
                result = measure(qubit)
                print(result)
            else:
                raise NotImplementedError('single qubit gate not implementable')
