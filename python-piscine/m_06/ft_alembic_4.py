import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reached")
print("This will raise an exception!")
try:
    print(alchemy.create_earth())
except Exception as e:
    tb = e.__traceback__
    lines: list[str] = []
    lines.append("Testing the hidden create_earth: Traceback (most recent call last):\n")
    while tb is not None:
        frame = tb.tb_frame
        lines.append(f'  File "{frame.f_code.co_filename}", line {tb.tb_lineno}, in {frame.f_code.co_name}\n')
        tb = tb.tb_next
    lines.append(f"\n{e.__class__.__name__}: {e}\n")
    print(''.join(lines), end='')
# print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
