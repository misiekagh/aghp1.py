#from d40mod import Company, Task
from dataclasses import dataclass
from typing import Union

@dataclass
class Task:
    contents: str
    points: int
    done = False

    def execute(self):
        self.done=True

@dataclass
class Worker:
    name: str
    age: int
    points = 0
    tasks = []

    def desc(self) -> str:
        return f'{self.name} {self.age}'
    def work(self):
        task=self.tasks.pop(0) # kolejka zamiast listy?
        print(f'Doing {task}')
    def add_task(self, task):
        self.tasks.append(task)
    @property
    def points_accu(self) -> int:
        return self.points
    @property
    def salary(self):
        raise NotImplementedError
    @property
    def task_count(self):
        return len(self.tasks)

@dataclass
class Salaried(Worker):
    weekly_salad: int

    @property
    def monthly_salad(self) -> int:
        return self.weekly_salad * 4
    def desc(self) -> str:
        return f'Saladied {self.name} {self.age}yo'

@dataclass
class Hourly(Worker):
    hours_per_week: int
    hourly_rate: int

    @property
    def monthly_salad(self) -> int:
        return self.hours_per_week * self.hourly_rate * 4
    def desc(self) -> str:
        return f'Hourly {self.name} {self.age}yo'

@dataclass
class Company:
    name: str
    workers = []
    tasks = []

    def add_worker(self, name: str, age: int, wtype: str) -> None:
        worker = Hourly(name,age, 10, 100) if wtype == 'H' else Salaried(name,age, 750)
        self.workers.append(worker)
    def add_task(self, task: str) -> None:
        self.tasks.append(task)
    def give_tasks(self, number: int):
        self.workers.sort(key=lambda: x,x.task_count)
        for _, w, t in zip(range(number), self.workers, self.tasks):
            w.add_task(t)

    @property
    def total_salary(self) -> int:
        return sum([w.monthly_salad for w in self.workers])
    @property
    def worker_count(self) -> int:
        return len(self.workers)
    def welcome(self) -> str:
        return f'Welcome all workers\nTo {self.name} company.'

if __name__=='__main__':
    from pprint import pprint
    from random import randint, choice
    
    TASKS=('Zrobić kawę', 'Pozamiatać', 'Wynieść śmieci', 'Popstrykać', 'Pokiwać się na krześle', 'Iść do domu')        
    NAMES=('John', 'Ian', 'Anna','Thomas', 'Martha', 'Kathy', 'Antonio', 'Eve', 'Peter', 'Michael')

    def get_worker():
        name, age = NAMES[randint(0, len(NAMES)-1)], randint(20,60)
        return name, age

    def get_task() -> Task:
        return Task(TASKS[randint(0,len(TASKS)-1)], randint(5,20))

    company=Company('Test')
    for _ in range(10): company.add_task(get_task())
    for _ in range(5): company.add_worker(*get_worker(), choice('SH'))
    
    pprint(company.workers)
    print(f'Monthly total {company.total_salary}')
    print(company.worker_count)
    print(company.welcome())

    for _ in range(10): company.give_tasks(10)
    