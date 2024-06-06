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

