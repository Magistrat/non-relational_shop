from fastapi import HTTPException
from fastapi import status


class ExceptionFactory:
    """
    Сборка исключений.
    """

    @classmethod
    async def get_http_exception(cls, status_code: int, text: str) -> HTTPException:
        """
        Базовый метод поднятия HTTPException (fastapi)

        :param status_code: Статус код ответа
        :param text: Описание тела ответа
        :return: Объект класса исключения (HTTPException)
        """
        return HTTPException(status_code=status_code, detail=text)

    @classmethod
    async def get_service_unavailable(cls, text: str) -> HTTPException:
        """
        Возвращает объект класса-исключения, что какой-то из серверов не доступен

        :param text: Описание тела ответа
        :return: Объект класса-исключения (HTTPException)
        """
        return await cls.get_http_exception(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, text=text)

    @classmethod
    async def get_not_found(cls, text: str) -> HTTPException:
        """
        Возвращает объект класса-исключения, что не было найдено значение

        :param text: Описание тела ответа
        :return: Объект класса-исключения (HTTPException)
        """
        return await cls.get_http_exception(status_code=status.HTTP_404_NOT_FOUND, text=text)

    @classmethod
    def get_value_error(cls, text: str) -> ValueError:
        """
        Возвращает объект ValueError класса-исключения

        :param text: Описание тела ответа
        :return: Объект класса-исключения (ValueError)
        """
        return ValueError(text)
