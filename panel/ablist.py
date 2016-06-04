class ablist:
	"""list of antibodies"""
	def total_t_cell_list():
		ls= (
			('CD2','CD2 (LFA-2)'),
			('CD3','CD3'),
			('CD4','CD4'),
			('CD5','CD5'),
			('CD7','CD7'),
			('CD8','CD8'),
			('CD45','CD45 (Leucocyte Common Antigen)'),
		)
		return ls

	def dendritic_cell_list():
		ls =(
			('CD11c','CD11c'),
			('CD16','CD16'),
			('CD56','CD56 (N-CAM)'),
			('CD80','CD80 (B7-1)'),
			('CD83','CD83'),
			('CD86','CD86 (B70-/B7-2)'),
			('CD123','CD123 (IL-3 Receptor α chain)'),
			('CD209','CD209 (DC-SIGN)'),
			('HLA-DR','HLA-DR'),
			('Lin-1','Lin-1'),
			('Lin-2','Lin-2'),
			('Lin-3','Lin-3'),
		)

	def b_cell_list():
		ls =(
			('CD5','CD5'),
			('CD19','CD19'),
			('CD23','CD23'),
			('CD20','CD20'),
			('CD23','CD23'),
			('CD38','CD38'),
			('CD45','CD45 (Leucocyte Common Antigen)'),
			('lg, ϰ light chain','lg, ϰ light chain'),
			('lg, λ light chain','lg, λ light chain'),
			('FMC7','FMC7'),
		)

	def myeloid_cell_list():
		ls =(
			('CD11b', 'CD11b/Mac-1 (CR3)'),
			('CD13', 'CD13'),
			('CD14', 'CD14'),
			('CD15', 'CD15'),
			('CD16', 'CD16'),
			('CD33', 'CD33'),
			('CD45','CD45 (Leucocyte Common Antigen)'),
			('CD64', 'CD64'),
		)
