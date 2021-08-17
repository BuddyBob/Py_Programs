questions = [
    'this then that',
    'this'
]
items = {'oranges':8,'apples':2}
question = (input('What would you like to do: '))
if question == questions[0]:
    question = (input('Enter you items comma seperated: '))
    question = question.split(',')
    if len(question) == len(items.keys()):
        for i in range(len(items.keys())):
            print()