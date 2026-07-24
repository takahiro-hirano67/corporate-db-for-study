"""法人テーブルを作成するモジュール"""

import sqlite3

from config import DB_PATH

# DBに接続
connection = sqlite3.connect(database=DB_PATH)
cursor = connection.cursor()

# SQL文の定義
create_table_sql = """
-- 1. テーブル作成
CREATE TABLE 
    IF NOT EXISTS corporate_registry (
        corporate_number TEXT PRIMARY KEY, -- 法人番号
        corporate_name TEXT NOT NULL       -- 法人名
    );

-- 2. 法人名にインデックスを付与(完全一致・前方一致検索などの高速化)
CREATE INDEX IF NOT EXISTS index_corporate_name ON corporate_registry (corporate_name);
"""

# テーブル作成処理実行 (複数の命令を同時に実行)
cursor.executescript(create_table_sql)
# コミットして保存を確定する
connection.commit()

# 参考: テーブル名確認
response = cursor.execute("SELECT name FROM sqlite_master")
data = response.fetchone()[0]
print("テーブル名:", data)
