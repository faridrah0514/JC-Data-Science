print ('Soal 3:')
def tower_builder(n_floors,block_size):
    w,h = block_size
    z = ''
    for i,j in zip(range(n_floors*h),range(n_floors*h-1,-1,-1)):
        for a in range((j//h)):
            for c in range(w):
                z += ' '
        for b in range(((i//h)*2)+1):
            for d in range(w):
                z += '*'
        z += '\n'
    return print (z)


tower_builder(6, (2,1))
tower_builder(3, (2,3))
tower_builder(6, (3,3))
