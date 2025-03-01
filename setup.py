import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile


def main():
	chdir()
	if os.name == "nt":
		yarn = os.path.abspath(
			os.path.join(
				tempfile.gettempdir(), "..", "..", "Roaming", "npm", "yarn.cmd"
			)
		)
		npm = os.path.abspath(
			os.path.join("C:\\", "Program Files", "nodejs", "npm.cmd")
		)
	else:
		yarn = os.path.abspath(
			os.path.join(tempfile.gettempdir(), "..", "..", "Roaming", "npm", "yarn")
		)
		npm = os.path.abspath(
			os.path.join("C:\\", "Program Files", "nodejs", "npm")
		)

	parser = argparse.ArgumentParser(
		description="""
    This tool is designed to setup all of the dependencies for the RedKraken git
    repo. This script has the capabilities to install all of the required node
    modules for both the root directory and the frontend directory, setups all
    git submodules, and installs all pip packages from the pipfile.
    
    If not arguments are given, `setup.py` will set up ALL dependencies.
    
    # -------------------------------- warning ------------------------------- #
    
    When setting up node modules, the following error may occur:
    
    PermissionError: [WinError 32] The process cannot access the file because it
    is being used by another process
    
    To avoid this error, close all instances of VSCode and re-run this command
    from the terminal.
    """,
		formatter_class=argparse.RawTextHelpFormatter,
	)
	parser.add_argument(
		"-s",
		"--submodules",
		help="Will setup the git submodules",
		action="store_true",
	)
	parser.add_argument(
		"-p",
		"--pipenv",
		help="Will setup the pipenv environment",
		action="store_true",
	)
	parser.add_argument(
		"-n",
		"--node",
		help="""
    Will setup the node packages from the ./root and ./root/frontend directories
    """,
		action="store_true",
	)
	parser.add_argument(
		"--npm_path",
		help=f"The path to npm executable.\ndefault: {npm}",
		type=str,
		default=npm,
	)
	parser.add_argument(
		"--yarn_path",
		help=f"The path to yarn executable.\ndefault: {yarn}",
		type=str,
		default=yarn,
	)
	args = parser.parse_args()

	all_false = True

	if args.submodules:
		all_false = False
		setup_git_modules()

	if args.node:
		all_false = False
		setup_node_modules(args)

	if args.pipenv:
		all_false = False
		setup_pipenv()

	if all_false:
		setup_git_modules()
		setup_node_modules(args)
		setup_pipenv()


# ============================================================================ #
#                                     SETUP                                    #
# ============================================================================ #


def setup_git_modules():
	cwd = chdir()

	if not os.path.exists(os.path.join(cwd, ".gitmodules")):
		print(f".gitmodules could not be found at {cwd}")
		return

	modules = []
	with open(".gitmodules", "r") as gitmodules:
		modules = re.findall(r"path\s*=\s*(.*)\nurl\s*=\s*(.*)", gitmodules.read())
	for module in modules:
		module_path = os.path.join(*module[0].split("/"))

	print("Setting up submodules...")
	# Reset the submodules
	run(
		["git", "submodule", "foreach", "--recursive", "git reset --hard"],
		check=True,
		capture_output=True,
		text=True,
	)
	print("Reset successful")

	# Clean the submodules
	run(
		["git", "submodule", "foreach", "--recursive", "git", "clean", "-fd"],
		check=True,
		capture_output=True,
		text=True,
	)
	print("Clean successful")

	# Update the submodules
	run(
		["git", "submodule", "update", "--recursive"],
		check=True,
		capture_output=True,
		text=True,
	)
	print("Update successful")

	for module in modules:
		module_path = os.path.join(*module[0].split("/"))
		if not os.path.exists(module_path):
			print(f"{module_path} could not be found. Now adding...")
			try:
				subprocess.run(["git", "submodule", "add", module[1], module_path])
				print(f"Added {module_path} successfully!")
			except subprocess.CalledProcessError:
				print(f"Failed to add {module_path}")

	print("Done!")


def setup_pipenv():
	cwd = chdir()

	if not os.path.exists(os.path.join(cwd, "Pipfile")):
		print(f"Pipfile could not be found at {cwd}")
		return

	print("Setting up pipenv...")

	os.environ["PIPENV_VENV_IN_PROJECT"] = "1"

	venv_path = os.path.join(cwd, ".venv")
	if os.path.exists(venv_path):
		shutil.rmtree(venv_path)

	run(["pipenv", "install"], check=True)
	print("Done!")


def setup_node_modules(args):
	cwd = chdir()

	if not os.path.join(cwd, "package.json"):
		print(f"Package.json could not be found at {cwd}")
		return

	node_modules_path = os.path.join(cwd, "node_modules")
	if os.path.exists(node_modules_path):
		print(f"Removing {node_modules_path}...")
		shutil.rmtree(node_modules_path)

	print("Detecting package manager...")
	if os.path.exists("package-lock.json"):
		package_manager = args.npm_path
	elif os.path.exists("yarn.lock"):
		package_manager = args.yarn_path
	else:
		print("No lock file found, using npm...")
		package_manager = args.npm_path

	if not os.path.exists(package_manager):
		print(
			f"Cannot find {os.path.basename(package_manager)} at {package_manager}"
		)
		sys.exit(1)

	print(f"Installing node_modules with {os.path.basename(package_manager)}...")
	run([package_manager, "install"], check=True)
	print("Done!")


# ============================================================================ #
#                                     UTILS                                    #
# ============================================================================ #


def chdir(path: str = ""):
	if path == "":
		path = os.path.dirname(os.path.abspath(__file__))

	if os.path.exists(path):
		os.chdir(path)
	else:
		print(f"Path does not exist: {path}")
		sys.exit(1)

	return path


def run(command: list, **kwargs):
	try:
		subprocess.run(command, **kwargs)
	except subprocess.CalledProcessError as e:
		print(f"Command failed: {e}")
		print(f"Error output: {e.stderr}")
		sys.exit(1)


if __name__ == "__main__":
	main()
