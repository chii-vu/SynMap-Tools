# SynMap Workflow

qID, sID = CoGe.ParseIDs(query=query,subject=subject)

# Run whole genome comparison
blastz = blast.BlastZ(query=query,db=subject)

# Generate BED files from BLAST result
bedfiles = blast.Blast2Bed(blastz)

# Filter tandem duplicates from BED files
filtered_dups = blast.BlastToRaw(blast=blastz, qbed=bedfiles[0],sbed=bedfiles[1],tandem_Nmax=10,cscore=0)

# Process Query Tandem Duplicate File
query_dups = CoGe.ProcessDups(data=filtered_dups[0])

# Processing Subject Tandem Duplicate File
subject_dups = CoGe.ProcessDups(data=filtered_dups[2])

# Format file for DAGChainer
dag_formatted = CoGe.DAGFormatter(blast_file=filtered_dups[4],query='a'+qID,subject='b'+sID)

# Convert to genomic order
gene_order = CoGe.GeneOrder(input=dag_formatted,gid1=qID,gid2=sID,feature1='CDS',feature2='CDS')

# Run DAGChainer
dagchainer = CoGe.DagChainer(dag=gene_order,gap_init=0,gap_extend=-3,min_score=0,gap_dist=10.0,gap_max=20.0,e_value=0.05,min_aligned_pairs=5)

# Convert to genomic coordinates
gene_coords = CoGe.GeneOrder(input=dagchainer,gid1='',gid2='',feature1='CDS',feature2='CDS')

# Calculate synonymous mutation values
ks_file = CoGe.KsCalcZero(gene_coords)

# Generate GEvo links
gevo_links, condensed_links = CoGe.GevoLink(data=gene_coords,dsgid1=qID,dsgid2=sID)

# Generate .svg image
dotplot = CoGe.DotPlot(dag_file=gene_coords,xhead="",yhead="")

return ks_file