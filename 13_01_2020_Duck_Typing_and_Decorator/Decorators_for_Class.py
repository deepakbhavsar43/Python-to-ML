def fancy_intro(self):
    print("I am Deepak Bhavsar.")


def fancy_domain(self):
    print("From Machine Learning domain.")


def decorate(c):
    c.__init__=fancy_intro
    c.domain=fancy_domain
    return c


if __name__=='__main__':
    @decorate
    class MyName:
        def intro(self):
            print('Intern in 1Rivet.')


    person=MyName()
    person.intro()
    person.domain()