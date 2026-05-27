def wordOfInteger(n,dic):
    result=''
    for i in n:
      if(i=='0'):
        result+=(dic['0'])
      elif i=='1':
        result+=(dic['1'])
      elif i=='2':
        result+=(dic['2'])
      elif i=='3':
        result+=(dic['3'])
      elif i=='4':
        result+=(dic['4'])
      elif i=='5':
        result+=(dic['5'])
      elif i=='6':
        result+=(dic['6'])
      elif i=='7':
        result+=(dic['7'])
      elif i=='8':
        result+=(dic['8'])
      else:
        result+=(dic['9'])  
    return result
        

n=input("Enter the interger: ")
dic={'0':'Zero ','1':'One ','2':'Two ','3':'Three ','4':'Four ','5':'Five ','6':'Six ','7':'Seven ','8':'Eight ','9':'Nine '}
print(wordOfInteger(n,dic))
