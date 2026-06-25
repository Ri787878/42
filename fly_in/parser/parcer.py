from zone_network import InvalidConfiguration


def file_interpreter(filename: str) -> dict:
    with open(filename, "r") as f:
        content = f.read()

    lines: list[str] = content.splitlines()
    nb_drones: int = -1
    start_hub: str = ""
    hubs: list[str] = []
    end_hub: str = ""

    # Check if file starts with nb_drones and skips comments
    for line in lines:
        if line.startswith("#"):
            continue
        else:
            if not line.startswith("nb_drones:"):
                raise InvalidConfiguration(
                        "[ERROR] Configuration file doen't start"
                        " with 'nb_drones'.")
            elif line.startswith("nb_drones:"):
                nb_drones = int(line.removeprefix("nb_drones:"))
                break

    for line in lines:
        if line.startswith("#"):
            continue

        if line.startswith("start_hub:") and start_hub:
            raise InvalidConfiguration(
                "[ERROR] There are 2 'start_hub'"
                "configurations.")
        elif line.startswith("start_hub:"):
            start_hub = line.removeprefix("start_hub:")

        if line.startswith("hub:"):
            hubs.append(line.removeprefix("hub:"))

        if line.startswith("end_hub:") and end_hub:
            raise InvalidConfiguration(
                "[ERROR] There are 2 'end_hub'"
                "configurations.")
        elif line.startswith("end_hub:"):
            end_hub = line.removeprefix("end_hub:")

        if line.startswith("connection:"):
            pass

    res: dict = {
        "nb_drones": nb_drones,
        "start_hub": start_hub,
        "end_hub": end_hub,
        "hubs": hubs}
    split_file(content)

    return res


def split_file(content: str) -> list[str]:
    pass
    return [""]
