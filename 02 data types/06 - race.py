h1,m1,s1 = map(int, input('enter the time of finish for 1st sportsman(h:m:s)\n').split(':'))
seconds1 = int(h1 * 3600 + m1 * 60 + s1)
h2,m2,s2 = map(int, input('enter the time of finish for 2nd sportsman(h:m:s)\n').split(':'))
seconds2 = int(h2 * 3600 + m2 * 60 + s2)
if seconds2 <= seconds1:
    print('2nd cant be earlier than 1st, check your data')
else:
    print('time difference is ' + str(seconds2 - seconds1) + ' seconds')