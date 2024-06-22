# List Installed Python Packages with Sizes

This Python script lists all installed Python packages and their sizes. It uses `pip` to retrieve the list of installed packages and the `du` command to calculate the size of each package.

## Prerequisites

- Python 3.x
- `pip` (Python package installer)
- `du` command (available on Unix-like systems)

## Installation

1. **Clone the repository or download the script file**:
    ```sh
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```
    or simply download `find_python_package.py` to your desired directory.

2. **Ensure you have the necessary permissions to run the script**:
    ```sh
    chmod +x find_python_package.py
    ```

## Usage

1. **Navigate to the directory containing the script**:
    ```sh
    cd /path/to/directory
    ```

2. **Run the script**:
    ```sh
    python find_python_package.py
    ```

3. **Example Output**:
    ```
    Package                        Size
    ----------------------------------------
    pip                            1.3M
    setuptools                     938K
    wheel                          48K
    numpy                          45M
    pandas                         60M
    ```
    ```
    636K	/opt/anaconda3/lib/python3.11/site-packages/yfinance
    ```

## How It Works

1. **`get_installed_packages` function**:
   - Uses `pip list --format=freeze` to get a list of installed packages.
   - Returns a list of package names.

2. **`get_package_size` function**:
   - Determines the installation path of each package.
   - Uses `du -sh` to calculate the size of the package directory.

3. **`main` function**:
   - Lists all packages and their sizes in a formatted table.

## Notes

- This script is designed to run on Unix-like systems (Linux, macOS) where the `du` command is available.
- On Windows, you might need to use alternative methods to calculate directory sizes or run this script in a Unix-like environment such as WSL (Windows Subsystem for Linux).

## Troubleshooting

- If you encounter a "Size not found" message, ensure that the package is correctly installed and available in the site-packages directory.
- Ensure that you have the necessary permissions to execute the `du` command and access the Python installation directories.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [pip](https://pip.pypa.io/en/stable/)
- [Python](https://www.python.org/)
- [pypa](https://github.com/pypa)
