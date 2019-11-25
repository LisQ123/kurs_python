import random


class Player:
    """ Gracz w grze strzelance. """

    def blast(self, enemy):
        damage = random.randint(1, 10)
        print('Gracz razi wroga. Zadaje mu obrazenia na poziomie mocy', damage, '.\n')
        if damage > 3:
            enemy.die()
        else:
            enemy.win()
            enemy.yawn()


class Alien:
    """ Obcy w grze strzelance. """

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')


    def win(self):
        print('Obcy zjada gracza ze smakiem')


    def yawn(self):
        print('Obcy ziewa znudzony, przeciąga sie i mlaszczac z niesmakiem kladzie sie spac.')


if __name__ == '__main__':
    print('****** Smierc obcego *********\n')
    hero = Player()
    invader = Alien()
    hero.blast(invader)
    input('\n\nAby zakonczyc program, nacisnij klawisz Enter.')
