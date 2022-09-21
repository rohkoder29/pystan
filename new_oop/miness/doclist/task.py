# 
class Task:
    def __init__(self, task_title: str) -> None:
        self.title = task_title


    def __repr__(self) -> str:
        return f" - {self.title}"