import asyncio
import json
from prisma import Prisma

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

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

        data = Object()
        data.users = users

        await prisma.disconnect()
        return {
            "is_success": True,
            "data": json.loads(data.toJSON()),
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

        await prisma.disconnect()
        return {
            "is_success": True,
            "data": user
        }
    except Exception as e:
        print(e)
        return {
            "is_success": False,
            "message": str(e)
        }
