class PrinterQueue:
    class __Instance:
        def __init__(self):
            self.queue = []

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

    _instance = None

    def __init__(self):
        if not PrinterQueue._instance:
            PrinterQueue._instance = PrinterQueue.__Instance()

    def __getattr__(self, name):
        return getattr(self._instance, name)


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

    # B.
    # In the original code:
    # The singleton is implemented by overriding __new__, ensuring all references point to the same object.
    # This makes printer1 and printer2 identical and their __dict__ the same.

    # In the new code:
    # The singleton state is encapsulated in the __Instance object,
    # and PrinterQueue serves as a proxy. This keeps printer1
    # and printer2 as separate objects with shared state and we do not create or initialize
    # any attributes on the PrinterQueue instance that is why __dict__ is empty for
    # both

    # C.
    print(PrinterQueue._instance.__dict__)
# the __dict__ that contains the queue resides in the __Instance object