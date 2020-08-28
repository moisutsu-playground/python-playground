from importlib import reload

def auto_reload(module):
    def _inner():
        reload(module)
        return module
    return _inner
