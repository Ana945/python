def concatena_texto(texto1, texto2):
    texto_inteiro = texto1 + texto2
    imprime_2_vezes(texto_inteiro)

def imprime_2_vezes(texto_inteiro):
    print(texto_inteiro)
    print(texto_inteiro)

texto1 = "Agua mole em pedra dura, "
texto2 = "tanto bate até que fura."

concatena_texto(texto1, texto2)

#chamando função  concatena_texto ()
#parametro é oq ta dentro do parentese  def concatena_texto()