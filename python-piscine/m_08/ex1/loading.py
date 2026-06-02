from typing import Any


def is_modules_installed() -> bool:
    print("Checking dependencies:")
    status_code: int = 0
    try:
        import pandas  # type: ignore
        print(f"[OK] pandas: ({pandas.__version__}) - Data manipulation ready")
        status_code += 0
    except AttributeError:
        print("Import 'pandas' is not installed,"
              "\t\tTo install run: pip install pandas")
        status_code += 1
    try:
        import numpy  # type: ignore
        print(f"[OK] numpy: ({numpy.__version__}) - Numerical computation ready")
        status_code += 0
    except AttributeError:
        print("Import 'numpy' is not installed,"
              "\t\tTo install run: pip install numpy")
        status_code += 0
    try:
        import matplotlib  # type: ignore
        print(f"[OK] matplotlib: ({matplotlib.__version__})"
              f" - Visualization ready")
        status_code += 0
    except ModuleNotFoundError:
        print("Import 'matplotlib' is not installed,"
              "\t\tTo install run: pip install matplotlib")
        status_code += 1
    if status_code == 0:
        return True
    else:
        print("\n[Warning] Missing dependencies!")
        print("\nTo install with pip:\n\tpip install -r requirements.txt")
        print("[NOTE] Pip utilizes .txt file that can or not lock in a verimport ossion"
              " of a module or just a limit(ex. >=2.0, meaning after or "
              "including version 2.0)")
        print("\nTo install with Poetry:\n\tpoetry install ")
        print("[NOTE] Poetry utilizes .toml file and locks module"
              " versions for reproducibility porposes")
        print("")
        return False


def create_data() -> Any:
    import numpy as np
    return np.random.randint(0, 500, size=(32, 32))


def modify_data(data: Any) -> Any:
    import numpy as np
    return data.astype(float) * 1.2 + np.random.randint(-20, 21, size=data.shape)


def sort_data(matrix: Any) -> Any:
    import numpy as np
    return np.sort(matrix, axis=0)


def create_graph(matrix: Any) -> None:
    import pandas as pd
    import matplotlib.pyplot as plt # type: ignore
    
    df = pd.DataFrame(matrix)

    plt.figure(figsize=(8, 6))
    plt.imshow(df.values, cmap="viridis", interpolation="nearest")
    plt.colorbar(label="value")
    plt.title("Matrix heatmap")
    plt.tight_layout()
    plt.savefig("matrix_plot.png", dpi=150)
    plt.close()



def test_m8_ex1() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    
    if is_modules_installed():
        data = create_data()
        print("\nAnalyzing Matrix data...")
        modified_data = modify_data(data)
        print("Processing 1000 data points...")
        sorted_data = sort_data(modified_data)
        print("Generating visualization...")
        create_graph(sorted_data)

        print("\nAnalysis complete!")
        print("Results saved to: matrix_analysis.png")
    else:
        print("Nothing is installed!")
        return


if __name__ == "__main__":
    test_m8_ex1()
    # print(f"\n\n{sys.modules}")matrix_analysis.png
