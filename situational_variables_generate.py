import openai

openai.api_key = ""
#for filling the variables for exiting variables from the situation given
def situational_variables_generate(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "make a number of variables for python to explain the situation given by prompt, when you answer give as list such as [var1=value, var2=value, var3=value] but don't give extra stuff other than [], try mix number and letter as less as possible"},
      {"role": "user", "content": prompt},
    ]
)    
    list1=response['choices'][0]['message']['content']
    #delete [] from string
    list1=list1[1:-1]
    #split string into list
    list1=list1.split(", ")
    #make dictionary from list
    dict1={}
    for i in list1:
        dict1[i.split("=")[0]]=i.split("=")[1]
    #try change value of dict1 into int and it is possible then change it
    for i in dict1:
        try:
            dict1[i]=int(dict1[i])
        except:
            pass
    #try change value of dict1 into boolean  and it is possible then change it
    for i in dict1:
        if dict1[i]=="True":
            dict1[i]=True
        elif dict1[i]=="False":
            dict1[i]=False

    return dict1