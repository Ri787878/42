# import sys
def check_installed_modules() -> None:
    print("Checking dependencies:")
    try:
        import pandas  # type: ignore
        print(f"[OK] pandas: ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        print("Import 'pandas' is not installed,"
              "\t\tTo install run: pip install pandas")
    try:
        import numpy  # type: ignore
        print(f"[OK] numpy: ({numpy.__version__}) - Numerical computation ready")
    except ImportError:
        print("Import 'numpy' is not installed,"
              "\t\tTo install run: pip install numpy")
    try:
        import matplotlib  # type: ignore
        print(f"[OK] matplotlib: ({matplotlib.__version__})"
              f" - Visualization ready")
    except ImportError:
        print("Import 'matplotlib' is not installed,"
              "\t\tTo install run: pip install matplotlib")


def test_m8_ex1() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    check_installed_modules()
    pass


if __name__ == "__main__":
    test_m8_ex1()
    # print(f"\n\n{sys.modules}")
