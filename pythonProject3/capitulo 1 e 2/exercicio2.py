precodecapa = 24.95
precocapalivrodesconto = precodecapa - (precodecapa * 0.40)
custodofreteprimeiro = precocapalivrodesconto + 3.00
custodefreterestante = precocapalivrodesconto + 0.75
custototal = custodofreteprimeiro + (custodefreterestante * 59)

print("O preço total de atacado para 60 exemplares é de:", custototal)