from pymatgen import Structure

s1 = Structure.from_file('96_1.vasp')
s2 = Structure.from_file('96_2.vasp')
s3 = Structure.from_file('192.vasp')

s1.to(fmt='cif', filename='96_1.cif')
s2.to(fmt='cif', filename='96_2.cif')
s3.to(fmt='cif', filename='192.cif')

