def any_keyword_args(**kwargs):
    return kwargs

print(type(any_keyword_args(one=1, two=2, three=3)))