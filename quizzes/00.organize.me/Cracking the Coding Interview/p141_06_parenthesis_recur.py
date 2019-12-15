def parenthesis_wrapper(n):
    result = parenthesis(n,n)
    return result

def parenthesis(opening_cnt, closing_cnt):
    if opening_cnt == 0 and closing_cnt==0:
        #No:return [] 
        #Yes:
        return ['']
    
    if opening_cnt < 0 or closing_cnt < 0:
        assert(False)
    
    result = []
    
    #NEVER CORRUPT ORIGINAL VALUES OF openning_cnt, closing_cnt
    #IN THE NEXT IF STATEMENTS!!!!
    if 0<opening_cnt:
        #not to influence next if-statement below:
        tmp_opening_cnt =opening_cnt - 1
        result += joiner( '(' , parenthesis(tmp_opening_cnt, closing_cnt) )
        
    if opening_cnt < closing_cnt:
        #not to influence next if-statement if below is any:
        tmp_closing_cnt = closing_cnt - 1
        result += joiner( ')' , parenthesis(opening_cnt, tmp_closing_cnt) )
    
    return result 

#par_str = '('
#list_of_par_str = [ ')()' , '())' ]
def joiner( par_ch, list_of_par_string ):
    result = []
    for each_par_string in list_of_par_string:
        result.append( par_ch + each_par_string )
    
    return result
    
if __name__=="__main__":
    print parenthesis_wrapper(3)
