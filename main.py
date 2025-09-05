import os
import tempfile
from subprocess import run, PIPE

def test_detect_secrets_on_sample_file():
    # Create a sample file with a fake secret
    with tempfile.TemporaryDirectory() as tempdir:
        secret_file = os.path.join(tempdir, "secrets.txt")
        with open(secret_file, "w") as f:
            f.write("AWS_SECRET_ACCESS_KEY=FAKESECRET1234567890\n")
        # Run detect-secrets CLI
        result = run([
            os.path.join(os.getcwd(), ".venv/bin/detect-secrets"),
            "scan", secret_file, "--all-files", "--json"
        ], stdout=PIPE, stderr=PIPE, text=True)
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        assert "AWS_SECRET_ACCESS_KEY" in result.stdout
        assert result.returncode == 0

if __name__ == "__main__":
    test_detect_secrets_on_sample_file()
    print("detect-secrets test passed.")
