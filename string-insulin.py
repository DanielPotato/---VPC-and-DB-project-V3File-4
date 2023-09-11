# Store the human preproinsulin sequence in a variable called preproinsulin:
preproinsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
ls_insulin = "malwmrllpllallalwgpdpaaa"
b_insulin = "fvnqhlcgshlvealylvcgergffytpkt"
a_insulin = "giveqcctsicslyqlenycn"
c_insulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Printing the sequence of human preproinsulin:
print("The sequence of human preproinsulin:")
print(preproinsulin)

# Printing the sequence of human insulin, chain a:
print("The sequence of human insulin, chain a: " + a_insulin)

# Calculating the molecular weight of insulin
# Creating a dictionary of amino acid (AA) weights
aa_weights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
              'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
              'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
              'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Count the number of each amino acid
aa_count_insulin = {x: float(preproinsulin.upper().count(x)) for x in aa_weights}

# Multiply the count by the weights and sum them up
molecular_weight_insulin = sum(aa_count_insulin[aa] * weight for aa, weight in aa_weights.items())

# Printing the rough molecular weight of insulin:
print("The rough molecular weight of insulin: " + str(molecular_weight_insulin))