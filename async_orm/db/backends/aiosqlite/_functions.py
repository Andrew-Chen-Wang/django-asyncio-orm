import asyncio
import functools
import random

from async_orm.db.backends.sqlite3._functions import (
    StdDevPop,
    StdDevSamp,
    VarPop,
    VarSamp,
    create_conn_functions,
)


async def register(connection):
    create_deterministic_function = functools.partial(
        connection.create_function,
        deterministic=True,
    )
    await asyncio.gather(*create_conn_functions(create_deterministic_function))

    async def create_aggregate(*args):
        await connection._execute(connection._conn.create_aggregate, *args)

    # Don't use the built-in RANDOM() function because it returns a value
    # in the range [-1 * 2^63, 2^63 - 1] instead of [0, 1).
    await connection.create_function("RAND", 0, random.random)
    await create_aggregate("STDDEV_POP", 1, StdDevPop)
    await create_aggregate("STDDEV_SAMP", 1, StdDevSamp)
    await create_aggregate("VAR_POP", 1, VarPop)
    await create_aggregate("VAR_SAMP", 1, VarSamp)
