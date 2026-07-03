# corporate-db-for-study

初心者向けに、実践的な法人データを扱いながら Python × SQLite を用いてデータベースを作成する学習用リポジトリです。

国税庁が公開する「法人番号公表サイト」のCSVデータを SQLite3 データベースに取り込み、法人番号・法人名を検索できる状態にします。

## 解説記事へのリンク

Qiitaに解説記事を投稿しています。以下のリンクからアクセス可能です。

[【初心者向け】Python × SQLite で法人データベースを作ろう | Qiita](https://qiita.com/takahiro-hirano67/items/57c48517d2fbd29f45ac)

## 必要環境

- Python 3.10 以上（`str | None` 形式の型ヒントを使用しています）
- 標準ライブラリのみで動作します（`sqlite3`, `csv`, `pathlib`）。追加のパッケージインストールは不要です。

## 使い方

1. `data/` フォルダを作成し、法人データCSV（例: `00_zenkoku_all_20260630.csv`）を配置します。
2. `config.py` の `CSV_NAME` を、配置したCSVのファイル名に合わせて修正します。
3. テーブルを作成します。

```bash
python create_table.py
```

4. CSVデータをインポートします。

```bash
python insert_data.py
```

## ディレクトリ構成

```
.
├── config.py         # DB/CSVのパスなど設定情報
├── create_table.py   # corporate_registry テーブルを作成
├── csv_util.py        # CSVから値を抽出するヘルパー関数
├── insert_data.py     # CSVをDBへ一括インポート
├── data/               # 法人データCSVの配置場所（各自用意）
└── corporate.db        # 実行後に生成されるSQLiteデータベース（.gitignore対象）
```

## スキーマ

`corporate_registry` テーブル

| カラム名         | 型                 | 説明                       |
| ---------------- | ------------------ | -------------------------- |
| corporate_number | TEXT (PRIMARY KEY) | 法人番号                   |
| corporate_name   | TEXT (NOT NULL)    | 法人名（インデックスあり） |

## 補足

- `insert_data.py` は実行のたびに既存データを全削除してからCSVを再投入します（全件洗い替え）。
- CSVの列インデックス（法人番号: 1列目、法人名: 6列目）は国税庁CSVのフォーマットに依存しています。
