from unittest import TestCase
from main import put_ya_folder, get_folder_path


class TestYandex(TestCase):
    def test_put_ya_folder(self):
        expected = '201'
        names_folders = ['1-dir', '2-dir', '3-dir', '4-dir']
        for name in names_folders:
            result = put_ya_folder(name)
            self.assert_(result, expected)

    def test_get_folder_path(self):
        path = '2-dir'
        expected = f'disk:/{path}'
        result = get_folder_path(path)
        self.assert_(result, expected)

