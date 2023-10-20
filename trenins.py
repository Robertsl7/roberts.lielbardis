nenodots = input('Vai Jums ir kāds  nenodots izdevums? (j/n): ')
if nenodots == "j":
    print('Jūs nedrīkstat neko izņemt')
elif nenodots == 'n':
    pieprasits = input ('Vai šī publikācija ir pieprasīta (j/n)')
    if pieprasits == 'j':
        print('Izsniedz uz 2 dienām')
    elif pieprasits == 'n':
        zurnāls = input('Vai publikācija ir žurnāls')
        if zurnāls == 'j':
            print('Izsniedz uz 7 dienām')
        elif zurnāls == 'n':
            students = input('Vai jūs esat students?(j/n)')
            if students == 'j':
                print('Izsniedz uz 14 dienām')
            elif students == 'n':
                print('Izsniedz uz 28 dienām')
