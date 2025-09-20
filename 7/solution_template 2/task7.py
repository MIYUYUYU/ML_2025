def find_modified_max_argmax(L,f):
    a = [ f(x) for x in L if type(x) is int]
    return (m:=max(a),a.index(m)) if a else ()