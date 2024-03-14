df=PlayersChampionshipData
df=subset(df,select = -c(R1,R2,R3,R4,SGttg,PLAYER))
# Load required libraries
library(caret)
library(randomForest)
library(xgboost)

# Split the data into training and testing sets
set.seed(123)  # for reproducibility
train_index <- createDataPartition(df$TOT, p = 0.8, list = FALSE)
train_data <- df[train_index, ]
test_data <- df[-train_index, ]

# Linear Regression model
lm_modelplayers <- lm(TOT ~. , data = train_data)

# Random Forest model
rf_model <- randomForest(TOT ~ ., data = train_data)

# XGBoost model
xgb_model <- xgboost(data = as.matrix(train_data[, -which(names(train_data) == "TOT")]), 
                     label = train_data$TOT, 
                     nrounds = 100, 
                     objective = "reg:squarederror")
# Predictions
lm_pred <- predict(lm_modelplayers, newdata = test_data)
rf_pred <- predict(rf_model, newdata = test_data)
xgb_pred <- predict(xgb_model, newdata = as.matrix(test_data[, -which(names(test_data) == "TOT")]))

# Calculate RMSE (Root Mean Squared Error) for each model
lm_rmse <- sqrt(mean((test_data$TOT - lm_pred)^2))
rf_rmse <- sqrt(mean((test_data$TOT - rf_pred)^2))
xgb_rmse <- sqrt(mean((test_data$TOT - xgb_pred)^2))

# Print RMSE for each model
print(paste("Linear Regression RMSE:", lm_rmse))
print(paste("Random Forest RMSE:", rf_rmse))
print(paste("XGBoost RMSE:", xgb_rmse))

num_folds <- 10

# Define the cross-validation control
ctrl <- trainControl(method = "cv", 
                     number = num_folds,
                     verboseIter = TRUE)

# Define the model using train function
model <- train(TOT ~ ., 
               data = df, 
               method = "lm",  # Linear regression model
               trControl = ctrl)

# Print the cross-validation results
print(model)

#VIF
vif(lm_modelplayers)

#Assumptions
plot(lm_modelplayers, which=1, col=c("blue")) # residuals vs fitted 
plot(lm_modelplayers, which=2, col=c("blue")) # qq plot for normality
plot(lm_modelplayers, which=3, col=c("blue")) # for equal variance
plot(lm_modelplayers, which=5, col=c("blue")) #Residual vs Leverage

#Predictions
lm_modelplayers <- update(lm_modelplayers, . ~ . +SCR)
predictionfinal=predict.lm(lm_modelplayers,newdata=Predictionraw)
Predictionraw$Totalfinal=predictionfinal #add score predictions from model to data frame
Predictionraw$finaltopar=Predictionraw$Totalfinal-288
summary(lm_modelplayers)


#Export
write.xlsx(Predictionraw, file = "PlayersModelResults.xlsx")

# Load the Shiny library


