import re

pattern1 = '("a-zA-Z-"+)\s+("a-zA-Z0-9"+)'
pattern2 = "..."
pattern_arg1 = "..."

def parse(filename):
  qubits = {}
  f = open(filename)
  for line in f:
    m = re.search(pattern2, line)
    if len(m) == 1:
      if m[0][0] == "cnot":
        applyCNOT(qubits[m[0][1]], qubits[m[0][2]])
      if m[0][0] == "qubit":
        qubits[m[0][1]] = allocateQubit(int(m[0][2])
        print("qubit allocated")
    else:
      n = re.search(pattern1, line)
      if len(m) == 1:
        if m[0][0] == "h":
          applyH(qubits[m[0][1]])
        if m[0][0] == "measure":
          result = measure(qubits[m[0][1]])
          print(result)


