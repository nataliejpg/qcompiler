
import math

num_qubit = 0

def applyCNOT(q1, q2):
  print("cnot ", q1, ",", q2)

def applyH(q):
  print("h " , q)

def applyRz(theta, q):
  print("rz(", theta, ") ", q)

def applyRx(theta, q):
  print("rx(", theta, ") ", q)

def allocateQubit(init_val):
  num_qubit = num_qubit + 1
  print("qubit ", num_qubit, ",", init_val)
  return num_qubit

def measure(qubit):
  print("measure ", qubit)
  return None


def measureQubits(qubits):
  raise " to do: outsource this function "
  result = []
  for q in qubits:
    result.append(measure(q))

  return result
