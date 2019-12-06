from configs.keys    import vk_key
from vk_api.longpoll import VkLongPoll, VkEventType

import vk_api

def group():
    vk = vk_api.VkApi(vk_key)
    return vk