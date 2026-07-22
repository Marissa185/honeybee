#Don't forget to set your working directory! I recommend setting it to the directory where you have your STRUCTURE results files and NOTHING ELSE.

#install.packages(c("devtools","ggplot2","gridExtra","gtable","label.switching","tidyr"),dependencies=T)

library(devtools)
install_github('royfrancis/pophelper')

library(pophelper)
library(gridExtra)

# STRUCTURE files (do not use this command to read local files)
sfiles <- list.files(path="/home/marissa/Documents/Msc_project/7_Analysis/3_structure/3_subset/result", full.names=T) # <-- Look carefully here! You must put in the path where you have put the results files. No other files can be in that directory!
# basic usage
slist <- readQ(files=sfiles)
readQ(files=sfiles,filetype="structure")

sr1 <- summariseQ(tabulateQ(slist))

write.csv(evannoMethodStructure(sr1), "evannoMethodStructure.csv", na = "") 
p <- evannoMethodStructure(data=sr1,exportplot=F,returnplot=T,returndata=F,basesize=12,linesize=0.7)
grid.arrange(p)