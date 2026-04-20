def closest_integer(value):
    from decimal import Decimal, ROUND_HALF_UP
    d = Decimal(value)
    return int(d.to_integral_value(rounding=ROUND_HALF_UP))

