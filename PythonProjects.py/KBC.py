# ! we will make a list of questios and answers
result = 0
questions = [
    'What is the capital of india?',
    'What is the symbol of Potassium?',
    'Which party did Hitler belong to?',
    'Which was the first artificial satellite of earth?',
    'what was the first vaccine of?'
]
answers = [
    'NewDelhi',
    'K',
    'Nazi',
    'Sputnik1',
    'Smallpox'
]
value = [
    '1000',
    '5000',
    '7500',
    '10000',
    '20000'
]
def yesorno():
    while True:
        ans = input('Do you want to palay KBC?')
        if ans.lower() == 'yes':
            return 'Sure lets start the game.'
        else:
            continue

print(yesorno())
def question(a):
    Points = result
    print(questions[a])
    ans1 = input('enter your answer:')
    if ans1.lower() == answers[a].lower():
        print('Great thats correct!')
        Points += int(value[a])
        print(Points)
    else:
        return Points          
question(0)
question(1)
question(2)
question(3)
question(4)
print(f'your final result was:{result}')