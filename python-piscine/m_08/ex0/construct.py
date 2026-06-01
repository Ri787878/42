import sys
import os
import site


def get_venv_status(env_status: bool) -> str:
    if env_status:
        return "Welcome to the construct"
    else:
        return "You're still plugged in"


def get_venv_name(env_status: bool) -> str:
    if env_status:
        return os.environ['VIRTUAL_ENV']
    else:
        return "None detected"


def check_enviroment() -> bool:
    if 'VIRTUAL_ENV' in os.environ:
        return True
    else:
        return False


def get_package_location() -> str:
    return site.getsitepackages()[0]


def test_m8_ex0() -> None:
    enviroment_status: bool = check_enviroment()


    print(f"\nMATRIX STATUS: {get_venv_status(enviroment_status)}\n")

    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {get_venv_name(enviroment_status)}\n")

    if enviroment_status:

        print("SUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting the global system.\n")
        print(f"Package installation path:\n{get_package_location()}")
         
    else:
        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\Scripts\activate # On Windows\n"
              "\nThen run this program again.")

if __name__ == "__main__":
    test_m8_ex0()