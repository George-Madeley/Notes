import os
import sys


def chdir(path: str = ""):
  if path == "":
    path = os.path.dirname(os.path.abspath(__file__))

  if os.path.exists(path):
    os.chdir(path)
  else:
    print(f"Path does not exist: {path}")
    sys.exit(1)

  return path