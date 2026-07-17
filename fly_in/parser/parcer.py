from models import InvalidConfiguration


class Parcer():
    def file_interpreter(
        self,
        filename: str
    ) -> dict[str, str | list[str] | list[tuple[str, str, int]]]:
        with open(filename, "r") as f:
            content = f.read()

        lines: list[str] = content.splitlines()
        nb_drones: str = ""
        start_hub: str = ""
        hubs: list[str] = []
        end_hub: str = ""
        connections_list: list[tuple[str, str, int]] = []

        # Check if file starts with nb_drones and skips comments
        for line in lines:
            if line.startswith("#") or line == "":
                continue
            else:
                if not line.startswith("nb_drones:"):
                    raise InvalidConfiguration(
                            "[ERROR] Configuration file doen't start"
                            " with 'nb_drones'.")
                elif line.startswith("nb_drones:"):
                    nb_drones = line.removeprefix("nb_drones:")
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

            elif line.startswith("connection:"):
                raw = line.removeprefix("connection:").strip()

                bracket_i = raw.find("[")
                if bracket_i != -1:
                    core = raw[:bracket_i].strip()
                    meta = raw[bracket_i:].strip("[] ").split()
                else:
                    core = raw
                    meta = []

                parts = core.split("-")
                if len(parts) != 2:
                    raise InvalidConfiguration(f"[ERROR] Invalid connection "
                                               f"format: '{line}'")

                left_name = parts[0].strip()
                right_name = parts[1].strip()

                cap = 1
                for token in meta:
                    if token.startswith("max_link_capacity="):
                        cap = int(token.split("=", 1)[1].strip())

                connections_list.append((left_name, right_name, cap))

        res: dict[str, str | list[str] | list[tuple[str, str, int]]] = {
            "nb_drones": nb_drones,
            "start_hub": start_hub,
            "end_hub": end_hub,
            "hubs": hubs,
            "connections": connections_list
            }

        # Validate directories has allowed parameters
        self.validate_conf(res)

        return res

    def validate_conf(
        self,
        res: dict[str, str | list[str] | list[tuple[str, str, int]]]
    ) -> bool:
        # Check number of drones is valid
        if str(res.get("nb_drones")).strip() == "":
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'nb_drones'")

        if not str(res["nb_drones"]).isnumeric():
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'nb_drones'")

        # Check start hub / end_hub / hubs has valid format
        if res.get("start_hub") == "":
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'start_hub'")

        if res.get("end_hub") == "":
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'end_hub'")

        if res.get("hubs") == "":
            raise InvalidConfiguration(
                "[ERROR] Missing configuration parameter: 'hubs'")

        return True
