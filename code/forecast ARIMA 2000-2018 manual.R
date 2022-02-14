library (forecast)
library (tseries)
library(plyr)

df <- read.csv(file = 'years.csv')

mainData <- count(df, "YEAR4")

dfTs <- ts(mainData$freq,start=c(2000),end=c(2018)) # start end years
autoplot(dfTs)
#adf.test(dfTs) #check p value
# if p is not less than 0.01
dfTs2 <- diff(dfTs, differences=11) # d
adf.test(dfTs2) 

#Pacf(dfTs) # test for p
#Acf(dfTs2) # test for q

tsPDQ <- Arima(y = dfTs,order=c(1,11,2)) #     p d q 

forecast(tsPDQ)

autoplot(forecast(tsPDQ))



