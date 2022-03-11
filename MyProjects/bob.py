def editName(name):

    print(name[0].lower(), name[1].lower(), name[2].lower(), name[4].upper(), name[5], name[6], name[7], name[8],
          name[10].upper(), name[11], name[12], name[13], name[14], name[15], sep='')
    reject=name.__contains__('-')
    reject2=name.__contains__(' ')
    reject3=name.__contains__('*')

    if (name.__contains__(' ') and name.__contains__('*' )  and name.__contains__('-')):
        print(name.__delattr__(str(' ')))


name = 'BOB loves-coding'
name1='cats AND*Dogs-are Awesome'
editName(name)
editName(name1)