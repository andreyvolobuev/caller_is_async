import inspect


def caller_is_async(self, depth: int = 2) -> bool:
    """
    @param depth: how deep into the stack are we looking
    """
    stack = inspect.stack()
    caller = stack[depth][0]
    module = inspect.getmodule(caller)
    obj = caller.f_locals.get("self")
    if obj:
        cls_name = obj.__class__.__name__
        cls = getattr(module, cls_name)
        method_name = caller.f_code.co_name
        method = getattr(cls, method_name)
        return inspect.iscoroutinefunction(method)

