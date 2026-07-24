"""データ取得例"""

import sqlite3

import config


def execute_search(search_word: str):

    with sqlite3.connect(database=config.DB_PATH) as connection:
        cursor = connection.cursor()

        select_sql = """
        select
            corporate_number,
            corporate_name
        FROM
            corporate_registry
        WHERE
            corporate_name
        LIKE
            :search_word
        """

        search_params = {"search_word": f"%{search_word}%"}

        response = cursor.execute(select_sql, search_params)
        data = response.fetchall()
        for i, corporate in enumerate(iterable=data, start=1):
            print(f"| {i}件目 | {corporate[0]} | {corporate[1]} |")
        print("-" * 20)
        print(f"総数: {len(data)}件")


if __name__ == "__main__":
    search_word = input("検索したい企業名を入力してください: ")
    execute_search(search_word)
