from pathlib import Path
import sys


EX1_DIR = Path(__file__).resolve().parent.parent / "ex1"
if str(EX1_DIR) not in sys.path:
    sys.path.insert(0, str(EX1_DIR))
