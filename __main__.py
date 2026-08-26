from . import all_programs
from .Programs.Manager import Program
__version__ = "0.0.3.0.00a1"


def main():
    for pr_id in all_programs:
        try:
            Program(pr_id).run()
        except ImportError as e:
            print(e)
        except Exception as e:
            print(f"Failed to run program {pr_id}: {e}")


if __name__ == '__main__':
    main()
