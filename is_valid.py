#==============================================================#
#   Known Bugs: none
#   need to work on: range validation function
#==============================================================#



def length_valid(data,length,option):
    if option==1:
        if len(data)==length:
            return True
        return  False
    if option==2:
        if len(data)>=



def range_valid(data,hi,lo):
    #code to check that data between hi and lo
    #return True/False
    pass



if __name__=="__main__":
    try:
        print(length_valid(data=2,length="2",option=1))
    except:
        print("error")
