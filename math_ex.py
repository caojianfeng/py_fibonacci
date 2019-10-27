import math

GOLDEN_SECTION = (math.sqrt(5)-1)/2

# pos : 'start'|'end'
# start: +-[ret]-+------------+
# end  : +---[ret]----+-------+
def gold_pos(size,pos):
    if pos == "end":
        return size*GOLDEN_SECTION
    
    return size*(1-GOLDEN_SECTION)

def gold_offset(size,pos):
    return size/2-gold_pos(size,pos)