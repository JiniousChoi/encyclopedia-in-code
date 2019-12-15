#p115_05_diff_bits_counter.py
def diff_bits_counter(int_a, int_b):
    diff_str = bin(int_a ^ int_b)
    return diff_str.count('1')
    
if __name__ == "__main__":
    int_a = 31
    int_b = 14
    print diff_bits_counter(int_a, int_b)
