import parameters

def add(x,y):
    total = x + y
    print ('total>>>', total)
    return total
  

if __name__=="__main__":
    x = parameters.x
    y = parameters.y
    add(x,y)

