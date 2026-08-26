from . import all_programs
from .Programs.Manager import Program
from .Changelog import find_version_info
__version__ = "0.0.3.0.00a2"


def main():
    try:
        searchfor = __version__.split(".", maxsplit=3)
        sf3 = searchfor[3]
        insert = [sf3[0]+sf3[1], sf3.removeprefix(sf3[0]+sf3[1])]
        searchfor.remove(sf3)
        for item in insert:
            searchfor.append(item)
        print(find_version_info(*searchfor))
    except NotImplementedError as e:
        print(e)
    for pr_id in all_programs:
        try:
            Program(pr_id).run()
        except ImportError as e:
            print(e)
        except Exception as e:
            print(f"Failed to run program {pr_id}: {e}")


if __name__ == '__main__':
    main()
