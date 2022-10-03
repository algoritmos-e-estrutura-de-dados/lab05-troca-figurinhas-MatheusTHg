def maximizar_troca_de_figurinhas(Maria, Joao, A, B):

    indiceMaria = 0
    indiceJoao = 0 
    i = 0
    j = 0
    m = 0
    n = 0

    for i in range(int(A)):
      for j in range(int(B)):
        if Maria[i] == Joao[j]:
          indiceMaria += 1
 
    for m in range(int(B)):
      for n in range(int(A)):
        if Joao[m] == Maria[n]:
          indiceJoao += 1
   
    if (int(A) - int(indiceMaria)) < (int(B) - int(indiceJoao)):
        return print(f"O máximo de figurinhas para troca é:{int(A) - int(indiceMaria)}")
    else:
        return print(f"O máximo de figurinhas para troca é:{int(B) - int(indiceJoao)}")

if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao, A, B)
