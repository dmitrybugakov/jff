from jff.algorithms.stanford import multiplication, karatsuba


def main() -> None:
    print(multiplication(x="1234", y="2341", n=4))
    print(karatsuba(x="1234", y="2341", n=4))


if __name__ == "__main__":
    main()
