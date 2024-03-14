import json
from prisma import Prisma

from src.models.object import Object

async def async_sign_in(data):
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
        users = await prisma.user.find_many(
            where={
                'AND': [
                    {'name': {'equals': data['name']}},
                    {'email': {'equals': data['email']}},
                ]
            }
        )

        data_object = Object()
        data_object.users = users

        await prisma.disconnect()

        if len(users) > 0:
            return {
                "is_success": True,
                "data": json.loads(data_object.toJSON()),
            }        
        return {
            "is_success": False,
            "message": "name or email is not valid",
        }
    except Exception as e:
        print(e)
        return {
            "is_success": False,
            "message": str(e)
        }
