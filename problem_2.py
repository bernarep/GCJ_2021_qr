def cost(stringa, CJ, JC):
    costo=0
    for i in range(len(stringa)-1):
        tmp=stringa[i:i+2]
        if(tmp=="CJ"):
            costo=costo+CJ
        if(tmp=="JC"):
            costo=costo+JC
    return costo

def manipulate(stringa):
    formatted=""
    for i in range(len(stringa)):
        if(stringa[i]!="?"):
            formatted = formatted+stringa[i]
    return formatted
            
Ncases = input()
for i in range(int(Ncases)):
    CJ, JC, testo = [s for s in input().split(" ")]
    CJ = int(CJ)
    JC = int(JC)
    costo_fin = cost(manipulate(testo), int(CJ), int(JC))
    print("Case #{}: {}".format(i+1, costo_fin))
