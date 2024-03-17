def NULL_not_found(object :any) -> int:
    if(isinstance(object, type(None))):
        print("Nothing:None", type(object))
    elif(isinstance(object, float)):
        print("Float", type(object))
    elif(isinstance(object, int)):
        print("Integer", type(object))
    elif(isinstance(object, type(bool))):
         print("Boolean", type(object))
    else:
          print("object not found")
          return(1)
    return(0)


Nothing = None
Garlic = float("NaN")
zero = 0
fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(zero)
NULL_not_found(fake)
NULL_not_found("nfg")