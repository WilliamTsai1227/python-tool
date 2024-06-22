import subprocess
import os
import site

"""specific_package_size_and_path()可以找到特定python package路徑及檔案大小的程式"""
"""原始指令"""
"""pip show yfinance"""
"""
會出現

Name: yfinance
Version: 0.1.59
Summary: Yahoo! Finance market data downloader
Home-page: https://github.com/ranaroussi/yfinance
Author: Ran Aroussi
Author-email: ranaroussi@gmail.com
License: Apache
Location: /path/to/your/python/environment/lib/python3.8/site-packages
Requires: requests, pandas, numpy
Required-by: 


"""


"""
以下指令即可顯示檔案大小
du -sh /path/to/your/python/environment/lib/python3.8/site-packages/yfinance
"""


def specific_package_size_and_path(package_name):
    # Get the site-packages directory
    site_packages_dir = site.getsitepackages()[0]

    # Construct the package path
    package_path = os.path.join(site_packages_dir, package_name)

    # Use subprocess to run the du command
    result = subprocess.run(['du', '-sh', package_path], stdout=subprocess.PIPE)

    # Print the result
    print(result.stdout.decode('utf-8'))


"""以下為找到所有python package 並包含檔案大小"""
"""類似於pip list"""

def get_installed_packages():
    result = subprocess.run(['pip', 'list', '--format=freeze'], stdout=subprocess.PIPE)
    packages = result.stdout.decode('utf-8').split('\n')
    return [pkg.split('==')[0] for pkg in packages if pkg]

def get_package_size(package_name):
    # Get the site-packages directory
    site_packages_dirs = site.getsitepackages()
    package_path = None

    # Check in each site-packages directory for the package
    for dir in site_packages_dirs:
        possible_path = os.path.join(dir, package_name)
        if os.path.exists(possible_path):
            package_path = possible_path
            break

    if package_path:
        # Use subprocess to run the du command
        result = subprocess.run(['du', '-sh', package_path], stdout=subprocess.PIPE)
        return result.stdout.decode('utf-8').split('\t')[0]
    else:
        return 'Size not found'

def main():
    packages = get_installed_packages()
    print(f"{'Package':<30} {'Size'}")
    print("-" * 40)
    for package in packages:
        size = get_package_size(package)
        print(f"{package:<30} {size}")

if __name__ == "__main__":
    main()
    specific_package_size_and_path('yfinance')    # Get the size of yfinance package
