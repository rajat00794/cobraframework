from odmantic import Model


class FileStorage(Model):
    file: str
    file_name: str
    ext: str


class FileUpload:
    def __init__(self, dbmanager: object) -> None:
        self.dbmanager = dbmanager

    async def upload(self, data: object):
        data = FileStorage(**data)
        dart = await self.dbmanager.save(data)
        return str(data.id)
