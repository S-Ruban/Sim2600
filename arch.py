import pickle
archfile = open('chips/net_6502.pkl', 'r')
# output = open('arch.txt', 'w')
arch = pickle.load(archfile)
# for keys in arch:
    # output.write(str(keys) + '=>' + str(arch[keys]))
    # output.write("\n\n\n")
key = "WIRE_CTRL_FETS"
# print(arch[key])
print(arch[key])
# for i in range(1,5):
#     print(arch[key][i])
# print(len(arch[key]))
archfile.close()
# output.close()

# NUM_NULL_WIRES        => 21
# WIRE_NAMES            => 1725 wires (N0 - N1724)
# WIRE_CTRL_FETS        => 10467 wires
# WIRE_PULLED           => 1725 values (0 or 1) (probably initial state)
# NEXT_CTRL             => 65534
# NUM_WIRES             => 1725
# FET_SIDE2_WIRE_INDS   => 3510 longs
# NO_WIRE               => 65533
# WIRE_GATES            => 6960 longs
# NUM_FETS              => 3510
# FET_SIDE1_WIRE_INDS   => 3510 longs
# FET_GATE_INDS         => 3510 longs

# wire 657 is VCC
# wire 558 is VSS