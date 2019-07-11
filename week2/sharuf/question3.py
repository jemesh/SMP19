a = int(input("Enter the first number"))
b = int(input("Enter the Second number"))


def gcd(numerator, denominator, remainder):
    if remainder == 0:
      if denominator == 0:
        print(numerator, "is the GCD of", a, b)
      else:
        print(denominator, "is the GCD of", a, b)

    else:
        remainder = int(numerator % denominator)
        numerator = denominator
        denominator = remainder
        gcd(numerator, denominator, remainder)


if a > b:
    gcd(a, b, int(a % b))
else:
     gcd(b, a, int(b % a))

