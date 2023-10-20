izdevums = (input('Žurnāls vai grāmata '))
persona = (input('personāls vai students: '))
pieprasījums = (input('Pieprasīta vai nē: ' ))
nodevis = (input('Nodevis jā vai nē: ' ))


if nodevis == 'nē':
    print('Neesi nodevis grāmatas')
elif pieprasījums == 'jā':
    print('Grāmata tiek izsniegta uz divam dienam')
elif izdevums == 'grāmata':
    if persona == 'personāls':
        print('28 dienām')
    
