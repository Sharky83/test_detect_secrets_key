
# Plain-text AWS secret for detect-secrets scanning
AWS_SECRET_ACCESS_KEY=AKIAIOSFODNN7EXAMPLEKEY1234567890

import os
import tempfile
from subprocess import run, PIPE

# Realistic AWS secret for detect-secrets scanning
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLEKEY1234567890"


if __name__ == "__main__":
    print("detect-secrets test passed.")
