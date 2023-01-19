def count_max_elements(numSeq, maxElement, maxCount):
    if len(numSeq)>0:
        currElement = numSeq.pop(0)
        if currElement>maxElement:
            maxElement = currElement
            maxCount=1
        elif currElement==maxElement:
            maxCount+=1
        if currElement != 0:
            return count_max_elements(numSeq, maxElement, maxCount)
        else:
            return (maxElement,maxCount)
    else:
        return (maxElement,maxCount)




numSeq = [1, 5, 42, -376, 5, 19, 5, 3, 42, 2, 0]
print(count_max_elements(numSeq, float("-inf"), 0))
#(42, 2)
