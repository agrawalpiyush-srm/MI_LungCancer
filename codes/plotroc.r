### https://rstudio-pubs-static.s3.amazonaws.com/313760_3b2a1f8a53f6453db0b0b9db3e81544d.html
library(plotROC)
library(pROC)
library(ROCR)
data=read.table("ROC_input_file",header=T,sep="\t")

svm.act <- prediction(data$SVM_Pred, data$SVM_Act)
perf.svmact <- performance(svm.act, 'tpr', 'fpr')

rf.act <- prediction(data$RF_Pred, data$RF_Act)
perf.rfact <- performance(rf.act, 'tpr', 'fpr')

plot(perf.svmact, col="red",main="Independent Dataset (GSE62646)")
plot(perf.rfact, col="blue",add=TRUE)

legend(0.6,0.27,c('SVM, AUC = 0.99','RF, AUC = 0.95'),col=c('red','blue'),lwd=3)

ggsave("MI_Indep_Validation.png", units="in", width=6, height=4, dpi=600)
dev.off()
