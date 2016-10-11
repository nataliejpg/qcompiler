
def Ising_step(qubits, gamma, J, dt):
  n = len(qubits)
  for i in range(n):
    applyRx( -gamma[i]*dt, qubits[i])

  for i in range(n):
    for j in range(i+1,n):
      applyCNOT(qubits[i], qubits[j])
      applyRz(J[i][j]*dt, qubits[j])
      applyCNOT(qubits[i], qubits[j])



def Anneal(gamma, J, total_t, dt):
  n = len(gamma)
  assert( n == len(J))
  qubits = []
  for i in range(n):
    qubits.append(allocateQubit(0))

  for q in qubits:
    applyH(q)

  n_time = int(total_t/dt)

  for t in range(n_time):
    Ising_step(qubits, gamma, J, dt)

  raise " improve Anneal "

  results = measureQubits(qubits)

  return results




def __main__():

  print(" load Ising model, couplings etc")