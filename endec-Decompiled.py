# uncompyle6 version 3.3.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Apr 24 2019, 10:05:31) 
# [GCC 4.2.1 Compatible Android (5058415 based on r339409) Clang 8.0.2 (https://a
# Embedded file name: <ZBL>
# Compiled at: 2018-02-25 13:25:47
import os, sys, time, random, base64, marshal
m = '\x1b[1;91m'
u = '\x1b[1;95m'
h = '\x1b[1;92m'
p = '\x1b[0m'

def run(x):
    pt = '\x1b[0m'
    rd = '\x1b[0m\x1b[92m'
    rg = '\x1b[2;91m'
    try:
        num = 0
        while num < 1:
            for i, char in enumerate(x):
                if i == 0:
                    print '\r%s%s%s%s' % (rg, char.lower(), rd, x[1:]),
                    sys.stdout.flush()
                else:
                    if i == 1:
                        zbl = x[0].lower()
                        print '\r%s%s%s%s%s%s' % (rd, zbl, pt, char.lower(), rg, x[2:]),
                        sys.stdout.flush()
                    else:
                        if i == i:
                            zbl = x[0:i].lower()
                            print '\r%s%s%s%s%s%s' % (rd, zbl, pt, char.lower(), rg, x[i + 1:]),
                            sys.stdout.flush()
                    time.sleep(0.05)

            num += 1

    except:
        exit()


def clr():
    os.system('clear')


def logo():
    clr()
    print u + '______ ______ _____  ______ ______\n@@@@@@ @@@@@@ @@@@@\\ @@@@@@ @@@@@@|\n@@|_@@ @@| @@ @@| @@ @@|_@@ @@| @@|\n@@@@@@ @@| @@ @@| @@ @@@@@@ @@| __\n@@|___ @@| @@ @@|_@@ @@|___ @@|_@@|\n@@@@@@ @@| @@ @@@@@/ @@@@@@ @@@@@@|'
    print ('%sCoded by: %sZhu Bai Lee').center(40) % (h, p)


def menu():
    logo()
    print '\n01) Encrypt Base16\n02) Encrypt Base32\n03) Encrypt Base64\n04) Encrypt Hex\n05) Encrypt Marshal\n06) Decrypt base16\n07) Decrypt base32\n08) Decrypt base64\n09) Decrypt Hex\n00) Exit'
    try:
        inp = raw_input('Choose: ')
    except:
        exit()

    if inp == '1' or inp == '01':
        clr()
        logo()
        try:
            f = raw_input('Filenames: ')
        except:
            exit()
        else:
            try:
                bk = open(f, 'r').read()
            except:
                run('file %s tidak ditemukan ' % f)
                exit()

        en = base64.b16encode(bk)
        ff = f + 'c'
        open(ff, 'w').write('import base64\nexec(base64.b16decode("%s"))' % en)
        nm = ('').join(f.split('.')[:1]) + '-enc.py'
        os.rename(ff, nm)
        run('file berhasil di encrypt menjadi %s ' % nm)
    else:
        if inp == '2' or inp == '02':
            clr()
            logo()
            try:
                f = raw_input('Filenames: ')
            except:
                exit()
            else:
                try:
                    bk = open(f, 'r').read()
                except:
                    run('file %s tidak ditemukan ' % f)
                    exit()

            en = base64.b32encode(bk)
            ff = f + 'c'
            open(ff, 'w').write('import base64\nexec(base64.b32decode("' + en + '"))')
            nm = ('').join(f.split('.')[:1]) + '-enc.py'
            os.rename(ff, nm)
            run('file berhasil di encrypt menjadi %s ' % nm)
        else:
            if inp == '3' or inp == '03':
                clr()
                logo()
                try:
                    f = raw_input('Filenames: ')
                except:
                    exit()
                else:
                    try:
                        bk = open(f, 'r').read()
                    except:
                        run('file %s tidak ditemukan ' % f)
                        exit()

                en = base64.b64encode(bk)
                ff = f + 'c'
                open(ff, 'w').write('import base64\nexec(base64.b64decode("' + en + '"))')
                nm = ('').join(f.split('.')[:1]) + '-enc.py'
                os.rename(ff, nm)
                run('file berhasil di encrypt menjadi %s ' % nm)
            else:
                if inp == '4' or inp == '04':
                    clr()
                    logo()
                    try:
                        f = raw_input('Filenames: ')
                    except:
                        exit()
                    else:
                        try:
                            bk = open(f, 'r').read()
                        except:
                            run('file %s tidak ditemukan ' % f)
                            exit()

                    en = bk.encode('hex')
                    ff = f + 'c'
                    open(ff, 'w').write('exec("' + en + '").decode("hex")')
                    nm = ('').join(f.split('.')[:1]) + '-enc.py'
                    os.rename(ff, nm)
                    run('file berhasil di encrypt menjadi %s ' % nm)
                else:
                    if inp == '5' or inp == '05':
                        clr()
                        logo()
                        try:
                            f = raw_input('Filenames: ')
                        except:
                            exit()
                        else:
                            try:
                                bk = open(f, 'r').read()
                            except:
                                run('file %s tidak ditemukan ' % f)
                                exit()

                        c = compile(bk, '<zbl>', 'exec')
                        en = marshal.dumps(c)
                        ff = f + 'c'
                        open(ff, 'w').write('import marshal\nexec(marshal.loads(' + repr(en) + '))')
                        nm = ('').join(f.split('.')[:1]) + '-zbl.py'
                        os.rename(ff, nm)
                        run('file berhasil di encrypt menjadi %s ' % nm)
                    else:
                        if inp == '6' or inp == '06':
                            clr()
                            logo()
                            try:
                                f = raw_input('Filenames: ')
                            except:
                                exit()
                            else:
                                try:
                                    bk = open(f, 'r').read()
                                except:
                                    run('file %s tidak ditemukan ' % f)
                                    exit()

                            bk = bk.replace('exec(base64.b16decode("', '')
                            bk = bk.replace('"))', '')
                            bk = bk.replace('import base64\n', '')
                            en = base64.b16decode(bk)
                            ff = f + 'c'
                            open(ff, 'w').write(en)
                            nm = ('').join(f.split('.')[:1]) + '-dec.py'
                            os.rename(ff, nm)
                            run('file berhasil di decrypt menjadi %s ' % nm)
                        else:
                            if inp == '7' or inp == '07':
                                clr()
                                logo()
                                try:
                                    f = raw_input('Filenames: ')
                                except:
                                    exit()
                                else:
                                    try:
                                        bk = open(f, 'r').read()
                                    except:
                                        run('file %s tidak ditemukan ' % f)
                                        exit()

                                bk = bk.replace('exec(base64.b32decode("', '')
                                bk = bk.replace('"))', '')
                                bk = bk.replace('import base64\n', '')
                                en = base64.b32decode(bk)
                                ff = f + 'c'
                                open(ff, 'w').write(en)
                                nm = ('').join(f.split('.')[:1]) + '-dec.py'
                                os.rename(ff, nm)
                                run('file berhasil di decrypt menjadi %s ' % nm)
                            else:
                                if inp == '8' or inp == '08':
                                    clr()
                                    logo()
                                    try:
                                        f = raw_input('Filenames: ')
                                    except:
                                        exit()
                                    else:
                                        try:
                                            bk = open(f, 'r').read()
                                        except:
                                            run('file %s tidak ditemukan ' % f)
                                            exit()

                                    bk = bk.replace(+'exec(base64.b64decode("', '')
                                    bk = bk.replace('"))', '')
                                    bk = bk.replace('import base64\n', '')
                                    en = base64.b64decode(bk)
                                    ff = f + 'c'
                                    open(ff, 'w').write(en)
                                    nm = ('').join(f.split('.')[:1]) + '-dec.py'
                                    os.rename(ff, nm)
                                    run('file berhasil di decrypt menjadi %s ' % nm)
                                else:
                                    if inp == '9' or inp == '09':
                                        clr()
                                        logo()
                                        try:
                                            f = raw_input('Filenames: ')
                                        except:
                                            exit()
                                        else:
                                            try:
                                                bk = open(f, 'r').read()
                                            except:
                                                run('file %s tidak ditemukan ' % f)
                                                exit()

                                        bk = bk.replace('exec("', '') or bk.replace("exec('", '')
                                        bk = bk.replace('").decode("hex")', '') or bk.replace("').decode('hex')", '')
                                        en = str(bk).decode('hex')
                                        ff = f + 'c'
                                        open(ff, 'w').write(en)
                                        nm = ('').join(f.split('.')[:1]) + '-dec.py'
                                        os.rename(ff, nm)
                                        run('file berhasil di decrypt menjadi %s ' % nm)
                                    else:
                                        if inp == '0' or inp == '00':
                                            run('thank for using my tools ')
                                            exit()
                                        else:
                                            exit()


menu()
# okay decompiling 3.pyc
