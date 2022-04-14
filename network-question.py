# Practica: Seminario 2
# Autores:
# - Juan Guillermo Zafra Fernandez (alu0101353647)
# - Jorge Cabrera Rodriguez (alu0101351773)

import pysmile
import pysmile_license

# Funcion para pedir los valores iniciales a utilizar en nuestra red bayesiana
def askInitialValues():
	evidences = []
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

# Funcion principal de nuestro programa
def main():
	net = pysmile.Network()
	net.read_file("BotAgresivo.xdsl")
	evidences = askInitialValues()

	implicated_variables = 3
	try:
		net.set_evidence("St", evidences[0])
	except:
		print(f"Error initial value (St = {evidences[0]}) not valid")
		return -1

	try:
		net.set_evidence("Health", evidences[1])
	except:
		print(f"Error initial value (H = {evidences[1]}) not valid")
		return -1

	try:
		net.set_evidence("Heard_Noise", evidences[2])
	except:
		print(f"Error initial value (HN = {evidences[2]}) not valid")
		return -1

	try:
		net.set_evidence("Number_Enemies", evidences[3])
	except:
		print(f"Error initial value (NE = {evidences[3]}) not valid")
		return -1

	try:
		net.set_evidence("Opponent_Weapon", evidences[4])
	except:
		print(f"Error initial value (OW = {evidences[4]}) not valid")
		return -1

	try:
		net.set_evidence("Proximate_Healthpack", evidences[5])
	except:
		print(f"Error initial value (PH = {evidences[5]}) not valid")
		return -1

	try:
		net.set_evidence("Weapon", evidences[6])
	except:
		print(f"Error initial value (W = {evidences[6]}) not valid")
		return -1

	# Actualizamos la red
	net.update_beliefs() 

	# Calculamos los valores de St+1
	beliefs = net.get_node_value("St_1")

	# Mostrar por pantalla la tabla St+1
	for i in range(0, len(beliefs)):
		print(net.get_outcome_id('St_1', i) + " = " +str(round(float(beliefs[i] * 100))) + " %")

	return 0


if __name__ == "__main__":
	main()
