def trocaFigurinha(figurinhaPaulo, figurinhaHenrique):

  indice = 0
  qntd = 0

  if len(figurinhaPaulo) < len(figurinhaHenrique):
    for i in range(len(figurinhaPaulo)):
      for j in range(len(figurinhaHenrique)):
        if figurinhaPaulo[i] == figurinhaHenrique[j]:
          indice += 1
    qntd = len(figurinhaPaulo) - indice

  elif len(figurinhaHenrique) < len(figurinhaPaulo):
    for i in range(len(figurinhaHenrique)):
      for j in range(len(figurinhaPaulo)):
        if figurinhaHenrique[i] == figurinhaPaulo[j]:
          indice += 1
    qntd = len(figurinhaHenrique) - indice

  else:
    for i in range(len(figurinhaPaulo)):
      for j in range(len(figurinhaHenrique)):
        if figurinhaPaulo[i] == figurinhaHenrique[j]:
          indice += 1
    qntd = len(figurinhaPaulo) - indice

  return qntd
