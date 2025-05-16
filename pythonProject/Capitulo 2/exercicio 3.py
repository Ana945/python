print ("Tempo do primeiro trecho: 8 min e 15 s")
minutoPrimeirotrecho = 8 * 60
segundoPrimeiroTrecho = 15

#print ("Tempo do Primeiro trecho em segundo: ", totalTempoPrimeiroTrecho)

print("Tempo do segundo trecho: 7min e 12seg")
minutoSegundoTrecho = (7 * 3) * 60
segundosSegundoTrecho = 12 * 3

#print("Tempo do segundo trecho em segundos: ", totalTempoSegundoTrecho)

print("Tempo do terceiro trecho:8 min e 15 s ")
minutoTerceiroTrecho = 8 * 60
segundoTerceiroTrecho = 15

#print("Tempo do terceiro trecho em segundos: ", totalTempoTerceiroTrecho)

#soma o total de minutos e converte todos os segundos em minutos
totalTempoTodosTrechosMinutos = (minutoPrimeirotrecho + minutoSegundoTrecho + minutoTerceiroTrecho) /60

#soma valor total dos segundos
totalTempoTodosTrechosSegundo = (segundoPrimeiroTrecho + segundosSegundoTrecho + segundoTerceiroTrecho)


restanteMinutos = int(totalTempoTodosTrechosSegundo/ 60)
restanteSegundos = totalTempoTodosTrechosSegundo % 60

totalMinutos = totalTempoTodosTrechosMinutos + restanteMinutos
totalSegundos = restanteSegundos

print("Soma de tempo de todos os trechos: ", totalMinutos, "minutos")

print("Soma de tempo de todos os trechos: ", totalSegundos, "segundos")

horaInicialSegundos = (6 * 60) * 60
minutoInicialSegundos = 52 * 60
horarioInicialSegundos = horaInicialSegundos + minutoInicialSegundos
tempoTrechoMinutosSegundos = totalMinutos * 60

horasChegada = int((horarioInicialSegundos + tempoTrechoMinutosSegundos) / 60 / 60)
minutoChegada = int(((minutoInicialSegundos + tempoTrechoMinutosSegundos) / 60) % 60 )


print("o Tempo de chegada foi de", horasChegada , ":", minutoChegada, restanteSegundos)