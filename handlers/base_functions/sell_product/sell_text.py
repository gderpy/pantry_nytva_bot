from pydantic import BaseModel


class SellingText(BaseModel):

    name: str = "<b><i>Отправьте название товара</i></b>"

    price: str = "<b><i>Отправьте стоимость товара</i></b>"

    contact: str = ("<b><i>Оcтавьте какие-либо контакты для связи с вами.\n\n"
                    "Например: электронную почту, номер телефона, либо телеграм и тд</i></b>")

    end: str = ("<i>Данные о товаре внесены!</i>\n\n"
                "<b><i>Нажмите на кнопку ниже, чтобы отправить</i></b>")

    posted: str = ("<i>Данные отправлены на рассмотрение</i>!\n\n"
                   "<b><i>Срок рассмотрения 24 часа</i></b>")



