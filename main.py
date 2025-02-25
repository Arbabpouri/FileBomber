import os
from uuid import uuid1


__FILE_SIZE__ = 1024 * 1024
__FILE_NUMBER__ = 10

def create_file() -> None:
    with open(f"{uuid1()}.bin", "wb") as file:
        file.write(os.urandom(__FILE_SIZE__))


if __name__ == "__main__":
    for i in range(__FILE_NUMBER__):
        create_file()
