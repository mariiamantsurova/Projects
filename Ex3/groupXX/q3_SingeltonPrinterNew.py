class PrinterQueue:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.queue = []
        return cls._instance

    def add_to_queue(self, document):
        self.queue.append(document)
        print(f"Added '{document}' to the queue.")

    def print_next(self):
        if self.queue:
            document = self.queue.pop(0)
            print(f"Printing: {document}")
        else:
            print("The queue is empty. No documents to print.")

    def view_queue(self):
        print("Current queue:", self.queue)


if __name__ == '__main__':

    # First instance
    printer1 = PrinterQueue()
    printer1.add_to_queue("Document1.pdf")
    printer1.add_to_queue("Document2.pdf")

    # Second instance
    printer2 = PrinterQueue()
    printer2.view_queue()

    # Demonstrating the singleton property
    printer2.print_next()
    printer1.view_queue()

    print(printer1 is printer2)
    print(printer1.__dict__)
    print(printer2.__dict__)

