class Song(object):
    def __init__(self):
        self.verse = """{number_of_bottles} {text} of beer on the wall, {number_of_bottles} {text} of beer.
Take one down and pass it around, {next_verse_number_of_bottles} {text} of beer on the wall."""

        self.second_last_verse = """1 bottle of beer on the wall, 1 bottle of beer.
Take it down and pass it around, no more bottles of beer on the wall."""

        self.last_verse = """No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""

    def get_song(self) -> str:
        song: str = ""
        for x in range(100):
            song += self.get_verse(x+1) + "\n\n"
        return song

    @staticmethod
    def get_bottle_or_bottles(number_of_bottles):
        if number_of_bottles == 1:
            return 'bottle'
        return 'bottles'

    def get_verse(self, verse_number):
        number_of_bottles = 100 - verse_number
        next_verse_number_of_bottles = number_of_bottles - 1

        if next_verse_number_of_bottles == 0:
            return self.second_last_verse

        verse: str = self.verse
        if next_verse_number_of_bottles < 0:
            return self.last_verse

        return verse.format(number_of_bottles=number_of_bottles,
                            next_verse_number_of_bottles=next_verse_number_of_bottles,
                            text=self.get_bottle_or_bottles(number_of_bottles))
