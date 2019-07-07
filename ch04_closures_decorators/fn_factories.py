def raise_to(exp):
    def raise_to_pow(x):
        return pow(x, exp)
    return raise_to_pow