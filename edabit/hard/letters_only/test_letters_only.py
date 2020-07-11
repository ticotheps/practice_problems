import unittest
from letters_only import letters_only

class Test(unittest.TestCase):
    def test_letters_only(self):
        self.assertEqual(letters_only('R!=:~0o0./c&}9k`60=y'), 'Rocky')
        self.assertEqual(letters_only('^,]%4B|@56a![0{2m>b1&4i4'), 'Bambi')
        self.assertEqual(letters_only('^U)6$22>8p).'), 'Up')
        self.assertEqual(letters_only(',1|2)")A^1<[_)?^"]l[a`3+%!d@8-0_0d.*}i@&n?='), 'Aladdin')
        self.assertEqual(letters_only('I5n!449+c@e*}@@1]p{2@`,~t:i0o%n<3%8'), 'Inception')
        self.assertEqual(letters_only('!)"P[s9)"69}yc3+?1]+33>3ho'), 'Psycho')
        self.assertEqual(letters_only(':~;G{o}o{+524<df~:>}e24{l8:_l]a:?@]%s7'), 'Goodfellas')
        self.assertEqual(letters_only('&&S~]@8>1-0!h#r),80<_>!}|e>_k:'), 'Shrek')
        self.assertEqual(letters_only(')^/|,!!09]=/1<G2?`=[l{a}d9]^i7a0|t6_o2*r'), 'Gladiator')
        self.assertEqual(letters_only(']8;]V9e{=0r!.5t>i<^_g"4o"5~'), 'Vertigo')
        self.assertEqual(letters_only('%%)?"?B#>/_4a#,;t8|m8675a(n'), 'Batman')
        self.assertEqual(letters_only('97H^)~a8567ll*o?"6%)w63e37e<n?@='), 'Halloween')
        
if __name__ == "__main__":
    unittest.main()