import math

num_qubit = 0

def applyCNOT(q1, q2):
  applyH(q2)
  applyCPhase(math.pi, q1, q2)
  applyH(q2)

def applyH(q):
  raise "to be implemented"

def applyRz(theta, q):
  raise "to be implemented"

def applyRx(theta, q):
  raise "to be implemented"

def allocateQubit(init_val):
  print("this should allocate and initialise a qubit")
  num_qubit = num_qubit + 1
  return num_qubit

def measure(qubit):
  raise " implement measure "

def measureQubits(qubits):
  result = []
  for q in qubits:
    result.append(measure(q))

  return result


