#!/usr/bin/env python
# encoding: utf8

import pkg_resources

_a = unichr(261)
_A = unichr(260)
_c = unichr(263)
_C = unichr(262)
_e = unichr(281)
_E = unichr(280)
_l = unichr(322)
_L = unichr(321)
_n = unichr(324)
_N = unichr(323)
_o = unichr(243)
_O = unichr(211)
_s = unichr(347)
_S = unichr(346)
_z1 = unichr(378)
_Z1 = unichr(377)
_z2 = unichr(380)
_Z2 = unichr(379)

TYPE_MIANOWNIK = 0
TYPE_DOPELNIACZ = 1
TYPE_CELOWNIK = 2
TYPE_BIERNIK = 3
TYPE_NARZEDNIK = 4
TYPE_MIEJSCOWNIK = 5
TYPE_WOLACZ = 6

def convertToUnicode(s):
    result = s.replace('\\304\\205', _a)
    result = result.replace('\\304\\207', _c)
    result = result.replace('\\304\\231', _e)
    result = result.replace('\\305\\202', _l)
    result = result.replace('\\305\\204', _n)
    result = result.replace('\\303\\263', _o)
    result = result.replace('\\305\\233', _s)
    result = result.replace('\\305\\272', _z1)
    result = result.replace('\\305\\274', _z2)
    result = result.replace('\\304\\204', _A)
    result = result.replace('\\304\\206', _C)
    result = result.replace('\\304\\230', _E)
    result = result.replace('\\305\\201', _L)
    result = result.replace('\\305\\203', _N)
    result = result.replace('\\303\\223', _O)
    result = result.replace('\\305\\232', _S)
    result = result.replace('\\305\\271', _Z1)
    result = result.replace('\\305\\273', _Z2)
    return result

class OdmianaRzeczownikow:
    def __init__(self):
        self.str_mianownik = '''Mianownik'''
        self.str_dopelniacz = '''Dope''' + _l + '''niacz'''
        self.str_celownik = '''Celownik'''
        self.str_biernik = '''Biernik'''
        self.str_narzednik = '''Narz''' + _e + '''dnik'''
        self.str_miejscownik = '''Miejscownik'''
        self.str_wolacz = '''Wo''' + _l + '''acz'''
        self.__przypadki__ = [self.str_mianownik, self.str_dopelniacz, self.str_celownik, self.str_biernik,
                            self.str_narzednik, self.str_miejscownik, self.str_wolacz]
        #print 'Nazwy przypadk' + _o + 'w:'
        #print self.przypadki
        blocks_filename = pkg_resources.resource_filename(__name__, 'data/rzecz_pol_compact.txt')
        self.read(blocks_filename)

    def __buildDict__(self):
        self.dicts_lp = []
        self.dicts_lm = []
        for i in range(7):
            self.dicts_lp.append( {} )
            self.dicts_lm.append( {} )

        for i, block in enumerate( self.blocks ):
            block_lp, block_lm = block
            if block_lp:
                for j in range(7):
                    word = block_lp[j] #.decode('utf-8')
                    if not word in self.dicts_lp:
                        self.dicts_lp[j][word] = []
                    self.dicts_lp[j][word].append( i )

            if block_lm:
                for j in range(7):
                    word = block_lm[j] #.decode('utf-8')
                    if not word in self.dicts_lm:
                        self.dicts_lm[j][word] = []
                    self.dicts_lm[j][word].append( i )

    def getBlocks(self, word):
        #if not word.isalpha():
        #    raise Exception('Input word must be alpha character only.')
        if not word.islower():
            raise Exception('Input word must be lowercase.')

        result = []
        for i in range(7):
            if word in self.dicts_lp[i]:
                for block_idx in self.dicts_lp[i][word]:
                    block = self.blocks[block_idx]
                    result.append( (i, 'lp', block) )
            if word in self.dicts_lm[i]:
                for block_idx in self.dicts_lm[i][word]:
                    block = self.blocks[block_idx]
                    result.append( (i, 'lm', block) )
        return result

    def getLp(self, type_id, blocks, mianownik=None):
        result = []
        for word_type, count, (block_lp, block_lm) in blocks:
            if block_lp:
                if mianownik is None:
                    result.append( block_lp[type_id] )
                else:
                    if block_lp[TYPE_MIANOWNIK] == mianownik:
                        result.append( block_lp[type_id] )
        return result

    def getLm(self, type_id, blocks, mianownik=None):
        result = []
        for word_type, count, (block_lp, block_lm) in blocks:
            if block_lp:
                if mianownik is None:
                    result.append( block_lp[type_id] )
                else:
                    if block_lp[TYPE_MIANOWNIK] == mianownik:
                        result.append( block_lp[type_id] )
        return result

    def getMianownikLp(self, blocks):
        return self.getLp(TYPE_MIANOWNIK, blocks)

    def getMianownikLm(self, blocks):
        return self.getLm(TYPE_MIANOWNIK, blocks)

    def getDopelniaczLp(self, blocks, mianownik=None):
        return self.getLp(TYPE_DOPELNIACZ, blocks, mianownik=mianownik)

    def getDopelniaczLm(self, blocks, mianownik=None):
        return self.getLm(TYPE_DOPELNIACZ, blocks, mianownik=mianownik)

    def getCelownikLp(self, blocks, mianownik=None):
        return self.getLp(TYPE_CELOWNIK, blocks, mianownik=mianownik)

    def getCelownikLm(self, blocks, mianownik=None):
        return self.getLm(TYPE_CELOWNIK, blocks, mianownik=mianownik)

    def getBiernikLp(self, blocks, mianownik=None):
        return self.getLp(TYPE_BIERNIK, blocks, mianownik=mianownik)

    def getBiernikLm(self, blocks, mianownik=None):
        return self.getLm(TYPE_BIERNIK, blocks, mianownik=mianownik)

    def przypadki(self, word):
        blocks = self.getBlocks(word)
        if len(blocks) == 0:
            print u'Nie moge znaleźć nazwy miejsca w słowniku'
            word_m = word
        else:
            m_lp = self.getMianownikLp(blocks)
            if len(m_lp) == 0:
                m_lm = self.getMianownikLp(blocks)
                word_m = m_lm[0]
            else:
                word_m = m_lp[0]

        word_d = self.getDopelniaczLp(blocks, mianownik=word_m)
        if len(word_d) == 0:
            word_d = self.getDopelniaczLm(blocks, mianownik=word_m)
        if len(word_d) == 0:
            word_d = [word_m]

        word_c = self.getCelownikLp(blocks, mianownik=word_m)
        if len(word_c) == 0:
            word_c = self.getCelownikLm(blocks, mianownik=word_m)
        if len(word_c) == 0:
            word_c = [word_m]

        word_b = self.getBiernikLp(blocks, mianownik=word_m)
        if len(word_b) == 0:
            word_b = self.getBiernikLm(blocks, mianownik=word_m)
        if len(word_b) == 0:
            word_b = [word_m]

        return word_m, word_d[0], word_c[0], word_b[0]

    def readRaw(self, db_filename):
        with open(db_filename, 'r') as f:
            lines = f.readlines()
        print 'readRaw lines: ' + str(len(lines))

        # Format danych jest nastepujacy:
        # |Mianownik lp = zamek
        # |Dopelniacz lp = zamku
        # |Celownik lp = zamkowi
        # |Biernik lp = zamek
        # |Narzednik lp = zamkiem
        # |Miejscownik lp = zamku
        # |Wolacz lp = zamku
        # |Mianownik lm = zamki
        # |Dopelniacz lm = zamkow
        # |Celownik lm = zamkom
        # |Biernik lm = zamki
        # |Narzednik lm = zamkami
        # |Miejscownik lm = zamkach
        # |Wolacz lm = zamki
        # Kolejnosc moze nie byc zachowana, ale Mianownik lp jest pierwszy.
        # Nazwy przypadkow zawieraja polskie znaki.

        current_idx = 0
        lines_count = len(lines)
        
        self.skipped_lines = []
        self.blocks = []
        loop_counter = 0
        while True:
            block_idx = self.__findRawBlock__( lines, current_idx )
            if block_idx is None:
                break
            block = self.__readRawBlock__( lines, block_idx )
            if block is None:
                #print str(current_idx) + ' / ' + str(lines_count)
                self.skipped_lines.append( lines[current_idx] )
                current_idx += 1
            else:
                if len(block[0]) > 0:
                    #print 'Dodano ' + block[0][0] + ', ' + str(block_idx) + ' / ' + str(lines_count)
                    pass
                else:
                    #print 'Dodano ' + block[1][0] + ', ' + str(block_idx) + ' / ' + str(lines_count)
                    pass
                self.blocks.append( (block[0], block[1]) )
                current_idx = block_idx + block[2]
            loop_counter += 1

        self.__buildDict__()
        print 'Skipped lines: ' + str(len(self.skipped_lines))
        print 'Blocks: ' + str(len(self.blocks))

    def write(self, blocks_filename, skipped_filename):
        with open(blocks_filename, 'w') as f:
            for block in self.blocks:
                if len(block[0]) == 0:
                    line = '*******'
                else:
                    line = ''
                    for i in range(7):
                        line = line + block[0][i] + '*'
                if len(block[1]) == 0:
                    line = line + '******'
                else:
                    for i in range(7):
                        line = line + block[1][i]
                        if i < 6:
                            line = line + '*'
                if line.count('*') != 13:
                    raise Exception('Wrong number of separators: ' + line)
                f.write(line + '\n')

        with open(skipped_filename, 'w') as f:
            for line in self.skipped_lines:
                f.write(line)

    def read(self, blocks_filename):
        with open(blocks_filename, 'r') as f:
            lines = f.readlines()
            self.blocks = []
            self.skipped_lines = []
            for line in lines:
                items = line.split('*')
                assert len(items) == 14
                block_lp = {}
                block_lm = {}
                for i in range(7):
                    lp = items[i].strip().decode('utf-8')
                    if lp != '':
                        block_lp[i] = lp
                    lm = items[i+7].strip().decode('utf-8')
                    if lm != '':
                        block_lm[i] = lm
                self.blocks.append( (block_lp, block_lm) )
        self.__buildDict__()

    def __parsePrzypadek__(self, przypadek):
        if przypadek == self.str_mianownik:
            return TYPE_MIANOWNIK
        elif przypadek == self.str_dopelniacz:
            return TYPE_DOPELNIACZ
        elif przypadek == self.str_celownik:
            return TYPE_CELOWNIK
        elif przypadek == self.str_biernik:
            return TYPE_BIERNIK
        elif przypadek == self.str_narzednik:
            return TYPE_NARZEDNIK
        elif przypadek == self.str_miejscownik:
            return TYPE_MIEJSCOWNIK
        elif przypadek == self.str_wolacz:
            return TYPE_WOLACZ
        else:
            return None

    def __parseRawLine__(self, line):
        if line[0] != '|':
            return None

        eq_idx = line.find('=')
        line_low = line[0:eq_idx]
        line_high = line[eq_idx+1:].strip()

        items = line_low[1:].split()
        assert len(items) == 2

        przypadek = items[0].strip().decode('utf-8')
        przypadek_type = self.__parsePrzypadek__(przypadek)
        if przypadek_type is None:
            return None
        liczba = items[1].strip().decode('utf-8')
        if not liczba in ['lp', 'lm']:
            return None
        word = line_high

        return (przypadek_type, liczba, word)

    def __findRawBlock__(self, lines, index):
        for i in range(index, len(lines)):
            p = self.__parseRawLine__( lines[i] )
            if not p is None and p[0] == TYPE_MIANOWNIK:
                return i
        return None

    def __readRawBlock__(self, lines, index):
        if index >= len(lines)-14:
            #print 'Nie mozna odczytac bloku: przekroczono zakres pliku.'
            return None

        odmiany_lp = {}
        odmiany_lm = {}
        for i in range(7):
            p = self.__parseRawLine__( lines[index+i] )
            if p is None:
                #print 'nie mozna sparsowac linii ' + lines[index+i]
                return None
            if p[1] == 'lp':
                odmiany_lp[p[0]] = p[2]
            else:
                odmiany_lm[p[0]] = p[2]

        brak_lp = (len(odmiany_lp) == 0)
        brak_lm = (len(odmiany_lm) == 0)

        if not brak_lp and not brak_lm:
            for i in range(7):
                p = self.__parseRawLine__( lines[index+i+7] )
                if p is None:
                    #print 'nie mozna sparsowac linii ' + lines[index+i]
                    return None
                if p[1] == 'lp':
                    odmiany_lp[p[0]] = p[2]
                else:
                    odmiany_lm[p[0]] = p[2]

        for przyp_type in range(7):
        #for przyp in self.przypadki:
            if not brak_lp and not przyp_type in odmiany_lp:
                print 'Brakuje ' + str(przyp_type) + ' lp dla slowa ' + str(odmiany_lp)
                return None
            if not brak_lm and not przyp_type in odmiany_lm:
                print 'Brakuje ' + str(przyp_type) + ' lm dla slowa ' + str(odmiany_lm)
                return None

        lines_count = 0
        if not brak_lp:
            lines_count += 7
        if not brak_lm:
            lines_count += 7
        return odmiany_lp, odmiany_lm, lines_count
