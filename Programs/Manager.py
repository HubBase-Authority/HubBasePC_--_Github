import importlib, sys
from pathlib import Path


def print_ImportError(error: BaseException, module_name: str, message: str | None=None):
    if message:
        raise Exception(f"[HubBase Engine] {message}")
    else:
        raise ImportError(f"[HubBase Engine] Failed to import {module_name}: {error}")


class Program:
    def __init__(self, id: int | str, source = None):
        self.id = str(id)
        self.project_root = Path(__file__).resolve().parent.parent if source is None else source
        if str(self.project_root) not in sys.path:
            sys.path.insert(0, str(self.project_root))
        self.program_dir = self.project_root / "Programs" / self.id
        self.path = self.program_dir / "main.py"
        if not self.path.exists():
            raise FileNotFoundError(f"[HubBase Engine] Programs.{self.id}.main not found")

    def load(self):
        module_name = f"Programs.{self.id}.main"
        md_module_name = f"Programs.{self.id}"
        metadata = None
        try:
            module = importlib.import_module(module_name)
            try:
                md_module = importlib.import_module(md_module_name)
                metadata = md_module.ProgramInfo
            except (AttributeError, ImportError):
                metadata = None
            return module.run, [], metadata
        except ImportError as e:
            return print_ImportError, [e, module_name], metadata
        except AttributeError as e:
            return print_ImportError, [e, module_name, f"[HubBase Engine] {module_name} doesn`t have a `run()` method. "], metadata

    def run(self):
        metadata = None
        try:
            to_run, args, metadata = self.load()
            print(f"[HubBase Engine] Launching program №{self.id} - {metadata["Name"]}")
            to_run(*args)
            return True, metadata
        except Exception as e:
            print(f"[HubBase Engine] Failed to run program №{self.id}: {e}")
            return False, metadata
