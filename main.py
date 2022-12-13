# standard library
import os

# others libraries
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    print(os.getenv("ENV_VAR"))
