x = [20,3,2,4,-1]
def sort_asc(x):
    for i in range(len(x)):
        m=0
        print("=*=*=*=*=*")
        for _ in range(len(x)):
            print(f"ini i: {i}, ini m: {m} -> if x[{i}] < x[{m}] ? -> {x}")
            if x[i] < x[m]:
                x[m], x[i] = x[i], x[m]
            m+=1
            
            print(x)

def sort_desc(x):
    for i in range(len(x)):
        m=0
        for _ in range(len(x)):
            if x[i] > x[m]:
                x[m], x[i] = x[i], x[m]
            m+=1
    print(x)

sort_asc(x)
# sort_desc(x)
