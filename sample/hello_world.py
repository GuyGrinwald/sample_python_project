import logging

import utils.logging_config  # isort:skip

logger = logging.getLogger(__name__)

class Greeter:
    def __init__(self) -> None:
        pass

    def say_hello(self):
        logger.info("Hello, World!")
        return "Hello, World!"

if __name__ == "__main__":
    # Use this in non-prod envs only
    greeter = Greeter()
    print(greeter.say_hello())
