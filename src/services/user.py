import json
from prisma import Prisma

from src.models.object import Object

async def get_all_users():
    """_summary_

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        prisma = Prisma()
        await prisma.connect()

        # write your queries here
        users = await prisma.user.find_many()

        data_object = Object()
        data_object.users = users

        await prisma.disconnect()
        return {
            "is_success": True,
            "data": json.loads(data_object.toJSON()),
        }
    except Exception as e:
        print(e)
        return {
            "is_success": False,
            "message": str(e)
        }


async def save_new_user(data):
    """_summary_

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        prisma = Prisma()
        await prisma.connect()

        # write your queries here
        user = await prisma.user.create(
            data=data,
        )

        data_object = Object()
        data_object.user = user

        await prisma.disconnect()
        return {
            "is_success": True,
            "data": json.loads(data_object.toJSON())
        }
    except Exception as e:
        print(e)
        return {
            "is_success": False,
            "message": str(e)
        }
