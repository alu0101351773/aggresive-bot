import pysmile
import pysmile_license

# funcion que pregunta por las evidencias y lasguarda en un array que luego retorna
def askInitialValues():
	evidences = []
	print("Se le va a solicitar introducir los valores iniciales. Aquellos valores que esten mal escritos seran incicializados a otro que tenga sentido.")
	print("Introduce el valor de St:\n - A (attack)\n - SW (switch weapon)\n - SH (switch health)\n" +
	" - E (explore)\n - F (flee)\n - DD (detect danger)")
	evidences.append(input()) 
	print("Introduce el valor de Health:\n - High\n - Medium\n - Low")
	evidences.append(input())
	print("Introduce el valor de Heard Noise:\n - No\n - Yes")
	evidences.append(input())
	print("Introduce el valor de Number Enemies:\n - None\n - One\n - Two")
	evidences.append(input())
	print("Introduce el valor de Opponent Weapon:\n - Yes\n - No")
	evidences.append(input())
	print("Introduce el valor de Proximate Healthpack:\n - Yes\n - No")
	evidences.append(input())
	print("Introduce el valor de Weapon:\n - Yes\n - No")
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
		print("Error initial value (St) not valid")
		return -1

	try:
		net.set_evidence("Health", evidences[1])
	except:
		print("Error initial value (H) not valid")
		return -1

	try:
		net.set_evidence("Heard_Noise", evidences[2])
	except:
		print("Error initial value (HN) not valid")
		return -1

	try:
		net.set_evidence("Number_Enemies", evidences[3])
	except:
		print("Error initial value (NE) not valid")
		return -1

	try:
		net.set_evidence("Opponent_Weapon", evidences[4])
	except:
		print("Error initial value (OW) not valid")
		return -1

	try:
		net.set_evidence("Proximate_Healthpack", evidences[5])
	except:
		print("Error initial value (PH) not valid")
		return -1

	try:
		net.set_evidence("Weapon", evidences[6])
	except:
		print("Error initial value (W) not valid")
		return -1

	# Actualizamos la red
	net.update_beliefs() 

	# Calculamos los valores de St+1
	beliefs = net.get_node_value("St_1")

	# Mostrar por pantalla la tabla St+1
	for i in range(0, len(beliefs)):
		print(net.get_outcome_id('St_1', i) + "=" + "0." +str(round(float(beliefs[i] * 100))))

	return 0

main()