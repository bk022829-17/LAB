#Binary Search 	

def split(data,number,mini,maxim):
    if(maxim>=mini):
        mid = int((mini+maxim) / 2)
        if (data[mid] == number):
            return mid
        elif (data[mid] > number):
            return split(data,number,mini,mid-1)
        else:
            return split(data,number,mid+1,maxim)
    else:
        return False

def convert(data):
	converted= []
	for i in range (0,(len(data)-1)):
		converted.append(ord(data[i])-97)
	return converted
    
        
def binary_Search(data,number):
	if (type(data[0])==str):
		number = ord(number) - 97
		data = convert(data)
	data.sort()
	return(split(data,number,0,(len(data)-1)))
    #result=split(data,number,0,(len(data)-1))
    # if (result != False):
    #     print("value found on index",result)
    # else:
    #     print("NOT found")


  
if __name__ == "__main__":
	binary_Search()
