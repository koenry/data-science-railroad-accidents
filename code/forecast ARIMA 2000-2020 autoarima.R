library (forecast)
library (tseries)
library(plyr)

df <- read.csv(file = 'years.csv')


mainData <- count(df, "YEAR4")

mainData

dfTs <- ts(mainData$freq,start=c(2000))

new <- auto.arima(dfTs)

f4cast = forecast(new, 10)
autoplot(f4cast)

