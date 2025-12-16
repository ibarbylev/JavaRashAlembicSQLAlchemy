import asyncio
from sqlalchemy import text, inspect

from database import engine


async def print_db_tables():

    async with engine.connect() as conn:

        async with engine.connect() as conn:
            # Получаем список таблиц через run_sync
            def get_tables(sync_conn):
                inspector = inspect(sync_conn)
                return inspector.get_table_names()

            tables = await conn.run_sync(get_tables)
            print(f"Найдено таблиц: {tables}")

            for table in tables:
                print(f"\nСодержимое таблицы '{table}':")
                result = await conn.execute(text(f'SELECT * FROM "{table}"'))
                rows = result.all()  # <-- просто .all(), без await

                if rows:
                    for row in rows:
                        print(dict(row._mapping))
                else:
                    print("Таблица пуста.")

    await engine.dispose()



if __name__ == "__main__":
    asyncio.run(print_db_tables())
