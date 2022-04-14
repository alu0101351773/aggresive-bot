# Practica: Seminario 2
# Autores:
# - Juan Guillermo Zafra Fernandez (alu0101353647)
# - Jorge Cabrera Rodriguez (alu0101351773)

import pysmile
import pysmile_license

# Funcion para pedir los valores iniciales a utilizar en nuestra red bayesiana
def askEvidences():
	evidences = []
	print("Introduce el valor de St:\n - A (attack)\n - SW (switch weapon)\n - SH (switch health)\n" +
	" - E (explore)\n - F (flee)\n - DD (detect danger)")
	evidences.append(input()) 
	print("\nIntroduce el valor de Health:\n - High\n - Medium\n - Low")
	evidences.append(input())
	print("\nIntroduce el valor de Heard Noise:\n - No\n - Yes")
	evidences.append(input())
	print("\nIntroduce el valor de Number Enemies:\n - None\n - One\n - Two")
	evidences.append(input())
	print("\nIntroduce el valor de Opponent Weapon:\n - Yes\n - No")
	evidences.append(input())
	print("\nIntroduce el valor de Proximate Healthpack:\n - Yes\n - No")
	evidences.append(input())
	print("\nIntroduce el valor de Weapon:\n - Yes\n - No")
	evidences.append(input())
	return evidences

# Funcion principal de nuestro programa
def main():
	net = pysmile.Network()
	net.read_file("BotAgresivo.xdsl")
	evidences = askEvidences()

	implicated_variables = ["St", "Health", "Heard_Noise", "Number_Enemies", 
	"Opponent_Weapon", "Proximate_Healthpack", "Weapon"]
	error_code = False

	for i in range(len(implicated_variables)):
		try:
			net.set_evidence(implicated_variables[i], evidences[i])
		except:
			print(f"The value \"{evidences[i]}\" is not valid for {implicated_variables[i]}")
			error_code = True

	if (error_code == True):
		return -1

	# We update the net with the evidences
	net.update_beliefs() 

	# We calculate the results for the next instant (St+1)
	beliefs = net.get_node_value("St_1")

	print("\nFinal results:")
	# Print the results
	for i in range(0, len(beliefs)):
		print(net.get_outcome_id('St_1', i) + " = " + str(round(float(beliefs[i] * 100))) + " %")

	return 0


if __name__ == "__main__":
	main()
