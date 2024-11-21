
class StatusCode:
    """Represents the status code for operations."""
    def __init__(self, code):
        self.code = code

    def get_status_code(self):
        return self.code


class HelloWorldString:
    """Represents the HelloWorld string."""
    def __init__(self, string):
        self.string = string

    def get_hello_world_string(self):
        return self.string


class StringFactory:
    """Factory to create HelloWorldString objects."""
    _instance = None

    @staticmethod
    def get_instance():
        if StringFactory._instance is None:
            StringFactory._instance = StringFactory()
        return StringFactory._instance

    def create_hello_world_string(self, string):
        return HelloWorldString(string)


class PrintStrategy:
    """Defines a print strategy."""
    def __init__(self):
        self.output_stream = None

    def setup_printing(self):
        try:
            self.output_stream = open("output.txt", "w", encoding="utf-8")
            return StatusCode(0)
        except Exception as e:
            print(f"Setup failed: {e}")
            return StatusCode(-1)

    def print(self, hello_world_string):
        try:
            self.output_stream.write(hello_world_string.get_hello_world_string() + "\n")
            self.output_stream.flush()
            return StatusCode(0)
        except Exception as e:
            print(f"Printing failed: {e}")
            return StatusCode(-1)

    def close(self):
        if self.output_stream:
            self.output_stream.close()


class PrintStrategyFactory:
    """Factory to create PrintStrategy objects."""
    _instance = None

    @staticmethod
    def get_instance():
        if PrintStrategyFactory._instance is None:
            PrintStrategyFactory._instance = PrintStrategyFactory()
        return PrintStrategyFactory._instance

    def create_print_strategy(self):
        strategy = PrintStrategy()
        code = strategy.setup_printing()
        if code.get_status_code() != 0:
            raise RuntimeError(f"Failed to create PrintStrategy: {code.get_status_code()}")
        return strategy


class HelloWorldImplementation:
    """Implementation of HelloWorld."""
    def get_hello_world_string(self):
        factory = StringFactory.get_instance()
        return factory.create_hello_world_string("Hello, World!")

    def get_print_strategy(self):
        factory = PrintStrategyFactory.get_instance()
        return factory.create_print_strategy()

    def print(self, strategy, hello_world_string):
        return strategy.print(hello_world_string)


class HelloWorldFactory:
    """Factory to create HelloWorldImplementation objects."""
    _instance = None

    @staticmethod
    def get_instance():
        if HelloWorldFactory._instance is None:
            HelloWorldFactory._instance = HelloWorldFactory()
        return HelloWorldFactory._instance

    def create_hello_world(self):
        return HelloWorldImplementation()


# Main execution
if __name__ == "__main__":
    factory = HelloWorldFactory.get_instance()
    hello_world = factory.create_hello_world()

    hello_world_string = hello_world.get_hello_world_string()
    print_strategy = hello_world.get_print_strategy()

    status_code = hello_world.print(print_strategy, hello_world_string)
    if status_code.get_status_code() != 0:
        raise RuntimeError("Failed to print.")

    print_strategy.close()
    