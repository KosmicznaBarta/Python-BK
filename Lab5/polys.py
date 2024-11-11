def add_poly(poly1, poly2):
    length = max(len(poly1), len(poly2))
    result = [0] * length
    for i in range(length):
        a = poly1[i] if i < len(poly1) else 0
        b = poly2[i] if i < len(poly2) else 0
        result[i] = a + b
    return result

def sub_poly(poly1, poly2):
    length = max(len(poly1), len(poly2))
    result = [0] * length
    for i in range(length):
        a = poly1[i] if i < len(poly1) else 0
        b = poly2[i] if i < len(poly2) else 0
        result[i] = a - b
    return result

def mul_poly(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i, a in enumerate(poly1):
        for j, b in enumerate(poly2):
            result[i + j] += a * b
    return result

def is_zero(poly):
    return all(coef == 0 for coef in poly)

def eq_poly(poly1, poly2):
    while len(poly1) > 1 and poly1[-1] == 0:
        poly1.pop()
    while len(poly2) > 1 and poly2[-1] == 0:
        poly2.pop()
    return poly1 == poly2

def eval_poly(poly, x0):
    result = 0
    for coef in reversed(poly):
        result = result * x0 + coef
    return result

def combine_poly(poly1, poly2):
    result = [0]
    for coef in reversed(poly1):
        result = add_poly(mul_poly(result, poly2), [coef])

    while len(result) > 1 and result[-1] == 0:
        result.pop()
        
    return result

def pow_poly(poly, n):
    result = [1]
    for _ in range(n):
        result = mul_poly(result, poly)
    return result

def diff_poly(poly):
    result = [i * coef for i, coef in enumerate(poly)][1:]
    return result if result else [0]