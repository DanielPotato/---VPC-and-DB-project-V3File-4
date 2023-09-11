
# Python3.6  
# Coding: utf-8  
# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin

pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}
float(insulin.count("Y"))
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)
seqCount = {'k': 1, 'h': 2, 'r': 3, 'y': 4, 'c': 5, 'd': 6, 'e': 7}
pKR = {'k': 10.0, 'h': 9.0, 'r': 11.0, 'y': 4.0, 'c': 3.0, 'd': 4.0, 'e': 5.0}

for pH in range(15):
    netCharge = sum(
        ((seqCount[x] * (10**pKR[x])) / ((10**pH) + (10**pKR[x])))
        for x in ['k', 'h', 'r']
    ) - sum(
        ((seqCount[x] * (10**pH)) / ((10**pH) + (10**pKR[x])))
        for x in ['y', 'c', 'd', 'e']
    )
    print('{0:.2f}'.format(pH), netCharge)