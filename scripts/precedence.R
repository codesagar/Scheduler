prefrences <- read.csv("/home/sagar/Dropbox/Scheduler/data/prefrences.csv")
library(dummies)
x=dummy(prefrences$Competency,sep="_")
x = data.frame(x)
x$Competency_Not.Comfortable <- NULL
new_df = cbind(x,prefrences[,-1])
model = lm(Score ~ . -Rank, data=new_df)
summary(model)
prefrences$predict <- predict(model)

prefrences <- prefrences[order(prefrences$predict,decreasing = T),]
View(prefrences)
write.csv(prefrences[order(prefrences$Rank),1:4],'/home/sagar/Dropbox/Scheduler/data/prefrences_out.csv',row.names = F)
