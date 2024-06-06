# Backup_python_scripts
When implementing lots of experiments and changes for model designs, it's easy to lose track of changes, especially after several days. Usually, not all variations can be easily captured in the config files or hyperparameterized. To ensure you can trace back modifications that correspond to specific results, a direct way is to back up all Python code used into the results folder. It helps manage model development and numerous experiments effectively.

# <p align=center>🔥` Thanks for ChatGPT!!!! `🔥</p>

# Step-by-Step Instructions
## 1. Create the Backup Module
First, create a dedicated Python file for the backup logic, for example, backup.py:

```python
# backup.py
import os
import shutil
import sys

def save_script_backup(script_path, backup_dir):
    script_path = os.path.abspath(script_path)
    script_rel_path = os.path.relpath(script_path, start=os.getcwd())
    backup_script_path = os.path.join(backup_dir, script_rel_path)

    os.makedirs(os.path.dirname(backup_script_path), exist_ok=True)
    shutil.copy2(script_path, backup_script_path)
    print(f"Backup of the script saved to: {backup_script_path}")

def backup_imported_modules(project_root, backup_dir="backups"):
    project_root = os.path.abspath(project_root)

    for module_name, module in sys.modules.items():
        try:
            module_file = getattr(module, '__file__', None)
            if module_file and module_file.endswith('.py'):
                module_file = os.path.abspath(module_file)
                # Only backup files within the project root
                if module_file.startswith(project_root):
                    module_rel_path = os.path.relpath(module_file, start=project_root)
                    backup_module_path = os.path.join(backup_dir, module_rel_path)

                    os.makedirs(os.path.dirname(backup_module_path), exist_ok=True)
                    shutil.copy2(module_file, backup_module_path)
                    print(f"Backup of the module {module_name} saved to: {backup_module_path}")
        except Exception as e:
            print(f"Failed to backup module {module_name}: {e}")

```

## 2. Use the Backup Module in Your Main Script
In your main script (e.g., main.py), import the backup.py module and call the functions to backup all imported modules. You can specify a custom backup directory.

```python
# main.py
import backup
import os

# Custom backup directory path
custom_backup_dir = "custom_backups"

# Save backup of the current script
backup.save_script_backup(__file__, custom_backup_dir)

# Your original script content
print("Running main script...")

# Import other modules in your project
import package1.script1
import package2.script2

# Backup all imported modules within the project directory
project_root = os.path.dirname(os.path.abspath(__file__))
backup.backup_imported_modules(project_root, custom_backup_dir)

# Add your code here

```


## 3. Example Modules with Imports
Ensure other modules within your project also import the backup logic if necessary:

```python
# package1/script1.py
import package3.script3  # Additional imports

# Your original script content
print("Running script1...")
# Add your code here
```

```python
# package1/script1.py
import package3.script3  # Additional imports

# package2/script2.py
import package4.script4  # Additional imports

# Your original script content
print("Running script2...")
# Add your code here
```
## 4. Example Modules
Here's an example for package3 and package4:

```python
# package3/script3.py

# Your original script content
print("Running script3...")
# Add your code here
```

```python
# package4/script4.py

# Your original script content
print("Running script4...")
# Add your code here
```

## 5. Project Directory Structure
Your project directory might look like this:
```
my_project/
├── custom_backups/
├── backup.py
├── main.py
├── package1/
│   └── script1.py
├── package2/
│   └── script2.py
├── package3/
│   └── script3.py
└── package4/
    └── script4.py
```

## 6. Running the Main Script
When you run main.py, it will backup itself and all other imported modules within the project directory to the specified backup directory, preserving the original directory structure.
```python
python main.py
```

## Output Example:
```
Backup of the script saved to: /path/to/my_project/custom_backups/main.py
Running main script...
Backup of the module package1.script1 saved to: /path/to/my_project/custom_backups/package1/script1.py
Running script1...
Backup of the module package3.script3 saved to: /path/to/my_project/custom_backups/package3/script3.py
Backup of the module package2.script2 saved to: /path/to/my_project/custom_backups/package2/script2.py
Running script2...
Backup of the module package4.script4 saved to: /path/to/my_project/custom_backups/package4/script4.py
```
