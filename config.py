"""データベース接続情報やファイルパスを管理するモジュール"""

from pathlib import Path

# 実行中のスクリプトのパスを取得
SCRIPT_PATH = Path(__file__).resolve()
# スクリプトが配置されているディレクトリのパスを取得
BASE_DIR = SCRIPT_PATH.parent

# 法人データCSVのファイル名・配置場所 (実際のファイル名に合わせて書き換えてください)
CSV_NAME = "00_zenkoku_all_20260630.csv"
CSV_PATH = BASE_DIR / "data" / CSV_NAME

# データベースのファイル名・配置場所
DB_NAME = "corporate.db"
DB_PATH = BASE_DIR / DB_NAME
