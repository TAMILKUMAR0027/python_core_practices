class ProcessString:
    def ProcessString(self, text):
        print(text.upper())
        print(text[::-1])
        print(len(text))

    def ProcessString(self, text, count):
        print(text.upper())
        print(text[::-1])
        print(len(text))
        print("Count:", count)


if __name__ == "__main__":
    obj = ProcessString()
    obj.ProcessString("hello")
    obj.ProcessString("hello", 2)
