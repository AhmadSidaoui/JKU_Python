def compose(*functions):
    def composed_function(x):
        for func in reversed(functions):
            x = func(x)
        return x
    return composed_function