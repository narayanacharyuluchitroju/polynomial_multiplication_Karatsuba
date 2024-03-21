import sys


def read_input(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if count == 0:
                n = int(line)
            elif count == 1:
                l1 = [int(i) for i in line.split(" ")]
            elif count == 2:
                l2 = [int(i) for i in line.split(" ")]
            count += 1
    return n, l1, l2


def karatsuba_mul(n1,n2,n):
    if (n == 1):
        return n1*n2
    else:
        m = n//2
        a = n1 // (2**m)
        b = n1 % (2**m)
        c = n2 // (2**m)
        d = n2 % (2**m)
        e = karatsuba_mul(a,c,m)
        f = karatsuba_mul(b,d,m)
        g = karatsuba_mul((a-b),(c-d),m)
        return (2**(2*m))*e + (2**m)*(e+f-g) + f

def karatsuba_poly_multiply(p1, p2):
    # Find the max  length of the polynomials
    n = max(len(p1), len(p2))

    # Base case: If the polynomial is a constant
    if n == 1:
        return [p1[0] * p2[0]]

    # Split the polynomials into halves
    m = n // 2
    a = p1[:m]
    b = p1[m:]
    c = p2[:m]
    d = p2[m:]

    # Recursively compute the products
    ac = karatsuba_poly_multiply(a, c)
    bd = karatsuba_poly_multiply(b, d)

    # Extend and pad the polynomials with zeros
    m = max(len(a), len(b), len(c), len(d))
    a_extended = a + [0] * (m - len(a))
    b_extended = b + [0] * (m - len(b))
    c_extended = c + [0] * (m - len(c))
    d_extended = d + [0] * (m - len(d))

    # Add the extended polynomials
    a_plus_b = [a_extended[i] + b_extended[i] for i in range(m)]
    c_plus_d = [c_extended[i] + d_extended[i] for i in range(m)]

    # Recursively compute the product of the sums
    ad_plus_bc = karatsuba_poly_multiply(a_plus_b, c_plus_d)
    if len(ac) < len(bd):
        ac = ac + [0] * (len(bd) - len(ac))

    # Combine the products to get the final result
    result = [0] * (2 * n - 1)
    for i in range(len(ac)):
        result[i] += ac[i]
    if n % 2 == 0:
        m = n // 2
    else:
        m = len(ac) - m
    for i in range(len(ad_plus_bc)):
        result[i + m] += ad_plus_bc[i] - ac[i] - bd[i]
    for i in range(len(bd)):
        result[len(result) - len(bd) + i] += bd[i]

    return result

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py input_file_name.txt")
        sys.exit(1)

    input_file_path = sys.argv[1]
    n,p1,p2 = read_input(input_file_path)
    result = karatsuba_poly_multiply(p1, p2)
    print(result)
