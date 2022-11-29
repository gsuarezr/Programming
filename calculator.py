class calci:
    def __init__(self):
        self.state=0
        print(self.state)
    def check(self,n):
        if (type(n) in (int,float)) or n.isnumeric():
            pass
        else:
            print('it is not valid input, threortical error,resetting...')
            self.reset()
            return True
    def reset(self):
        self.state=0
        return self.state
    def add(self,n):
        if self.check(n):
            self.reset()
            return self.state
        self.state=self.state+n
        return self.state
    def sub(self,n):
        if self.check(n):
            self.reset()
            return self.state
        self.state=self.state-n
        return self.state
    def mul(self,n):
        if self.check(n):
            self.reset()
            return self.state
        self.state=self.state*n
        return self.state
    def div(self,n):
        if self.check(n):
            self.reset()
            return self.state
        if n==0:
            print('Error')
            return self.state
        self.state=self.state/n
        return self.state
        