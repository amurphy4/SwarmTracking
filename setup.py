import os, sys

# Python version
version = "{0}.{1}".format(sys.version_info[0], sys.version_info[1])

if sys.platform == "linux" or sys.platform == "linux2":
    # Linux - Recommended platform
    pkg_folder = "/usr/lib/python{0}/dist-packages".format(version)
    folder = "{0}/SwarmTracking".format(pkg_folder)

    if not os.path.exists(folder):
        # Create SwarmTracking directory in package folder
        os.system("sudo mkdir -p {0}".format(folder))

    # Get path of setup.py file
    current_path = os.path.realpath(__file__)

    # Get path of parent directory (SwarmTracking)
    parent = os.path.abspath(os.path.join(current_path, os.pardir))

    # Loop over parent directory
    for item in os.listdir(parent):
        # Ignore unwanted files
        if item != "setup.py" and item != ".git" and item != ".gitignore":
            if (os.path.isdir(item)):
                # Copy folder to new package folder
                os.system("sudo cp -r {0}/{1} {2}".format(parent, item, folder))
            else:
                # Copy file to new package folder
                os.system("sudo cp {0}/{1} {2}".format(parent, item, folder))

    print("Package has been installed at {0}".folder)
            
elif sys.platform == "darwin":
    # macOS
    pkg_folder = "/Library//Python/{0}/site-packages".format(version)
    folder = "{0}/SwarmTracking".format(pkg_folder)

    if not os.path.exists(folder):
        # Create SwarmTracking directory in package folder
        os.system("sudo mkdir -p {0}".format(folder))

    # Get path of setup.py file
    current_path = os.path.realpath(__file__)

    # Get path of parent directory (SwarmTracking)
    parent = os.path.abspath(os.path.join(current_path, os.pardir))

    # Loop over parent directory
    for item in os.listdir(parent):
        # Ignore unwanted files
        if item != "setup.py" and item != ".git" and item != ".gitignore":
            if (os.path.isdir(item)):
                # Copy folder to new package folder
                os.system("sudo cp -r {0}/{1} {2}".format(parent, item, folder))
            else:
                # Copy file to new package folder
                os.system("sudo cp {0}/{1} {2}".format(parent, item, folder))

    # Ensure the package folder is on the PYTHONPATH
    if pkg_folder not in sys.path:
        os.system('echo "export PYTHONPATH=$PYTHONPATH:{0}" >> ~/.bash_profile'.format(pkg_folder))
        os.system('source ~/.bash_profile')

    print("Package has been installed at {0}".folder)
    
elif sys.platform == "win32":
    # Windows
    print("This installation method is not supported on Windows")
    sys.exit(0)
else:
    print("Unable to determine platform")
    sys.exit(0)

