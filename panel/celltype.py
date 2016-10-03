from .ablist import *

class celltype:
	def cell_types():
		cell_types = (
			# Need to add antibodies list from ablist on the left in the tuple below
			('T Cell','T Cell'),
			('Dentritic Cell', 'Dendritic Cell'),
			('B Cell','B Cell'),
			('Astrocyte',''),
			('Basophil',''),
			('Embryonic',''),
			('Endothelial Cell',''),
			('Eosinophil',''),
			('Epithelial Cell',''),
			('Erythrocyte',''),
			('Fibroblast',''),
			('Hematopoietic Stem Cell',''),
			('Macrophage',''),
			('Mast Cell',''),
			('MDSC',''),
			('Megakarocyte',''),
			('Mesenchymal Stem Cell',''),
			('Microglia',''),
			('Myeloid Dendritic Cell',''),
			('Naive T Cell',''),
			('Neurons',''),
			('Netrophil',''),
			('NK Cell',''),
			('Plasmacytoid Dendritic Cell',''),
			('Platelets',''),
			('Stromal Cell',''),
			('T Follicular Helper',''),
			('Th1',''),
			('Th2',''),
			('Th9',''),
			('Th17',''),
			('Th22',''),
			('Treg',''),
			)
		return cell_types