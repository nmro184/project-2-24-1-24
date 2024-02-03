class Task:
    def __init__(self , task_tuple ):
        self.id = task_tuple[0]
        self.description =task_tuple[1]
        self.date = task_tuple[2]
        self.category = task_tuple[3]
        
    def to_dict(self):
        return {
            'description': self.description,
            'date': self.date,
            'category' : self.category
        }
