import polars as pl

df = pl.read_csv("data/01_data.txt")


def get_solution(df=df):
    one_sorted = df.select("one").sort("one")
    two_sorted = df.select("two").sort("two")

    sorted_df = pl.concat([one_sorted, two_sorted], how="horizontal")

    sorted_df = sorted_df.with_columns(three=abs(pl.col("one") - pl.col("two")))

    answer = sorted_df.select("three").to_series().sum()
    return answer


def get_part_2(df=df):

    df_vc = df["two"].value_counts().sort("two")
    value_counts_dict = dict(zip(df_vc["two"], df_vc["count"]))

    one_list = df["one"].to_list()

    result = []
    for one in one_list:
        if one in value_counts_dict:
            result.append(value_counts_dict[one] * one)

    return sum(result)


def main():
    print("Part 1:", get_solution())
    print("Part 2:", get_part_2())


if __name__ == "__main__":
    main()
