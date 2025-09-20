def find_modified_max_argmax(L,f):
    M = [f(x) for x in L if type(x) is int]
    return (max(M),M.index(max(M))) if M else ()