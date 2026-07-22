#set your working directory!

#install.packages("ape")

library(ape)

#to get STRUCTURE format

# read in data
dat <- read.dna("Apis_m_mtDNA_NA_subset.fst", format = "fasta")
dat.matrix <- read.dna("Apis_m_mtDNA_NA_subset.fst", format = "fasta", as.character = TRUE)

if(file.exists("output.prn")){file.remove("output.prn")}

dat.matrix[dat.matrix == "-"] <- "?"

dat.matrix[dat.matrix == "N"] <- "?"

dat.matrix[dat.matrix == "n"] <- "?"

x2 <- dat.matrix

colnames(x2) <- paste("locus", seq(ncol(x2)), sep = "")

x3 <- rbind(x2, x2)
row.names(x3) <- NULL

x3 <- cbind(x3, 1)

colnames(x3)[ncol(x3)] <- "pop" 

for(i in 1:nrow(x2)){
	
	x3[((2*i)-1), 1:(ncol(x3)-1)] <- x2[i,]
	x3[((2*i)), 1:(ncol(x3)-1)] <- x2[i, ]
	
	x3[((2*i)-1),"pop"] <- rownames(x2)[i]
	x3[((2*i)),"pop"] <- rownames(x2)[i]

	
}

x4 <- as.matrix(x3)

is.odd <- function(x) x %% 2 != 0
is.even <- function(x) x %% 2 == 0

for(i in 1:(ncol(x4)-1)){
	
	for(j in 1:nrow(x4)){
		
		if(!is.na(x4[j,i])){
			
			if(x4[j,i] == "y"){
			
				if(is.odd(j)){
				
					x4[j,i] <- "?"
				
				}else{
				
						x4[j,i] <- "?"
				
				}
			
			}	

			if(x4[j,i] == "r"){
			
				if(is.odd(j)){
				
					x4[j,i] <- "?"
				
				}else{
				
						x4[j,i] <- "?"
				
				}
			
			}

			if(x4[j,i] == "w"){
			
				if(is.odd(j)){
				
					x4[j,i] <- "?"
				
				}else{
				
						x4[j,i] <- "?"
				
				}
			
			}

			if(x4[j,i] == "s"){
			
				if(is.odd(j)){
				
					x4[j,i] <- "?"
				
				}else{
				
						x4[j,i] <- "?"
				
				}
			
			}

			if(x4[j,i] == "k"){
			
				if(is.odd(j)){
				
					x4[j,i] <- "?"
				
				}else{
				
						x4[j,i] <- "?"
				
				}
			
			}

			if(x4[j,i] == "m"){
			
				if(is.odd(j)){
				
					x4[j,i] <- "?"
				
				}else{
				
						x4[j,i] <- "?"
				
				}
			
			}			
			
		}
	
	}
	
}

rownames(x4) <- x4[,"pop"]

x4 <- x4[order(rownames(x4)),] 

x5 <- x4[,-which(colnames(x4) == "pop")]

x6 <- x5

x6[x6 == "?"] <- -999

x7 <- NULL
for(i in 1:ncol(x6)){
	
	x7 <- cbind(x7, match(x6[,i], letters[1:26]))
	
}

x7[which(is.na(x7))] <- -999

colnames(x7) <- colnames(x6)
rownames(x7) <- rownames(x6)

x8 <- x7[which(is.odd(1:nrow(x7))),]

write.table(paste(colnames(x8), collapse = " "), sep = " ", col.names = FALSE, row.names = FALSE, quote = FALSE, "output.prn")

write.table(x8, col.names = FALSE, sep = " ", "output.prn", quote = FALSE, append = TRUE)

structure.info <- c(ncol(x8), nrow(x8))

names(structure.info) <- c("number.loci", "number.individuals")

write.table(structure.info, "structure_info.csv", sep = ",", col.names = FALSE)