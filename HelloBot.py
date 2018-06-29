
DIRECTION = 'NESW'

_currentPositionX = 0
_currentPositionY = 0
_currentFacing = 0
_step = ''

input = "W55555RW555555W444444W1"
def walk():
    global _step, _currentPositionX, _currentPositionY, _currentFacing
    if _step == '':
        return None

    # print('Move ' + _step)  
    if DIRECTION[_currentFacing] == 'N':
        _currentPositionY += int(_step)
    elif DIRECTION[_currentFacing] == 'E':
        _currentPositionX += int(_step)
    elif DIRECTION[_currentFacing] == 'S':
        _currentPositionY -= int(_step)
    elif DIRECTION[_currentFacing] == 'W':
        _currentPositionX -= int(_step)  
    #reset step    
    _step = ''  
    return None 

def convertDirectionCharToString(charDirection):
    if charDirection == 'N':
        return 'North'
    elif charDirection == 'E':
        return 'East'
    elif charDirection == 'S':
        return 'South'
    elif charDirection == 'W':
        return 'West'

i = 0
while i < len(input):    
    if input[i] == 'R':
        walk()
        if _currentFacing == 3:
            _currentFacing = -1            
        _currentFacing += 1
    elif input[i] == 'L':
        walk()
        if _currentFacing == 0:
            _currentFacing = 4
        _currentFacing -= 1
    elif input[i] == 'W':
        walk()
        i += 1
        continue 
    else:
        _step += input[i] 

    i += 1

walk()
print('X: ' + str(_currentPositionX) + ' Y: ' + str(_currentPositionY) + ' Direction: ' + convertDirectionCharToString(DIRECTION[_currentFacing]))
