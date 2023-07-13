
import re
#Define the find_Novowels function here
def find_Novowels(string):
  a = []
  vo=[]
  for x in string:
    for x in string:
    #print(len([char for char in x if char in "aeiouAEIOU"]))
       vo = re.findall(r'a|e|i|o|u', x)
       print(len(vo))
       if len(vo)>=0:
         string.remove(x)
    else:
        a.append(x)
        print("------")
    #print(string)

  '''for x in string:
    #print(len([char for char in x if char in "aeiouAEIOU"]))
    vo = re.findall(r'a|e|i|o|u', x)
    print(len(vo))
    if len(vo)>=0:
      string.remove(x)
    else:
      a.append(x)
    print("------")
    for x in string:
       a.append(x)'''

  return a
 
#Sample main section. 
#Do not remove the below portion of code. 
if __name__=='__main__':
        #count=int(input())
        inp_str=['avoid', 'build', 'create', 'book']
        '''for i in range(count):
                inp_str.append(input())'''
        output=find_Novowels(inp_str)
        if len(output)!=0:
                print('Strings without vowels:')
                for i in output:
                        print(i)
        else:
                print('No string found')