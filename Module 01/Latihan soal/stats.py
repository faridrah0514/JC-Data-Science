class hitung_stats:
    def __init__(self, x):
        self.x = x
        self.average = self.avg()
        self.median = self.mdn()
        self.modus = self.mds()

    def avg(self):
        total=0
        for i in self.x:
            total+=i
        return float(total/len(self.x))

    def mdn(self):
        self.x.sort()
        med = 0
        lenght=len(self.x)
        if lenght % 2 == 0:
            med=(float(self.x[int((lenght/2)-1)] + self.x[int(lenght/2)])/2)
        else:
            med = self.x[int(lenght/2)]
        return med

    def mds(self):
        set_x = set(self.x)
        mod=[]
        temp=[]
        for i in set_x:
            jumlah = self.x.count(i)
            temp.append(jumlah)
        temp1=max(temp)
        for j in set_x:
            if self.x.count(j) == temp1:
                mod.append(j)
        if len(mod) > 2:
            return "Empty"
        else:
            return mod
                

        
# ll = hitung_stats([1,2,3,4,5,6,7])

# arr = [1,2,3,4,5,6,7,8,9,5,7]
# k = hitung_stats(arr)
# print(k.average())
# print(k.median())
# k.modus()
