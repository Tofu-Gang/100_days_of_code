import unittest

from src.day_008_caesar_cipher.caesar_cipher import encode_message, decode_message


########################################################################################################################

class TestChallenge008(unittest.TestCase):

    def test_encode(self):
        self.assertEqual("svylt pwzbt kvsvy zpa htla, jvuzljalaby hkpwpzjpun lspa, zlk kv lpbztvk altwvy pujpkpkbua ba shivyl la kvsvyl thnuh hspxbh. ba lupt hk tpupt clupht, xbpz uvzaybk lelyjpahapvu bsshtjv shivypz upzp ba hspxbpw le lh jvttvkv jvuzlxbha. kbpz hbal pybyl kvsvy pu ylwyloluklypa pu cvsbwahal clspa lzzl jpssbt kvsvyl lb mbnpha ubssh whyphaby. lejlwalby zpua vjjhljha jbwpkhaha uvu wyvpklua, zbua pu jbswh xbp vmmpjph klzlybua tvsspa hupt pk lza shivybt.",
                         encode_message("lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", 7))

########################################################################################################################

    def test_decode(self):
        self.assertEqual("lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
                         decode_message("behuc yfikc tebeh iyj qcuj, sediusjujkh qtyfyisydw ubyj, iut te uykicet jucfeh ydsytytkdj kj bqrehu uj tebehu cqwdq qbygkq. kj udyc qt cydyc ludyqc, gkyi deijhkt unuhsyjqjyed kbbqcse bqrehyi dyiy kj qbygkyf un uq seccete sediugkqj. tkyi qkju yhkhu tebeh yd hufhuxudtuhyj yd lebkfjqju lubyj uiiu sybbkc tebehu uk vkwyqj dkbbq fqhyqjkh. unsufjukh iydj essqusqj skfytqjqj ded fheytudj, ikdj yd skbfq gky evvysyq tuiuhkdj cebbyj qdyc yt uij bqrehkc.", 42))


########################################################################################################################

if __name__ == '__main__':
    unittest.main()

########################################################################################################################
