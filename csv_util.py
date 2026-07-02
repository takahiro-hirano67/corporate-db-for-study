"""CSVから値を抽出するためのヘルパーモジュール"""


def get_csv_value(index: int, row: list[str]) -> str | None:
    """CSVのカラムインデックスから文字列を抽出し、トリミングします。

    指定されたインデックスの値を取得し、前後の空白を削除します。
    トリミング後の値が空文字("")の場合は、Noneを返します。

    Args:
        index (int): 抽出する要素の列インデックス。
        row (list[str]): CSVの1行分のデータが含まれる文字列のリスト。

    Returns:
        str | None: トリミングされた文字列。空文字の場合は None。
    """
    value = row[index].strip()
    return value or None


# 動作確認
if __name__ == "__main__":
    import csv
    from config import CSV_PATH
    
    LIMIT_ROWS = 10  # 読み込む最大行数
    
    print("=== 法人CSVを開いて内容を確認します ===")
    print(f"対象ファイルパス: {CSV_PATH}\n")
    
    # CSVファイルを直接開いて読み込む
    with open(CSV_PATH, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        
        for count, row in enumerate(iterable=reader, start=1):
            if count > LIMIT_ROWS:
                break
            # 該当行の特定のカラムインデックスから値を取得
            corporate_number = get_csv_value(index=1, row=row)
            corporate_name = get_csv_value(index=6, row=row)
            print(f"------ {count}行目 ------")
            print(f"{row}\n")
            print(f"法人番号: {corporate_number}")
            print(f"法人名  : {corporate_name}\n")
