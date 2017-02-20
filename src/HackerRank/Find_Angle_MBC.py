import math
def FindAngleMBC():
    import math
    degree_sign = u'\N{DEGREE SIGN}'
    ab,bc = float(raw_input()),float(raw_input())
    theta = str(int(90.0 - 180*math.acos(((ab**2+bc**2)**.5)/(2*bc))/(math.pi)))
    answer = list(theta)
    answer.append(degree_sign)
    return ''.join(answer)

a = FindAngleMBC()

print a


