def generate_almost_isosceles_pythagorean_triples(num_triples, skip_first=False):
    """
    Generate almost isosceles Pythagorean triples: a² + b² = c² where b = a + 1

    Uses recurrence: x' = 3x + 4y, y' = 2x + 3y

    Starting from x=1, y=1 yields: (3,4,5), (20,21,29), (119,120,169)...

    All generated triples satisfy b = a + 1, including (3,4,5).

    Args:
        num_triples: Number of triples to generate
        skip_first: If True, skip (3,4,5) and start from (20,21,29)

    Yields:
        Tuple[int, int, int]: (a, b, c) where a² + b² = c² and b = a + 1
    """
    x, y = (7, 5) if skip_first else (1, 1)

    for _ in range(num_triples):
        x, y = 3*x + 4*y, 2*x + 3*y
        a = x // 2
        b = a + 1
        c = y
        yield (a, b, c)

def verify_triple(a, b, c):
    """Verify that (a,b,c) is a valid almost isosceles Pythagorean triple"""
    return a*a + b*b == c*c and b == a + 1

if __name__ == "__main__":
    try:
        num_triples = int(input("Enter the number of almost isosceles Pythagorean triples to generate: "))
        if num_triples < 1:
            raise ValueError("Count must be positive")
    except ValueError as e:
        print(f"Invalid input: {e}")
        exit(1)

    skip = input("Skip (3,4,5)? [y/N]: ").lower().startswith('y')

    print(f"\nGenerating {num_triples} triple(s):")
    for i, triple in enumerate(generate_almost_isosceles_pythagorean_triples(num_triples, skip_first=skip), 1):
        a, b, c = triple
        assert verify_triple(a, b, c), f"Generated invalid triple: {triple}"
        print(f"{i:3d}: ({a}, {b}, {c})")