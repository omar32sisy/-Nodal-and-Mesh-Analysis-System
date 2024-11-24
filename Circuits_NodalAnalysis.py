
import numpy as np

def conductance(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0


def nodal_analysis():
    Nodes = int(input("Enter the number of true Nodes: "))
    conductance_matrix = np.zeros((Nodes, Nodes))
    current_column = np.zeros((Nodes,1))
    for i in range(0, Nodes ):
        for j in range(0, Nodes ):
            if i == j:
                print(
                    "Please enter the resistances of the resistors connected to node number "
                    + str(i + 1)+": ")
                C = input().split()  #get the conductances fro the user
                conductance_matrix[i, j] = sum(
                    [conductance(1,float(x)) for x in C])  #Store the sum of conductances on that cell
                print(
                    "Please enter the value of the currents sources entering Node "
                    + str(i + 1) +
                    " in postive values and currents out of it in negative values: "
                )
                I = input().split()  #get the conductances fro the user
                current_column[i,0] = sum([float(x) for x in I])  #Store of the sum of currents on that cell

            if i< j:
                print(
                    "Please enter all the resistances of the resistors between nodes "
                    + str(i + 1) + " and " + str(j + 1)+": ")
                C = input().split()  #get the conductances fro the user
                conductance_matrix[i, j] = -sum([conductance(1,float(x)) for x in C])  #Store negative of the sum of conductances on that cell
                conductance_matrix[j, i] = conductance_matrix[i, j]
    A=conductance_matrix
    B=current_column
    Ainv=np.linalg.inv(A)
    X=Ainv.dot(B)
    print("The conductance matrix is: ")
    print(A)
    print("The current column is: ")
    print(current_column)
    print("The voltages of the "+str(Nodes)+" Nodes are: ")
    print(X)


def mesh_analysis():
    Loops = int(input("Enter the number of loops"))
    

while True:
    N_M = input("Do you have all voltage sources, current sources, both or you want to exit? (C, V, B  or E): ")
    if N_M == "C":
        nodal_analysis()
    elif N_M == "V":
        Loops = int(input("\nPlease Enter the number of Loops: "))   
    elif N_M == "B":
        print("\nPlease change all current sources into voltage sources or vice versa.")
    elif N_M =="E":
        break
    else:
        print("\nPlease Enter a valid value\n")





