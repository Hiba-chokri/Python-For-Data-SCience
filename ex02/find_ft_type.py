def all_thing_is_obj(object: any) -> int:
    if(isinstance(object, 'str')):
        print(str , "is in the kitchen :", type(object))
    elif(isinstance(object, list)):
        print("List",type(object))
    else:
        print("object not foundd")
    return 42
    
all_thing_is_obj("brian")
