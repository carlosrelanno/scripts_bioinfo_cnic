echo "Lets go"
start=$(date +%s)
date

source /data3/crelanor/SC.analysis.cluster/miniconda3.v4.9.2.cluster.source
conda activate r-markdown
Rscript /data3/crelanor/scripts/render.rmarkdown/render.R $1

end=$(date +%s)
echo "Runtime: $(($end-$start)) seconds"
