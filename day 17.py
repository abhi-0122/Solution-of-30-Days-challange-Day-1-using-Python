def power(self,n,p):
    self.n = n
    self.p = p
    if n < 0 or p < 0:
        raise Exception("n and p should be non-negative")
    else:
        return n**p
