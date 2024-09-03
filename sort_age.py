workers=[('John',26),('Eric',28)]
def sort_by_age(workers):
     return sorted(workers,key=lambda person:person[1])
    

sort_by_age(workers)