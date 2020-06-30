#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.visualization import *
from math import *
from qiskit.extensions import Initialize 
from numpy import *


# In[2]:


def FindStrokeWithIndex(index):
    output = ""
    switcher =  {
        0 : "Thaa",
        1 : "Ki",
        2 : "Thom",
        3 : "Nam",
        4 : "Ta",
        5 : "Dhin",
        6 : "Mi",
        7 : "Cha",
        8 : "Chapu",
        9 : ",",
      
    }
    return (switcher.get(index, "X"))

# Number of Strokes : Define how long the music needs to be [Length in number of strokes] 
def Q4C (NumberOfStrokes):
    
    # Define vectors for Each stroke

    Thaa = [10,75,10,50,25,50,25,50,75,50,0,0,0,0,0,0]
    Ki = [75,10,75,75,95,50,5,5,10,50,0,0,0,0,0,0]
    Thom = [10,75,25,75,25,50,50,50,75,50,0,0,0,0,0,0]
    Nam = [50,75,75,25,5,95,95,25,25,50,0,0,0,0,0,0]
    Ta = [50,95,95,5,5,5,75,25,5,50,0,0,0,0,0,0]
    Dhin = [50,50,50,95,5,50,95,25,5,50,0,0,0,0,0,0]
    Mi = [25,5,50,95,75,95,5,5,5,50,0,0,0,0,0,0]
    Cha = [50,5,50,25,25,25,5,5,5,50,0,0,0,0,0,0]
    Chapu = [75,10,75,25,5,5,5,5,5,50,0,0,0,0,0,0]
    Kaarvai = [50,50,50,50,50,50,50,50,50,50,0,0,0,0,0,0]

    # Then calculate the norm from the frequency distribution
    Norm_Thaa = linalg.norm(Thaa)
    Norm_Ki = linalg.norm(Ki)
    Norm_Thom = linalg.norm(Thom)
    Norm_Nam = linalg.norm(Nam)
    Norm_Ta = linalg.norm(Ta)
    Norm_Dhin = linalg.norm(Dhin)
    Norm_Mi = linalg.norm(Mi)
    Norm_Cha = linalg.norm(Cha)
    Norm_Chapu = linalg.norm(Chapu)
    Norm_Kaarvai = linalg.norm(Kaarvai)


    # Then normalize the vector to be used with the QuGate
    Thaa_Norm = Thaa/Norm_Thaa
    Ki_Norm = Ki/Norm_Ki
    Thom_Norm = Thom/ Norm_Thom
    Nam_Norm = Nam/Norm_Nam
    Ta_Norm = Ta/Norm_Ta
    Dhin_Norm = Dhin/Norm_Dhin
    Mi_Norm = Mi/Norm_Mi
    Cha_Norm = Cha/Norm_Cha
    Chapu_Norm = Chapu/Norm_Chapu
    Kaarvai_Norm = Kaarvai/Norm_Kaarvai

    InitialState = [ Thaa_Norm, Ki_Norm, Thom_Norm, Nam_Norm, Ta_Norm, Dhin_Norm, Mi_Norm, Cha_Norm, Chapu_Norm,Kaarvai_Norm]
    ProbState = [ Thaa, Ki, Thom, Nam, Ta, Dhin, Mi, Cha, Chapu, Kaarvai ]
    # Print all the normalized input vectors
    #for item in InitialState:
    #    print(item)

     # Select an arbitray input state using random function
    # Though this means that all the states have equal probability as input,
    # it is still a valid assumption for the use-case
    firstSelect = True
    while (firstSelect):
        input_state = random.randint(0,len(InitialState))
        if (input_state != 6 or input_state != 9):
            firstSelect = False

    # Defining Backend for Quantum Simulator
    backend = Aer.get_backend('statevector_simulator')

    # Initialise our qubit and measure it
    NumberofQbits = 4
    NumberofQuOutputBits = 4

    # Define the Quantum Circuit
    qc = QuantumCircuit(NumberofQbits, NumberofQuOutputBits)
    FinalList = []
    for i in range (0, NumberOfStrokes):
        redo_stroke = True
        # print("State " + str (i) + " is " + FindStrokeWithIndex(input_state))
        FinalList.append(FindStrokeWithIndex(input_state))
        while (redo_stroke) :
            randomSelect = True
            # Now that the ciruit is setup - Algorithm to generate Music
            initializer  = Initialize(InitialState[input_state])
            initializer.label = str("input stroke")
            qc.append(initializer, [0,1,2,3])
            qc.h(0)
            qc.h(1)
            qc.h(2)
            qc.h(3)
            qc.measure_all()
            # qc.draw()
            # State Vector Simulator for Output
            result = execute(qc,backend).result()
            counts = result.get_counts()
            next_state = (list(counts.keys())[list(counts.values()).index(1)]).split()[0]
            if (int(next_state, 2) < 10 and ProbState[input_state][int(next_state, 2)] >=25):
                redo_stroke = False
                input_state = int(next_state, 2)
            if ( i == NumberOfStrokes - 2 ):
                if (input_state == 1 or input_state == 3 or input_state == 5 or input_state == 6 ):
                    redo_stroke = False
                else:
                    redo_stroke = True
            
    return (FinalList)


def main():
    NumberOfStrokes = 8
    print (Q4C(NumberOfStrokes))

if __name__ == '__main__':
    main()
