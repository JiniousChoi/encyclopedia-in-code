#bitwise operation p155 5.6
import pdb

def bitSwapper(original):
    #pdb.set_trace()
    mask_odd_bits = 0xffffffff / 3
    mask_even_bits = (mask_odd_bits << 1)
    
    odd_bits = original & mask_odd_bits
    even_bits = original & mask_even_bits
    
    result = (odd_bits << 1)
    result |= (even_bits >> 1)
    
    return result
    
if __name__=="__main__":
    #original = 0x89abcdef
    #original = 0b11100001
    #original = 0b111010
    original = 0b10
    decimal_result = bitSwapper(original)
    binary_result_string = bin(decimal_result)
    print binary_result_string
