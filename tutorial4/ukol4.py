import numpy as np
 
def createH(inputFile):
    text = None
    with open(inputFile, 'r') as f:
        text = f.read()
    lines = text.splitlines()
    nodes = int(lines[0])
    print(nodes)

    edges = np.zeros((nodes, nodes))

    for i in range(1, nodes + 1):
        line = lines[i].split(' ')
        if line[0] is not '':
            for item in line:
                parse_line = item.split(':')
                edges[i-1,int(parse_line[0])] = int(parse_line[1])
 
    print("edges:\n{}\n".format(edges))

    H = np.zeros((nodes, nodes))
    for row in range(0, nodes):
        for column in range(0, nodes):
            if edges[row,column] > 0:
                H[row,column] = 1/sum(edges[row])

    print("H:\n{}\n".format(H))
    return(H)
 
def createS(H):
    S = np.copy(H)
    for row in range(0, len(H)):
        if sum(S[row]) == 0:
            for column in range(0, len(S[row])):
                S[row,column] = 1/len(S)

    print("S:\n{}\n".format(S))
    return(S)
 
def createG(H,S,alpha):
    G = np.copy(S)
    for row in range(0, len(H)):
        for column in range(0, len(H[row])):
            G[row,column] = (alpha*S[row,column]) + (1.0 - alpha)*(1.0/len(H[row]))*1.0

    print("G:\n{}\n".format(G))
    return(G)
 
 
def computePR(G, iterations):
    PR = []
    PR.append(np.ones(len(G)) * 1.0/6)
    print("PR:\n{}\n".format(PR.reshape(-1)))
    print("PR:\n{}\n".format((PR[0]) * G))

    # for i in range(1,iterations + 1):
    #     PR.append((PR[i-1].transpose()) * G)

    # for row in range(len(PR)):
    #     print("PR:\n{}{}\n".format(row, PR[row]))

 
inputFile = "./data/test3_edux.txt"
alpha = 0.9
iterations = 16
 
H = createH(inputFile)
#computePR(H, iterations)
 
S = createS(H)
#computePR(S, iterations)
 
G = createG(H,S,alpha)
computePR(G, iterations)