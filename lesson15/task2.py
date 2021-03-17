
# Реализуйте 2 класса, первый - Босс, а второй - Рабочий.
# У Worker есть свойство boss, и его значение должно быть экземпляром Boss.
# Вы можете переназначить это значение, но вы должны проверить, является ли новое значение Boss.
# У каждого босса есть список своих рабочих. Вам следует реализовать метод, позволяющий добавлять рабочих к боссу.
# Вам не разрешено добавлять экземпляры класса Boss в список рабочих напрямую через доступ к атрибуту,
# вместо этого используйте геттеры и сеттеры!

# + добавил декоратор изменения компании для работника


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id_
        self._name = name
        self._company = company
        self._workers = []

    @property
    def company(self):
        return self._company

    def add_worker(self, worker):
        if worker not in self._workers:
            self._workers.append(worker)
        else:
            print(f'The {worker} works in our company!')

    def __str__(self):
        return f'({self._name} ,{self._company}, workers:{self._workers}, {self.id_})'

    def __repr__(self):
        return f'{self._name}'


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id_ = id_
        self.name = name
        self._company = company
        self._boss = boss

    def __str__(self):
        return f'Worker name: {self.name}, Company: {self._company}, id :{self.id_}, Boss: {self._boss}.'

    def __repr__(self):
        return f'{self.name}'

    @property
    def boss(self):
        return f'{self._boss}'

    @boss.setter  # переназначение босса
    def boss(self, new_boss: Boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss

    @property
    def company(self):
        return f'{self._company}'

    @company.setter  # переназначение компании
    def company(self, new_company: str):
        self._company = new_company


if __name__ == '__main__':
    george = Boss(1, 'George', 'ATB')
    steve = Boss(2, 'Steve', 'Google')
    edik = Worker(2, 'Edik', 'ATB', george)
    slava = Worker(1, 'Slava', 'ATB', george)
    viktor = Worker(1, 'Viktor', 'Google', steve)
    george.add_worker(edik)
    george.add_worker(slava)
    steve.add_worker(viktor)
    print(viktor)
    viktor.boss = george
    viktor.company = george.company
    print(viktor)
    print(edik)
    print(slava)
    print(steve)
    print(george)

