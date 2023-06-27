print("WEL_COME TO KBC")
question_list = [
    "How many continents are there?",              # first question
    "What is the capital of India?",            # second question
    "NG mei kaun se course padhaya jaata hai?"    # third question
    ""
]

options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]

shorted_option=[[" ( 3 ) seven"," ( 4 ) eight"],[" ( 2 ) bhopal"," ( 4 ) Delhi"],[" ( 1 ) software engineering"," ( 3 ) tourism"]]
solution_list=[3,4,1]
amount_list=[5000,10000,50000]
i=0
while i<len(question_list):
    print(i+1,".",question_list[i])
    j=0
    while j<len(options_list[i]):
        print("","(",j+1,")",options_list[i][j])
        j+=1
    life_line=input("Do you want life line y/n? :- ")
    if life_line=="y":
        a=0
        while a<1:
            b=0
            while b<len(shorted_option[a]):
                print("",shorted_option[i][b])
                b+=1
            a+=1
    Answer=int(input("Choose your answer :- "))
    if Answer==solution_list[i]:
        print("","hurrey!! your answer is correct")
        print("","you won",amount_list[i])
    else:
        print("so sad!!! your answer is wrong \nGame over")
        break
    i+=1
print("congratulations!! You won the game")
