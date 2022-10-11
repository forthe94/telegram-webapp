import json


async def test_proccess_message(world, add_user):
    message = json.dumps({
        'type': 'coordinates_change',
        'new_x': 5,
        'new_y': 0
    })
    user = add_user
    res = await world.proccess_message(message, user=user)
    assert res is True
