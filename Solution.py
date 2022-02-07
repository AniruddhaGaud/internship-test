class solution :
    
    def main( args) :
        a =  []
        a.append(2)
        a.append(3)
        a.append(4)
        a.append(5)
        a.append(6)
        p = 4
        # use any value
        index = solution.getIndex(a, p)
        print("Index: " + str(index))
    
    def  getIndex( a,  p) :
        index = -1
        i = 0
        while (i < len(a)) :
            if (p == a[i]) :
                index = i
                break
            i += 1
        if (index == -1) :
            index = len(a)
        return index
    

if __name__=="__main__":
    solution.main([])