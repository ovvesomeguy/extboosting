from vk_api.longpoll import VkLongPoll, VkEventType

def check(vk):
    answer = {}
    longpoll = VkLongPoll(vk)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.from_user:
                answer['id'] = event.user_id
                answer['message'] = event.text
                return answer
