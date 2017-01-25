from .ablist import *

class celltype:
	def cell_types():
		cell_types = (
			# Need to add antibodies list from ablist on the left in the tuple below
			('T Cell','T Cell'),
			('Dentritic Cell', 'Dendritic Cell'),
			('B Cell','B Cell'),
			('Astrocyte','Astrocyte'),
			('Basophil','Basophil'),
			('Embryonic','Embryonic'),
			('Endothelial Cell','Endothelial Cell'),
			('Eosinophil','Eosinophil'),
			('Epithelial Cell','Epithelial Cell'),
			('Erythrocyte','Erythrocyte'),
			('Fibroblast','Fibroblast'),
			('Hematopoietic Stem Cell',''),
			('Macrophage','Macrophage'),
			('Mast Cell','Mast Cell'),
			('MDSC','MDSC'),
			('Megakarocyte','Megakarocyte'),
			('Mesenchymal Stem Cell','Mesenchymal Stem Cell'),
			('Microglia','Microglia'),
			('Myeloid Dendritic Cell','Myeloid Dendritic Cell'),
			('Naive T Cell','Naive T Cell'),
			('Neurons','Neurons'),
			('Netrophil','Netrophil'),
			('NK Cell','NK Cell'),
			('Plasmacytoid Dendritic Cell','Plasmacytoid Dendritic Cell'),
			('Platelets','Platelets'),
			('Stromal Cell','Stromal Cell'),
			('T Follicular Helper','T Follicular Helper'),
			('Th1','T helper cells 1'),
			('Th2','T helper cells 2'),
			('Th9','T helper cells 9'),
			('Th17','T helper cells 17'),
			('Th22','T helper cells 22'),
			('Treg','Regulatory T cell'),
			)
		return cell_types