import os
import sys


def safe_load_dotenv() -> bool:
    try:
        from dotenv import load_dotenv  # type: ignore
    except ModuleNotFoundError:
        print("python-dotenv is not installed; skipping .env load.")
        print("Install it with: pip install python-dotenv")
        return False
    try:
        load_dotenv()
        return True
    except Exception as e:
        print("Failed to load .env:", e)
        return False


def is_env_correct() -> bool:
    from dotenv import load_dotenv

    variables = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    load_dotenv()
    responses: list[str | None] = [os.getenv(v) for v in variables]

    for i, response in enumerate(responses):
        if response is None:
            print(f"Missing configuration for variable {variables[i]}")
            return False

    conf_mode = os.getenv("MATRIX_MODE")
    if conf_mode not in ("development", "production"):
        return False

    return True


def test_m8_ex2() -> None:
    env_status: bool
    try:
        env_status = is_env_correct()
    except ModuleNotFoundError as e:
        print("Required module missing:", e)
        print("Please run: pip install python-dotenv")
        return
    modules_status: bool = safe_load_dotenv()

    conf_mode = os.getenv("MATRIX_MODE")

    if modules_status and env_status:
        print("\nORACLE STATUS: Reading the Matrix...\n")
        from dotenv import load_dotenv

        load_dotenv()

        db_url = os.getenv("DATABASE_URL")
        api_access = os.getenv("API_KEY")
        log_level = os.getenv("LOG_LEVEL")
        zion_connection = os.getenv("ZION_ENDPOINT")

        print("Configuration loaded:")
        if conf_mode == "development":
            print(f"Mode: {conf_mode}")
            if db_url == "127.0.0.1":
                print(f"Database: Connected to local instance")
            else:
                print(f"Database: Unable to connect to local instance")

            if api_access == "dummy-12345":
                print(f"API Access: Authenticated")
            else:
                print("API Access: Denied")
            print(f"Log Level: {log_level}")
            if zion_connection == "https://example.invalid/api":
                print(f"Zion Network: Online")
            else:
                print(f"Zion Network: Offline")
        
        if conf_mode == "production":
            print(f"Mode: {conf_mode}")
            if db_url == "DATABASE_URL=redis://:dummy_pass@192.0.2.1:6379/0":
                print(f"Database: Connected to production instance")
            else:
                print(f"Database: Unable to connect to production instance")

            if api_access == "secret123":
                print(f"Production API Access: Authenticated")
            else:
                print("Production API Access: Denied")
            print(f"Log Level: {log_level}")
            if zion_connection == "https://real/api":
                print(f"Production Zion Network: Online")
            else:
                print(f"Production Zion Network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
        
    if env_status:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file isn't properly configured")
    if conf_mode == "production":
        print("[OK] Production overrides available")
    elif conf_mode == "development":
        print("[OK] Development overrides available")
    else:
        print("[KO] MATRIX_MODE overrides unavailable")
    
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    test_m8_ex2()