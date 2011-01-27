from Bio import AlignIO


def find_gaps(alignment,tag):
    gaplist = []
    sequence = None
    for record in alignment:
        if(record.id == tag): #as far as I can tell I can only iterate through an alignment, I can't lookup by tag
            sequence = record
            break
    resid = 1
    gap_start = 1
    gap_end = 1
    in_gap = False
    for residue in sequence:
        if residue == '-': # we are in a gap now
            if not in_gap: #this must be the first position of the gap
                gap_start = resid
                in_gap = True
        else: #we are not in a gap now
            if in_gap: #the last gap position must have been the previous residue
                gap_end = resid-1 
                in_gap = False
                gaplist.append( (gap_start,gap_end) ) 
        resid += 1
    return gaplist