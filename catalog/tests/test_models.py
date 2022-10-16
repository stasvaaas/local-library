from django.test import TestCase
from catalog.models import Author, Genre, Book, BookInstance


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        # Getting an object to test
        author = Author.objects.get(id=1)
        # Getting the field metadata to get the necessary values
        field_label = author._meta.get_field('first_name').verbose_name
        # Compare the value with the expected result
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'Died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_last_name_coma_first_name(self):
        author = Author.objects.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        self.assertEquals(author.get_absolute_url(), '/catalog/author/1')


class GenreModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Drama')

    def test_name_label(self):
        name = Genre.objects.get(id=1)
        field_label = name._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        genre = Genre.objects.get(id=1)
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title=' The greatest book')

    def test_title_label(self):
        title = Book.objects.get(id=1)
        field_label = title._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        title = Book.objects.get(id=1)
        max_length = title._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_summary_max_length(self):
        summary = Book.objects.get(id=1)
        max_length = summary._meta.get_field('summary').max_length
        self.assertEquals(max_length, 1000)

    def test_isbn_length(self):
        isbn = Book.objects.get(id=1)
        length = isbn._meta.get_field('isbn').max_length
        self.assertEquals(length, 13)

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEquals(book.get_absolute_url(), '/catalog/book/1')

# class BookInstanceModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         BookInstance.objects.create(imprint='some more imprint to check')
#
#     def test_imprint_label(self):
#         imprint = BookInstance.objects.get(id=1)
#         length = imprint._meta.get_field('imprint').max_length
#         self.assertEquals(length, 200)
