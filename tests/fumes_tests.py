import unittest
from fumigate import Fumes


class FumesTestCase(unittest.TestCase):

    def setUp(self):
        self.fumes = Fumes()
        self.single_text = "hey amazon - my package never arrived " \
                           "https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first please fix asap! " \
                           "@amazonhelp "
        self.list_of_text = [
            "hey amazon - my package never arrived \
            One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They "
            "are right, as this is exactly what happened with me.<br /><br /> ",
            "I sure would like to see a resurrection of a up dated Seahunt series with the tech they have today it "
            "would bring back the kid excitement in me.I grew up on black and white TV and Seahunt with Gunsmoke were "
            "my hero's every week.You have my vote for a comeback of a new sea hunt.We need a change of pace in TV "
            "and this would work for a world of under water adventure.Oh by the way thank you for an outlet like this "
            "to view many viewpoints about TV and the many movies.So any ole way I believe I've got what I wanna "
            "say.Would be nice to read some more plus points about sea hunt.If my rhymes would be 10 lines would you "
            "let me submit,or leave me out to be in doubt and have me to quit,If this is so then I must go so lets do "
            "it. ",
            " 😆 👨 https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first please fix asap! @amazonhelp\
            hey amazon - my package never arrived ",
            "https://www.amazon.com/gp/css/or🧑‍🍼der-history?ref_=nav_orders_first please fix asap! @amazonhelp"
        ]

    def test_single_text(self):
        """Test single text"""

        result = self.fumes.purge(self.single_text)
        answer = "hey amazon package never arrived please fix asap"
        self.assertEqual(result, answer)

    def test_list_of_text(self):
        """Test list of text"""

        result = [self.fumes.purge(x) for x in self.list_of_text]
        answer = [
            'hey amazon package never arrived one reviewers mentioned watching oz episode youll hooked right exactly happened mebr br',
            'sure would like see resurrection dated seahunt series tech today would bring back kid excitement mei grew black white tv seahunt gunsmoke heros every weekyou vote comeback new sea huntwe need change pace tv would work world water adventureoh way thank outlet like view many viewpoints tv many moviesso ole way believe ive got wanna saywould nice read plus points sea huntif rhymes would lines would let submitor leave doubt quitif must go lets',
            'please fix asap hey amazon package never arrived', 'please fix asap']
        self.assertEqual(result, answer)

    def test_clean(self):
        """Test Clean method"""

        result = self.fumes.clean(self.single_text, methods=["url", "sym", "stopwords"])
        answer = "hey amazon package never arrived please fix asap amazonhelp"
        self.assertEqual(result, answer)

    def test_clean_extract(self):
        """Test Clean method with extract garbage"""

        result = self.fumes.clean(self.single_text, methods=["url"], extract=True)
        answer = ('hey amazon - my package never arrived please fix asap! @amazonhelp ',
                  [['https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first']])
        self.assertEqual(result, answer)

    def test_clean_exception(self):
        """Test Exception for clean method"""

        with self.assertRaises(Exception):
            self.fumes.clean(self.single_text, methods=["sym", "num", "gum"])

    def test_purge_exception(self):
        """Test Exception for purge method"""

        with self.assertRaises(Exception):
            self.fumes.purge()


if __name__ == '__main__':
    unittest.main()
