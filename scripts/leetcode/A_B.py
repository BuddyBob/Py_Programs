A = ''
B = ''
def check(A,B):
    if A == B:
        return True
    for i in range(len(A)):
        A = A[1:] + A[0]
        if A == B:
            return True
    return False
print(check(A,B))