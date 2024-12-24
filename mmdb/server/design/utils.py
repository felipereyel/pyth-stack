from functools import wraps


from mmdb.server.design.pages import Page


def page_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        title, content = func(*args, **kwargs)
        return Page(title=title, Child=content)

    return wrapper
