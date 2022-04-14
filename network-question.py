import pysmile
import pysmile_license

# funcion que pregunta por las evidencias y lasguarda en un array que luego retorna
def askInitialValues():
	evidences = []
	print("Introduce el valor de St(Ataca|Recoge_arma|Recoge_energia|Explorar|Huir|Detectar_enemigo):")
	evidences.append(input())
	print("Introduce el valor de H(Alta|Baja):")
	evidences.append(input())
	print("Introduce el valor de HN(Si|No):")
	evidences.append(input())
	print("Introduce el valor de NE(Si|No):")
	evidences.append(input())
	print("Introduce el valor de OW(Armado|Desarmado):")
	evidences.append(input())
	print("Introduce el valor de PH(Si|No):")
	evidences.append(input())
	print("Introduce el valor de PW(Si|No):")
	evidences.append(input())
	print("Introduce el valor de W(Armado|Desarmado):")
	evidences.append(input())
	return evidences

def main():
	# Cargamos la red y la librería de la red
	net = pysmile.Network()
	net.read_file("BotAgresivo.xdsl")

	# Fijamos las evidencias iniciales
	evidences = askInitialValues()

	try:
		net.set_evidence("St", evidences[0])
	except:
		print("Error initial value not valid")
		return -1

	try:
		net.set_evidence("H", evidences[1])
	except:
		print("Error initial value not valid")
		return -1

	try:
		net.set_evidence("HN", evidences[2])
	except:
		print("Error initial value not valid")
		return -1

	try:
		net.set_evidence("NE", evidences[3])
	except:
		print("Error initial value not valid")
		return -1

	try:
		net.set_evidence("OW", evidences[4])
	except:
		print("Error initial value not valid")
		return -1

	try:
		net.set_evidence("PH", evidences[5])
	except:
		print("Error initial value not valid")
		return -1

	try:
		net.set_evidence("PW", evidences[6])
	except:
		print("Error initial value not valid")
		return -1

	try:
		net.set_evidence("W", evidences[7])
	except:
		print("Error initial value not valid")
		return -1

	# Actualizamos la red
	net.update_beliefs() 

	# Calculamos los valores de St+1
	beliefs = net.get_node_values("St_1")

	# Mostrar por pantalla la tabla St+1
	for i in range(0, len(beliefs)):
		print(net.get_outcome_id('St_1', i) + "=" + str(round(float(beliefs[i] * 100))))

	return 0

main()