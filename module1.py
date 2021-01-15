def decorator(axelarator):
    def wraper(v0,v,t):
        a=axelarator(v,v0,t)
        s=v0*t+(a*t)**2/2
        print("ускоренние",s)
    return wraper
@decorator
def axelarator(v,v0,t):
    a=(v-v0)/t
    print("перемещение",a)
    return a
class MyException(BaseException):
    pass

try:
    v=int(input())
    v0=int(input())
    t=int(input())
    if t<=0:
        raise MyException("t НЕ ДОЛЖНО БЫТЬ 0")
    axelarator(v,v0,t)
except ValueError:
    print("вводите цифры")
except MyException:
    print("Завершение программы")





