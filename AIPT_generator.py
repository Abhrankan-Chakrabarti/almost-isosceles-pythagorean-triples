def generate_almost_isosceles_pythagorean_triples(num_triples):
    x, y = 1, 1
    count = 0
    while count < num_triples:
        x, y = 3*x + 4*y, 2*x + 3*y
        a = x // 2
        b = a + 1
        c = y
        yield (a, b, c)
        count += 1

num_triples = int(input("Enter the number of almost isosceles Pythagorean triples to generate: "))
triples = generate_almost_isosceles_pythagorean_triples(num_triples)
for i, triple in enumerate(triples):
    print(i, triple)