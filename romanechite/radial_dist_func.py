import matplotlib.pyplot as plt
from pymatgen.io.vasp.inputs import Poscar
from pymatgen_diffusion.aimd.van_hove import RadialDistributionFunction

plt.rc('text', usetex=True)
plt.rc('font', family="sans-serif", serif="Palatino")
plt.rcParams['text.latex.preamble'] = [
    r'\usepackage{amssymb}'
    r'\usepackage{siunitx}',
    r'\sisetup{detect-all}',
    r'\usepackage[cm]{sfmath}']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = 'cm'
plt.rcParams['xtick.major.size'] = 8
plt.rcParams['xtick.major.width'] = 3
plt.rcParams['xtick.minor.size'] = 4
plt.rcParams['xtick.minor.width'] = 3
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.major.size'] = 8
plt.rcParams['ytick.major.width'] = 3
plt.rcParams['ytick.minor.size'] = 4
plt.rcParams['ytick.minor.width'] = 3
plt.rcParams['ytick.labelsize'] = 18
plt.rcParams['axes.linewidth'] = 3

roman_st  = Poscar.from_file('pristine/DOS/CONTCAR')
rutile_st = Poscar.from_file('../simple/rutile/DOS/CONTCAR')
holla_st = Poscar.from_file('../from_TiO2/mvc-12404_TiO2/DOS/CONTCAR')
roman_1sr_st = Poscar.from_file('sr_filling/1/DOS/CONTCAR')
roman_2sra_st = Poscar.from_file('sr_filling/2/a/DOS/CONTCAR')
roman_2srb_st = Poscar.from_file('sr_filling/2/b/DOS/CONTCAR')
roman_3sr_st = Poscar.from_file('sr_filling/3/DOS/CONTCAR')
roman_4sr_st = Poscar.from_file('sr_filling/4/DOS/CONTCAR')

mysigma = 0.05
mygrid = 1001
myrmax = 10

roman_data = RadialDistributionFunction([roman_st.structure], ngrid=mygrid, rmax=myrmax, cellrange=1, sigma=mysigma,
                                        species=["O"], reference_species=["Ir"])
rutile_data = RadialDistributionFunction([rutile_st.structure], ngrid=mygrid, rmax=myrmax, cellrange=1, sigma=mysigma,
                                        species=["O"], reference_species=["Ir"])
holla_data = RadialDistributionFunction([holla_st.structure], ngrid=mygrid, rmax=myrmax, cellrange=1, sigma=mysigma,
                                        species=["O"], reference_species=["Ir"])
roman_1sr_data = RadialDistributionFunction([roman_1sr_st.structure], ngrid=mygrid, rmax=myrmax, cellrange=1, sigma=mysigma,
                                        species=["O"], reference_species=["Ir"])
roman_2sra_data = RadialDistributionFunction([roman_2sra_st.structure], ngrid=mygrid, rmax=myrmax, cellrange=1, sigma=mysigma,
                                        species=["O"], reference_species=["Ir"])
roman_2srb_data = RadialDistributionFunction([roman_2srb_st.structure], ngrid=mygrid, rmax=myrmax, cellrange=1, sigma=mysigma,
                                        species=["O"], reference_species=["Ir"])
roman_3sr_data = RadialDistributionFunction([roman_3sr_st.structure], ngrid=mygrid, rmax=myrmax, cellrange=1, sigma=mysigma,
                                        species=["O"], reference_species=["Ir"])
roman_4sr_data = RadialDistributionFunction([roman_4sr_st.structure], ngrid=mygrid, rmax=myrmax, cellrange=1, sigma=mysigma,
                                        species=["O"], reference_species=["Ir"])

fig, ax1 = plt.subplots()
#ax2 = ax1.twinx()

# RDF plots
if 1==1:
    plt.title(r'Radial Distribution Function')
    ax1.set_ylabel(r'RDF [g(r)]', fontsize=14)
    ax1.plot(roman_data.interval, roman_data.rdf, color='navy', linewidth=0.75, label=r'Romanechite')
    ax1.plot(rutile_data.interval, rutile_data.rdf, color='g', linewidth=0.75, label=r'Rutile')
    ax1.plot(holla_data.interval, holla_data.rdf, color='b', linewidth=0.75, label=r'Hollandite')
    ax1.plot(roman_1sr_data.interval, roman_1sr_data.rdf, color='m', linewidth=0.75, label=r'Romanechite +1Sr')
    ax1.plot(roman_2sra_data.interval, roman_2sra_data.rdf, color='y', linewidth=0.75, label=r'Romanechite +2Sr \#1')
    ax1.plot(roman_2srb_data.interval, roman_2srb_data.rdf, color='brown', linewidth=0.75, label=r'Romanechite +2Sr \#2')
    ax1.plot(roman_3sr_data.interval, roman_3sr_data.rdf, color='r', linewidth=0.75, label=r'Romanechite +3Sr')
    ax1.plot(roman_4sr_data.interval, roman_4sr_data.rdf, color='orange', linewidth=0.75, label=r'Romanechite +4Sr')

#CN plots
if 1==2:
    plt.title(r'Coordination Number')
    ax1.set_ylabel(r'CN [n(g(r))]', fontsize=14)
    ax1.plot(roman_data.interval, roman_data.coordination_number, color='navy', linewidth=0.75, label=r'Romanechite')
    ax1.plot(rutile_data.interval, rutile_data.coordination_number, color='g', linewidth=0.75, label=r'Rutile')
    ax1.plot(holla_data.interval, holla_data.coordination_number, color='b', linewidth=0.75, label=r'Hollandite')
    ax1.plot(roman_1sr_data.interval, roman_1sr_data.coordination_number, color='m', linewidth=0.75, label=r'Romanechite +1Sr')
    ax1.plot(roman_2sra_data.interval, roman_2sra_data.coordination_number, color='y', linewidth=0.75, label=r'Romanechite +2Sr \#1')
    ax1.plot(roman_2srb_data.interval, roman_2srb_data.coordination_number, color='b', linewidth=0.75, label=r'Romanechite +2Sr \#2')
    ax1.plot(roman_3sr_data.interval, roman_3sr_data.coordination_number, color='r', linewidth=0.75, label=r'Romanechite +3Sr')
    ax1.plot(roman_4sr_data.interval, roman_4sr_data.coordination_number, color='o', linewidth=0.75, label=r'Romanechite +4Sr')


#ax2.plot(rprist.interval, rprist.coordination_number, color='r')

ax1.set_xlabel(r'r [$\AA$]', fontsize=14)

#ax2.legend(frameon=False)
#plt.suptitle('Li-S 0K sigma 0.1 pym-diff latest version',fontsize=9)

ax1.set_xlim((0,10))
ax1.set_ylim((0,17))

#ax2.set_xlim((0,10))
#ax2.set_ylim((0,20))

plt.legend(fontsize=14)

plt.tight_layout()
plt.savefig('all_rdf.png', dpi=600)