import sys
import os

if __name__ == "__main__":
    p = os.popen("git rev-list --tags --max-count=1")
    commit = p.read().strip()
    p.close()

    if commit:
        p = os.popen("git describe --tags " + commit)
        tag = p.read().strip()
        p.close()
        version = tag[1:] if tag.startswith("v") else tag
    else:
        version = "0.0.0"

    version_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "../QtScrcpy/appversion"))
    with open(version_file, "w") as f:
        f.write(version)
    sys.exit(0)
