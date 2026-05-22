algoritmo "semnome"
var
   valor_emprestimo, adicional_dos_juros, valor_total_com_juros, valor_parcelas: real
   parcelas: inteiro
inicio
      Escreval ("Aghatar: Oir, alor, queria fazer um emprestimo")
      Escreval ("Leblanc: Qual valor mo?")
      Leia (valor_emprestimo)
      Escreval ("Leblanc: Hmmmm....")
      adicional_dos_juros <- (20/100)*valor_emprestimo // Aqui acontece o calculo do valor que vai ser com os 20% de juros
      valor_total_com_juros <- valor_emprestimo+adicional_dos_juros // Aqui acontece a soma do valor do emprestimo com o total de juros
      Escreval ("Leblanc: Olha, com os juros fixos de 20% fica R$ ", valor_total_com_juros)
      Escreval ("Aghatar: Caro ein fia, parcela vey?")
      Escreval ("Leblanc: Quantas parcelas você tem em mente?")
      Leia (parcelas)
      Escreval ("Leblanc: Hmmmmm......")
      valor_parcelas <- valor_total_com_juros/parcelas // Calculo do valor das parcelas
      Escreval ("Leblanc: Ficaria R$ ", valor_parcelas, " de R$ ", valor_total_com_juros)
      Escreval ("Aghatar: Tudo, vou querer veyr, onde assina?")
      Escreval ("Leblanc: Olhei aqui, você tem score baixissimo fia, sem pão velho pra você, vaza fudida")
      
      
fimalgoritmo
