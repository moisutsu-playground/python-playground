class Chain:
    def print_chain(self, display: str):
        print(display, end="")
        return self

if __name__ == "__main__":
    chain = Chain()
    chain.print_chain("Hello, ").print_chain("World").print_chain("!!").print_chain("\n")
