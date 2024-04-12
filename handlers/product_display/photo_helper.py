from sql.sql_engine import SQLEngine


class PhotoPaginatorHelper:

    def __init__(self,
                 product_id: int = None,
                 photo_index: int = 0):

        self.__sql_engine: SQLEngine = SQLEngine()  # Композиция

        self.product_id = product_id
        self.photo_index = photo_index

        self.photos: list | None = None
        self.len_photos: int | None = None

    async def get_list_of_photos(self):
        """
        Получить список file_id фото по product_id
        :return: list[str]
        """
        self.photos = \
            await self.__sql_engine.get_photos_from_table(product_id=self.product_id)

        self.len_photos = len(self.photos)


class PhotoAddingHelper(PhotoPaginatorHelper):
    pass


class PhotoDeletingHelper(PhotoPaginatorHelper):
    pass

