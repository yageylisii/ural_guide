from sqlalchemy import select, update
import time
from bot.database.core import async_session
from bot.database.models import User


async def insert_data(user_id:int):
    async with async_session() as session:
        requests = await select_user(user_id)
        if not requests:
            work_data = User(
                user_id = int(user_id),
                time_register = time.time()
            )
            session.add(work_data)
            await session.commit()
            return True
    return False

async def select_user(user_id:int):
    try:
        async with async_session() as session:
            requests = select(User).where(User.user_id == int(user_id))
            result = await session.execute(requests)
            user = result.scalars().first()
        return user
    except:
        return False

async def update_user(user_id:int, column: str, value: int | str):
    async with async_session() as session:
        request = (
            update(User).
            where(User.user_id == user_id).
            values({column: value})
        )

        await session.execute(request)
        await session.commit()