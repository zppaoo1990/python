#coding=utf-8
#装饰器
def log(level,*args,**kvargs):
    print level
    def inner(func):
        def warraper(*args,**kvargs):
            print level,'before calling',func.__name__
            print 'args',args,'kvargs',kvargs
            func(*args,**kvargs)
            print level,'end calling',func.__name__
        return warraper
    return inner


@log(level='IMPORTANT')
def hello(name,age):
    print 'hello',name,age

if __name__=='__main__':
    hello(name='zhangpan',age=22)