# 
from datetime import datetime
from typing import Iterator

class Collection:
    def __init__(self, collection_title: str, collection_content: str) -> None:
        self.title = collection_title
        self.date = datetime.now()
        self.content = collection_content
        self.status = False

    def getCollectionName(self) -> str:
        return self.title

    def getCollectionDate(self) -> datetime:
        return self.date

    def getCollectionContent(self) -> str:
        return self.content

    def getCollectionStatus(self) -> bool:
        return self.status

    def setCollectionStatusTrue(self) -> bool:
        return not self.status

    # def __iter__(self) -> Iterator:
    #     return iter({
    #         'title': self.title,
    #         'date': self.date,
    #         'status': self.status})

    def __repr__(self) -> str:
        return f"todo('title':'{self.title.capitalize()}','date':{self.date},'status':{self.status})"
