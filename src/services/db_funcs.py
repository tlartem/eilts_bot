# функция отправки аудиофайла д\раздела listening
async def send_audio_listening() -> None: ...


# функция отправки списка вопросов д\раздела listening
async def send_q_list_listening() -> None: ...


# функция отправки текста задания д\раздела reading
async def send_text_task_reading() -> None:
    pass


# функция отправки списка вопросов д\раздела reading
async def send_q_list_reading() -> None:
    pass
