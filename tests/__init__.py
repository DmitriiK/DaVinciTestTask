import os.path
import sys
# had to add parent directory explicitly to sys.path
directory = os.path.dirname(os.path.abspath("__file__"))
sys.path.append(directory)  # os.path.dirname(os.path.dirname(directory))
