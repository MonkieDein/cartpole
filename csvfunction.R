BindCsv <- function(dirname,fn,range){
  # Create a dataframe
  df = {}
  # For all existing range bind all datas
  for (i2 in 1:range){
    filename = paste0(dirname,"/",fn,i2,".csv")
    df = rbind(df,read.csv(filename))
  }
  return(df)
}


CreateSym <- function(df){
  # Create symmetric data
  dfsym = df
  dfsym[,2:5] = -dfsym[,2:5]
  dfsym$Action = as.numeric(dfsym$Action==0)
  # Combined symmetric data
  df = rbind(df,dfsym)
  return(df)
}




