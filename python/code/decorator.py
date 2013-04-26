def except_wrapper(handler='default_handler'):
    def exec_decorator(func):
        hd = getattr(Handler, handler)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                hd(e)
        return wrapper
    return exec_decorator
class Handler(object):
    def __init__(self):
        pass
    @staticmethod
    def default_handler(e):
        print "this is a default handler"
        print e
    @staticmethod  
    def simple_handler(e):
        print "this is a simple handler"
        print e
class API(object):
    def __init__(self):
        pass
    @except_wrapper()
    def test1(self):
       raise Exception("test1 exception")
    @except_wrapper('simple_handler')
    def test2(self):
       raise Exception("test2 excetpion")
api = API()
api.test1()
api.test2()
