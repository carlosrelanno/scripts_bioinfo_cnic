file <- commandArgs(trailingOnly = TRUE)[1L]

namer::name_chunks(file)
rmarkdown::render(file)
