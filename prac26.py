def expanding(a):
    for i in range(len(a)) :
        success = (a[i+1]-a[i])<(a[i+2]-a[i+1]) 
        if not success:
            return False
    return True        
user_input = list(map(int,input('Enter space separated Numbers: ').split()))
boolean_result = expanding(user_input)
print(boolean_result)