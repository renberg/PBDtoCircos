import Bio
import Bio.PBD
import Bio.Struct


#First, create a PDBParser object:
parser = PDBParser()
#Then, create a structure object from a PDB file in the following way (the PDB file in this case is called '1FAT.pdb', 'PHA-L' is a user defined name for the structure):
pdbstructure = parser.get_structure('1OTH', '1OTH.pdb')
