import json
import unittest

from pagrindinis import _get_data_form_read_me  # pyright: ignore[reportPrivateUsage]


class TestPagrindinis(unittest.TestCase):
    def test_get_data_form_read_me(self):
        """Validate that README parsing returns expected dictionary"""
        expected_result = {
            "--gui": "Paleidžia grafinę sąsają",
            "-C, --check": "Tikrina duomenis su Google Sheets",
            "-G, --generate": "Generuoja naujus barkodus",
            "-I, --isbnPdf": "Konvertuoja ISBN CSV į PDF",
            "-S, --webScraper": "Nuskaito duomenis iš iBiblioteka",
            "-h, --help": "Parodo pagalbos informaciją",
            "-i, --input": "Įvedimo failas",
            "-o, --output": "Išvedimo failas",
            "-v, --version": "Parodo programos versiją",
        }

        result = _get_data_form_read_me()
        print(json.dumps(result, sort_keys=True, indent=4, ensure_ascii=False))

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
