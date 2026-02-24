import sys
import pandas as pd


def create_ids(id_count: str) -> None:
    """ Generate a list of IDs and save it as a csv."""
    ids = [i for i in range(int(id_count))]
    df = pd.DataFrame(ids)
    df.to_csv("./id.csv", index=False)


if __name__ == "__main__":
    create_ids(sys.argv[1])