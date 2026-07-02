"""国税庁の法人番号データ(CSV形式)をSQLite3にインポートするモジュール"""

import csv
import sqlite3

# 設定情報
from config import CSV_PATH, DB_PATH

# CSVから値を取り出すための補助関数
from csv_util import get_csv_value


def import_corporate_data_from_csv() -> None:
    """法人番号データのCSVファイルを読み込み、全件洗い替えで保存するメイン処理"""

    print("=== 法人データのインポートを開始します ===")
    print(f"対象ファイル: {CSV_PATH}")

    # DBに接続
    with sqlite3.connect(database=DB_PATH) as connection:
        cursor = connection.cursor()

        # 1. 既存のデータをクリア(全件洗い替えのため)
        print("\n既存の法人データをクリアしています (DELETE FROM)...")
        cursor.execute("DELETE FROM corporate_registry;")

        # 2. CSVファイルを開いて読み込む
        print("CSVから法人データを投入しています (INSERT INTO)...")
        print("(処理には数十秒〜数分かかります)")
        with open(file=CSV_PATH, mode="r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)

            # 3. INSERT用のSQL文を準備 (名前付きプレースホルダー `:変数名` を使用)
            insert_query = """
                INSERT INTO corporate_registry (
                    corporate_number,
                    corporate_name
                ) VALUES (
                    :corporate_number,
                    :corporate_name
                )
            """

            # 4. CSVの行を1件ずつ取り出して処理するループ
            for row in reader:
                # 行から挿入する値を取得
                corporate_number = get_csv_value(index=1, row=row)
                corporate_name = get_csv_value(index=6, row=row)

                # どちらかが None なら、この行の処理はスキップして次の行へ
                if corporate_number is None or corporate_name is None:
                    continue

                # INSERT文に渡すためのデータセット(辞書)を作成
                insert_values_dict = {
                    "corporate_number": corporate_number,
                    "corporate_name": corporate_name,
                }

                # 1件ずつDBにINSERTを実行
                cursor.execute(insert_query, insert_values_dict)

        # 5. ループがすべて終わった最後に、1回だけコミットして保存を確定する
        connection.commit()

    print("\n=== 処理が完了しました ===")


# 実行
if __name__ == "__main__":
    import_corporate_data_from_csv()
