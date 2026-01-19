class Interpreter:
    def __init__(self):
        self.stack = []   # representing the stack as a list, stack is needed to load values & instructions there


    def LOAD_VALUE(self, value):
        self.stack.append(value)

    def PRINT_ANSWER(self):
        answer = self.stack.pop()
        print(answer)

    def ADD_TWO_VALUES(self):
        first_value = self.stack.pop()
        second_value = self.stack.pop()
        answer = first_value + second_value
        self.stack.append(answer)

    def RUN_CODE(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        values = what_to_execute["values"]

        for i in instructions:
            instruction, arg = i
            if instruction == "LOAD_VALUE":
                value = values[arg]  # get the number and load it
                self.LOAD_VALUE(value)

            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()

            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()


###### TESTING
what_to_execute = {
    "instructions": [("LOAD_VALUE", 0),  # the first number
                     ("LOAD_VALUE", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "values": [7, 5] }

interpreter = Interpreter()
interpreter.RUN_CODE(what_to_execute)