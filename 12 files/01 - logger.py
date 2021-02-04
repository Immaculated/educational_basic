from datetime import datetime
def logger(text, filename = 'log.data'):
    now = datetime.now()
    with open('log.data','a') as file:
        file.write(datetime.strftime(now, "%Y.%m.%d %H:%M:%S ") + text + '\n')
logger('Error! Check ur data!')
!more log.data