time = int(input('enter the time in minutes \n'))
way = int(input('enter the way in kilometers \n'))
speed = float((way * 1000) / (time * 60))
print('speed is ' + str(speed) + ' meters per second')