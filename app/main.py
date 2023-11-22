"""Sample main module"""


def hello_dss(name: str = "Dear Developer") -> str:
    """Returns formatted welcome message

    Args:
        name (str, optional): Name of welcomed person. Defaults to 'Dear Developer'.

    Raises:
        ValueError: If wrong data type passed

    Returns:
        str: Welcome message
    """
    if isinstance(name, str):
        return f"{name}, welcome in this sample repository!"
    else:
        msg = f"Wrong input data type. I need str, you gave me {type(name)}"
        raise ValueError(msg)


if __name__ == "__main__":
    print(hello_dss())
