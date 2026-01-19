class Interpreter:
    def __init__(self):
        self.stack = []   # representing the stack as a list, stack is needed to load values & instructions there
        self.environment = {}

    def STORE_NAME(self, name):
        val = self.stack.pop()
        self.environment[name] = val

    def LOAD_NAME(self, name):
        val = self.environment[name]
        self.stack.append(val)

    def parse_argument(self, instruction, argument, what_to_exec):
        """ Understand what the argument to each instruction means."""
        numbers = ["LOAD_VALUE"]
        names = ["LOAD_NAME", "STORE_NAME"]

        if instruction in numbers:
            argument = what_to_exec["values"][argument]

        elif instruction in names:
            argument = what_to_exec["names"][argument]

        return argument


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

        for i in instructions:
            instruction, arg = i
            arg = self.parse_argument(instruction, arg, what_to_execute)

            if instruction == "LOAD_VALUE":
                self.LOAD_VALUE(arg)

            elif instruction == "ADD_TWO_VALUES":
                self.ADD_TWO_VALUES()

            elif instruction == "PRINT_ANSWER":
                self.PRINT_ANSWER()

            elif instruction == "STORE_NAME":
                self.STORE_NAME(arg)

            elif instruction == "LOAD_NAME":
                self.LOAD_NAME(arg)

    def execute(self, what_to_execute):  # better way of the above func
        instructions = what_to_execute["instructions"]

        for i in instructions:
            instruction, arg = i
            arg = self.parse_argument(instruction, arg, what_to_execute)
            ## Give me the method of this object (interpreter) whose name is stored in the string instruction
            bytecode_method = getattr(self, instruction)  # get instruct. replacement for the if-else for each instruct
            if arg is None:
                bytecode_method()  # some methods don't take args, e.g. ADD-TWO_VALUES
            else:
                bytecode_method(arg)





###### TESTING
what_to_execute2 = {
    "instructions": [("LOAD_VALUE", 0),  # the first number
                     ("LOAD_VALUE", 1),  # the second number
                     ("ADD_TWO_VALUES", None),
                     ("PRINT_ANSWER", None)],
    "values": [7, 5] }

what_to_execute3 = {
        "instructions": [("LOAD_VALUE", 0),
                         ("LOAD_VALUE", 1),
                         ("ADD_TWO_VALUES", None),
                         ("LOAD_VALUE", 2),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "values": [7, 5, 8] }

what_to_execute4 = {
        "instructions": [("LOAD_VALUE", 0),
                         ("STORE_NAME", 0),
                         ("LOAD_VALUE", 1),
                         ("STORE_NAME", 1),
                         ("LOAD_NAME", 0),
                         ("LOAD_NAME", 1),
                         ("ADD_TWO_VALUES", None),
                         ("PRINT_ANSWER", None)],
        "values": [1, 2],
        "names":   ["a", "b"] }


interpreter = Interpreter()
interpreter.RUN_CODE(what_to_execute4)