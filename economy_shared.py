from redis_store import redis_get_json, redis_set_json

STATE_KEY = "slimebot:state"

state = {}

def load_state():
    global state
    state = redis_get_json(STATE_KEY, {"users": {}, "items": {}, "world": {}, "arena_world": {}, "lab_world": {}, "voidmaze_world": {}, "afk": {}})
    return state


def save_state():
    redis_set_json(STATE_KEY, state)
