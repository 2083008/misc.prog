def intToBinary ( integer, number_of_bits ):# could extend for 2's complement
	binary_out = ""
	current_bit = number_of_bits - 1 
	
	if ( 2**number_of_bits - 1 < integer ):
		return ("integer: %i cannot be represented in %i bits" % (integer,number_of_bits))
	for bits in range(number_of_bits):
		if (2**current_bit <= integer):
			binary_out += "1"
			integer -= 2**current_bit
		else:
			binary_out += "0"
		current_bit -= 1
	return binary_out

print intToBinary(127,7)
