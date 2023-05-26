#packages
import string
import math
from random import randint
import numbers

##########################################

#Determining Whether or not the algebra is associative
asso = None
while asso is None:
    inp=input("Is the agebra associative?( enter 1 if yes and 0 if no):")
    try:
      asso = int(inp)
    except ValueError:
      print("{input} is not a number, please enter 1 or 0 only".format(input=inp))
      continue
    if not(asso==0 or asso==1):
      print("Please enter 0 or 1")
      asso = None

#Determining Whether or not the algebra is commutative
comm = None
while comm is None:
    inp=input("Is the agebra commutatitive?( enter 1 if yes and 0 if no):")
    try:
      comm = int(inp)
    except ValueError:
      print("{input} is not a number, please enter 1 or 0 only".format(input=inp))
      continue
    if not(comm==0 or comm==1):
      print("Please enter 0 or 1")
      comm = None

#Determining Whether or not the algebra is idempotent
idemp = None
while idemp is None:
    inp=input("Is the agebra Idempotent?( enter 1 if yes and 0 if no):")
    try:
      idemp = int(inp)
    except ValueError:
      print("{input} is not a number, please enter 1 or 0 only".format(input=inp))
      continue
    if not(idemp==0 or idemp==1):
      print("Please enter 0 or 1")
      idemp = None


#################################################

# Important lists and variables
letters = list(string.ascii_letters)
digits = list(string.digits)

##################################################

# Class definitions


###################################################

# Monomial Class
class Monomial():
    'Represents the class of monomials'


    def __init__(self, m):
        """ Initialisation method for monomial class"""

        p = isinstance(m,str)

        if p is True:
            mon=""
            for i in m:
                if i == " ":
                    pass
                else:
                    mon = mon + i
                
            t = isMon(mon)
        else:
            t=False

        while t is False:
            print("{input} is not a valid monomial, please enter a valid monomial:".format(input=m))
            m = input("Eneter the monomial")
            mon=""
            for i in m:
                if i == " ":
                    pass
                else:
                    mon = mon + i
            t = isMon(mon)
                
        mon1=standardise(mon)
        if idemp==0:
            self.mon = mon1
        elif idemp==1:
            imon1 = idempotent(mon1)
            self.mon = imon1
        
        


        

    def __mul__(self, other):
        """Take two monomials and return their product.
            
            string + string --> string
            Quantities:
                lets = letters in self
                leto = letters in other
                rself = string containg just the letters in self
                rother = string containing just the letters in other
                """
        lets=0
        leto=0
        rself= ""
        rother= ""
        
        for i in self.mon:
            if i in letters:
                lets=lets+1
                rself=rself+i

        for i in other.mon:
            if i in letters:
                leto=leto+1
                rother=rother+i

        if asso == 1:
            if comm==1:
                p = self.mon + other.mon
                prod = Monomial(p)
                return prod
            elif comm==0:
                p = self.mon + other.mon
                prod = Monomial(p)
                return prod

        if asso ==0:
            if comm==0:
                if lets<2:
                    if leto <2:
                        p = self.mon + other.mon
                        prod = Monomial(p)
                        return prod
                    else:
                        p= self.mon + "("+ other.mon + ")"
                        prod = Monomial(p)
                        return prod
                
                elif leto<2:
                    p=   "("+ self.mon + ")" + other.mon
                    prod = Monomial(p)
                    return prod

                else:
                    p = "(" + self.mon + ")" + "(" + other.mon + ")" 
                    prod = Monomial(p)
                    return prod


            if comm==1:

                if lets==0:
                    p = self.mon +other.mon
                    prod= Monomial(p)
                    return prod
                elif leto == 0:
                    p = other.mon+self.mon
                    prod = Monomial(p)
                    return prod
                
                
                if lets == 1 :
                    if leto == 1:
                        p = other.mon + self.mon
                        prod = Monomial(p)
                        return prod
                    else:
                        p = self.mon + "(" + other.mon + ")"
                        prod = Monomial(p)
                        return prod

                elif leto==1:
                    p = other.mon + "(" +self.mon + ")"
                    prod = Monomial(p)
                    return prod

                else:
                    

                    if lets > leto:
                        p="(" + other.mon + ")" + "(" + self.mon + ")"
                        prod = Monomial(p)
                        return prod
            

                    elif lets < leto:
                        p= "(" + self.mon + ")" + "(" + other.mon + ")"
                        prod = Monomial(p)
                        return prod


                    else:
                        if len(self.mon)<len(other.mon):
                            p = "("+ self.mon + ")" + "(" + other.mon + ")"
                            prod = Monomial(p)
                            return prod
        
                        elif len(self.mon)>len(other.mon):
                            p = "("+ other.mon + ")" + "(" + self.mon + ")"
                            prod = Monomial(p)
                            return prod
        
                        else:
                            if rself<rother:
                                p = "("+ self.mon + ")" + "(" + other.mon + ")"
                                prod = Monomial(p)
                                return prod
        
                        
                            else:
                                p = "("+ other.mon + ")" + "(" + self.mon + ")"
                                prod = Monomial(p)
                                return prod
        
                        
    def __eq__(self, other):
        """compare two monomials: equality"""

        if isinstance(other, Monomial):
            if self.mon == other.mon:
                return True
        else:
            return False

    def __lt__(self, other):
        """compare two monomials: less than"""

        if isinstance(other, Monomial):
            lets=0
            leto=0
            rself= ""
            rother= ""
        
            for i in self.mon:
                if i in letters:
                    lets=lets+1
                    rself=rself+i

            for i in other.mon:
                if i in letters:
                    leto=leto+1
                    rother=rother+i

            if lets<leto:
                return True
            elif leto<lets:
                return False

            else:
                if len(self.mon)<len(other.mon):
                    return True
        
                elif len(self.mon)>len(other.mon):
                    return False
                 
                else:
                    if rself<rother:
                        return True
                    elif rself > rother:
                        return False
                    else:
                        if self.mon < other.mon:
                            return True
                        elif self.mob>other.mon:
                            return False
                        else:
                            return False
        else:
            return False


    def __gt__(self, other):
        """compare two monomials: greater than"""

        if isinstance(other, Monomial):
            lets=0
            leto=0
            rself= ""
            rother= ""
        
            for i in self.mon:
                if i in letters:
                    lets=lets+1
                    rself=rself+i

            for i in other.mon:
                if i in letters:
                    leto=leto+1
                    rother=rother+i

            if lets>leto:
                return True
            elif leto>lets:
                return False

            else:
                if len(self.mon)>len(other.mon):
                    return True
        
                elif len(self.mon)<len(other.mon):
                    return False
                 
                else:
                    if rself>rother:
                        return True
                    elif rself < rother:
                        return False
                    else:
                        if self.mon > other.mon:
                            return True
                        elif self.mob<other.mon:
                            return False
                        else:
                            return False

        else:
            return False
 

    def __hash__(self):
        """hash a monomial"""

        return hash(self.mon)

    def __str__(self):
        """Printing a monomial"""

        return self.mon

    def __repr__(self):
        """representing"""

        return self.mon

        
 
    


#############################################################

# Algebra Element Class
class AlgebraElement():

    def __init__(self, element):
        """ Initialisation for an algebra element"""

        p = isinstance(element, str)
        while p is False:
            print("{el} is not a valid element.".format(el=element))
            element= input('Please enter a valid element:')
            p= isinstance(element, str)
        if p is True:
            i=0
            while i <len(element):
                if element[i] == "-" or element[i]=="+":
                    element= element[0:i]+"#"+element[i:]
                    i=i+2
                elif i==0:
                    element="#"+element
                    i=i+2
                else:
                    i=i+1
            termlist=element.split("#")

            self.element = {}

            for term in termlist:
                if len(term)==0:
                    pass
                else:
                    insert = 0
                    i=0
                    while i < len(term):
                        if ((term[i] in letters) or (term[i]=="("))  and insert == 0:
                            if i==0:
                                term = "#" + term
                            else:
                                term = term[0:i]+"#"+term[i:]
                            i = i+2
                            insert=insert+1
                        elif i == len(term)-1 and insert ==0:
                            term = term + "#"
                            insert=insert+1
                            i=i+2
                        else:
                            i = i+1

                    termbreak = term.split("#")
                    if termbreak[0] in ["", "+", "-"]:
                        if termbreak[0] == "-":
                            coeff = -1
                        else:
                            coeff = 1
                    else:
                        coeff=None
                        while coeff is None:
                            
                            try:
                                coeff = float(termbreak[0])
                            except ValueError:
                                print("{coeff} is not a number, make sure each term has a valid coefficient.".format(coeff=termbreak[0]))
                                print("{mon} please enter a valid number as coefficient:".format(mon=termbreak[1]))
                                termbreak[0] = input()
                                continue

                    
                    
                    mon = Monomial(termbreak[1])

                    if mon in self.element.keys():
                        self.element[mon] = self.element[mon] + coeff
                    else:
                        self.element[mon] = coeff


                

                    

    def __mul__(self , other):
        """multiplication of two algebra elements"""

        if isinstance(other, AlgebraElement):
            prod = AlgebraElement("")
            for i in self.element.keys():
                for j in other.element.keys():
                    if i*j in prod.element.keys():
                        prod.element[i*j]=prod.element[i*j]+self.element[i]*other.element[j]
                    else:
                        s= str(self.element[i]*other.element[j])+str(i*j)
                        prod = prod + AlgebraElement(s)
            return prod

        elif isinstance(other, numbers.Number):
            sother = str(other)
            other=AlgebraElement(sother)
            return self*other
        elif isinstance(self, numbers.Number):
            sself = str(self)
            self=AlgebraElement(self)
            return self*other

        elif isinstance(other, Monomial):
            sother = other.mon
            other = AlgebraElement(sother)
            return self*other
        elif isinstance(self, Monomial):
            sself = str(self)
            self=AlgebraElement(self)
            return self*other

    def __rmul__(self, other):
        return self.__mul__(other)
            
    

        

    def __add__(self, other):
        """addition of two algebra elements"""

        if isinstance(other, AlgebraElement):
            summ = AlgebraElement("")
            for i in self.element.keys():
                summ.element[i] = self.element[i]
            for j in other.element.keys():
                if j in self.element.keys():
                    summ.element[j]=self.element[j]+other.element[j]
                else:
                    summ.element[j]=other.element[j]
            return summ

        elif isinstance(other, numbers.Number):
            sother = str(other)
            other=AlgebraElement(sother)
            return self+other
        elif isinstance(self, numbers.Number):
            sself = str(self)
            self=AlgebraElement(self)
            return self+other

        elif isinstance(other, Monomial):
            sother = other.mon
            other = AlgebraElement(sother)
            return self+other
        elif isinstance(self, Monomial):
            sself = str(self)
            self=AlgebraElement(self)
            return self+other

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        """String representation of an algebra element"""

        s=""
        sself = sort(self.element)
        k=[]
        for i in sself.keys():
            k=k+[i]
        for i in range(0,len(sself.keys())):
            if i==0:
                s=s+str(sself[k[i]])+" " + str(k[i])
            elif sself[k[i]]<0:
                s=s + " " + str(sself[k[i]]) + " " + str(k[i])      
            else:
                s=s + " + " + str(sself[k[i]]) + " " + str(k[i])

        return s
        

    

#################################################################

def isMon(self):
    """Method to Check if a monomial is valid

    is associative or commutative?

    input:String-->output:True/False

    Quantities:
            ln = length of string
            let = number of letters
            lefpar = number of left parenteses
            rightpar = number of right parentheses
            

        
    """
        
    ln=0
    let=0
    leftpar=0
    rightpar=0
    str1=""
    i=0
    while i < len(self):
        if self[i] in letters:
            str1=str1+self[i]
            i=i+1
        elif self[i]=='(' or self[i]==')':
            str1=str1+self[i]
            i=i+1

        elif self[i] =='^':
            if i==0:
                return False
            elif not(self[i-1] in letters or self[i-1]==')'):
                return False
            elif self[i+1]=='{':
                x=2
                close=1 #to stop when the braces close
                while close>0:
                    if self[i+x] in digits:
                        x=x+1
                    elif self[i+x]=="}":
                        x=x+1
                        close=close-1
                    else:
                        return False
                i=i+x

            else:
                return False
        else:
            return False

    if len(str1)==1 or len(str1)==2 or len(str1)== 0:
        for i in str1:
            if i in letters:
                let=let+1
        if let==len(str1):
            return True
        else:
            return False
    else:
        for i in str1:
            if i in letters:
                let=let+1
            if i == '(':
                leftpar=leftpar+1
            if i==')':
                rightpar=rightpar+1

        if leftpar==rightpar and leftpar<let-1 and asso==1:
            return True

        if leftpar==rightpar and (leftpar==let-2 and asso==0):
            let1=0
            leftpar1=0
            rightpar1=0
            for i in range(0, len(str1)):
                if leftpar1==rightpar1:
                    if i==0:
                        if str1[i]=='(':
                            leftpar1=leftpar1+1
                        pass
                    else:
                        str2=str1[0:i]
                        if i==len(str1)-1:
                            return False
                        else:
                            str3=str1[i:len(str1)]
                            if len(str2)>2:
                                X1=isMon(str2[1:len(str2)-1])
                            else:
                                X1=isMon(str2)
                            if len(str3)>2:
                                X2=isMon(str3[1:len(str3)-1])
                            else:
                                X2=isMon(str3)
                            return (X1 and X2)
                if str1[i] in letters:
                    let1=let1+1
                elif str1[i]=="(":
                    leftpar1=leftpar1+1
                else:
                    rightpar1=rightpar1+1
                if leftpar1==rightpar1 and i==len(str1)-1:
                    return False
        else:
            return False


        
def standardise(self):
    """To rewrite a monomial is standard form
    string-->string
    is associate or commutative?
     Quantities:
         ln = length of string
         leftpar = number of left parentheses
         rightpar = ........ right .......
         let= .......... letters
    """

    ln = len(self)
    leftpar=0
    rightpar=0
    let=0
    

    if asso==1:
        mon=""
        for i in self:
            if i=="(" or i==")":
                pass
            else:
                mon = mon + i
        if comm==1:
            i=0
            while i <len(mon):
                if mon[i] in letters:
                    if i==0:
                        mon="#"+mon
                        i=i+2
                    else:
                        mon= mon[0:i]+"#"+mon[i:]
                        i=i+2
                else:
                    i=i+1
            monlist=mon.split("#")
            monlist.sort()
            mon="".join(monlist)
            return mon

    if asso ==0:
        if comm==0:
            return self
        elif comm==1:
            red=""
            for i in self:
                if i in letters:
                    let=let+1
                    red=red+i
            if let==1:
                return self
            elif let ==0:
                return self
            elif let==2:
                if "(" in self:
                    mon=self[1:len(self)-1]
                    i=0
                    while i < len(mon):
                        if mon[i] in letters:
                            if i==0:
                                mon="#"+mon
                                i=i+2
                            else:
                                mon= mon[0:i]+"#"+mon[i:]
                                i=i+2
                        else:
                            i=i+1
                    monlist=mon.split("#")
                    monlist.sort()
                    mon="".join(monlist)
                    mon="("+ mon + ")"
                    return mon

                else:
                    mon=self
                    i=0
                    while i < len(mon):
                        if mon[i] in letters:
                            if i==0:
                                mon="#"+mon
                                i=i+2
                            else:
                                mon= mon[0:i]+"#"+mon[i:]
                                i=i+2
                        else:
                            i=i+1
                    monlist=mon.split("#")
                    monlist.sort()
                    mon="".join(monlist)
                    return mon

            else:
                for i in range(0, ln+1):
                    if i==0:
                        if self[i]=="(":
                            leftpar=leftpar+1
                        else :
                            x=2
                                close=0
                                while close==0:
                                    if self[i+x]=="}":
                                        close=close+1
                                        x=x+1
                                    else:
                                        x=x+1
                            str1=self[0:i+x]
                            str3=standardise(str1)
                            str2=self[i+x:ln]
                            str4=standardise(str2)
                            mon=reorder(str3,str4)
                            return mon
    
                    elif leftpar==rightpar:
                        if i==ln:
                            str1=self[1:i-1]
                            str2=standardise(str1)
                            str3="("+str2+")"
                            return str3
                        else:
                            str1=self[0:i]
                            str3=standardise(str1)
                            str2=self[i:ln]
                            str4=standardise(str2)
                            mon=reorder(str3,str4)
                            return mon
                    elif self[i]=="(":
                        leftpar=leftpar+1
                    elif self[i]==")":
                        rightpar=rightpar+1
                    else:
                        pass
 
        #return self
    
def reorder(self, other):
    """Take two components of a monomial and and put them in a standard order.
        Only applicable in case of non-associative but commutative algebras.
        string + string --> string
        Quantities:
            lets = letters in self
            leto = letters in other
            rself = string containg just the letters in self
            rother = string containing just the letters in other
    """
    lets=0
    leto=0
    rself= ""
    rother= ""
    
    if comm==0:
        return self + other
        
    for i in self:
        if i in letters:
            lets=lets+1
            rself=rself+i

    for i in other:
        if i in letters:
            leto=leto+1
            rother=rother+i

    if lets > leto:
        mon=other+self
        return mon

    elif lets < leto:
        mon=self+other
        return mon

    else:
        if len(self)<len(other):
            mon=self+other
            return mon
        elif len(self)>len(other):
            mon=other+self
            return mon
        else:
            if rself<rother:
                mon=self+other
                return mon
            else:
                mon=other+self
                return mon

def sort(self):
    """sort dictionary in ascending order of keys"""

    if len(self.keys()) < 2:
        return self

    low, same, high = {}, {}, {}
    
    k=[]
    for i in self.keys():
        k=k+[i]
    #r=randint(0, len(e1.keys()) - 1)
    p = k[randint(0, len(self.keys()) - 1)]

    for i in self.keys():
        if i==p:
            same[i]=self[i]
        elif i<p:
            low[i]=self[i]
        elif i>p:
            high[i]=self[i]
    l=sort(low) 
    h=sort(high)
    e={}
    for i in l.keys():
        e[i]=l[i]
    for i in same.keys():
        e[i]=same[i]
    for i in h.keys():
        e[i]=h[i]
    return e


def idempotent(self):
    """To apply idempotent property to monomials"""
    
    mon=""
    leftpar=0
    rightpar=0
    let=0
    
    if idemp==0:
        return self
    
    
    for i in self:
        if (i in letters or i == "(" or i==")" ):
            mon = mon + i
        else:
            pass
        
    if asso==1:
        i=0
        while i < len(mon)-1 :
            if mon[i] == mon[i+1]:
                if i==0:
                    mon = mon[1:]
                else:
                    mon = mon[0:i] + mon[i+1:]
            else:
                i=i+1
        return mon
    
    elif asso==0:
        red=""
        for i in mon:
            if i in letters:
                let=let+1
                red=red+i
        if let==1:
            return mon
        if let ==0:
            return mon
        if let==2:
            if "(" in mon:
                imon=mon[1:len(mon)-1]
                if imon[0]==imon[1]:
                    return imon[0]
                else:
                    return mon
            else:
                if mon[0]==mon[1]:
                    return mon[0]
                else:
                    return mon

        for i in range(0, len(mon)+1):
            if i==0:
                if self[i]=="(":
                    leftpar=leftpar+1
                else :
                    str1=mon[0:i+1]
                    str3=idempotent(str1)
                    str2=mon[i+1:len(mon)]
                    str4=idempotent(str2)
                    str5=reorder(str3,str4)
                    if str5 == mon:
                        imon=str5
                    else:
                        imon=idempotent(str5)
                    return imon    
            elif leftpar==rightpar:
                if i==len(mon):
                    str1=mon[1:i-1]
                    str2=idempotent(str1)
                    if len(str2)==1:
                        imon=str2
                    else:
                        imon="("+str2+")"
                    return imon
                else:
                    str1=mon[0:i]
                    str3=idempotent(str1)
                    str2=mon[i:len(mon)]
                    str4=idempotent(str2)
                    str5=reorder(str3,str4)
                    if str5 == mon:
                        imon=str5
                    else:
                        imon=idempotent(str5)
                    return imon
            elif self[i]=="(":
                leftpar=leftpar+1
            elif self[i]==")":
                rightpar=rightpar+1
            else:
                pass
 
 
