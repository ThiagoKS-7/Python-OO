class Programa:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_like(self, value):
        self._likes += value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value.title()

    def __str__(self):
        return f'{self._name} - {self.year} - {self.likes} likes'


class Filme(Programa):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'* {self._name} -- {self.year} -- {self.duration} minutos  -- {self.likes} likes'


class Serie(Programa):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'* {self._name} -- {self.year} -- {self.seasons} temporadas -- {self.likes} likes'


class Playlist:
    def __init__(self, name,  list):
        self.name = name
        self._list = list

    @property
    def list(self):
        return self._list

    def __len__(self):
        return len(self._list)

    def __getitem__(self, item):
        return self._list[item]

    def create(self):
        if type(self._list) != list:
            self._list = [self._list]
        for program in self._list:
            print(program)

    def size(self):
        if type(self._list) != list:
            self._list = [self._list]
        print(f'A playlist "{self.name}" tem {len(self)} programas, que são:')
        print()

    def check(self):
        self.size()
        self.create()

    def is_on_list(self, program, value):
        is_it_on_list = 'Sim' if program in self else 'Não'
        print(f'Pergunta {value}: {program.name} está na lista "{self.name}"? {is_it_on_list}')


if __name__ == '__main__':
    # *****************
    #    INSTÂNCIAS
    # ****************
    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    rick_morty = Serie('rick and morty', 2013, 5)
    atlanta = Serie('atlanta', 2018, 2)

    # *****************
    #      LIKES
    # ****************
    vingadores.give_like(1)
    rick_morty.give_like(999)
    atlanta.give_like(2)
    movies_and_series = [rick_morty, atlanta, vingadores]
    serie = atlanta

    # *****************
    #     PLAYLISTS
    # ****************
    playlist = Playlist('Hmmm', movies_and_series)
    playlist2 = Playlist('Dois', serie)

    print('******************************************************************')
    playlist.check()
    print()
    print('******************************************************************')
    playlist2.check()

    # *****************
    #     PERGUNTAS
    # ****************
    print()
    print('******************************************************************')
    question_number = 1
    playlist.is_on_list(vingadores, question_number)
    question_number += 1
    playlist2.is_on_list(rick_morty, question_number)
    print()
    print('******************************************************************')
