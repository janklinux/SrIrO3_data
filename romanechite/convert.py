from pymatgen import Structure

st = Structure.from_file('AMS_DATA.cif')
print st
st.to(filename='POSCAR',fmt='POSCAR')
