import pandas as pd
from sklearn.preprocessing import StandardScaler

train_model1_wo_impact_encoding = pd.read_csv(r'../data/interim/model1_train_set_wo_impact_encoding.csv')
train_model2_wo_impact_encoding = pd.read_csv(r'../data/interim/model2_train_set_wo_impact_encoding.csv')
scaling_train1 = train_model1_wo_impact_encoding.copy()
scaling_train2 = train_model2_wo_impact_encoding.copy()
impact_encode_columns=['race']
def impact_encoding_model1(dataframe):
    for i in impact_encode_columns:
        encodings = train_model1_wo_impact_encoding.groupby([i])['readmitted_general'].mean()
        dataframe[i] = dataframe[i].map(encodings)
def impact_encoding_model2(dataframe):
    for i in impact_encode_columns:
        encodings = train_model2_wo_impact_encoding.groupby([i])['readmitted_type'].mean()
        dataframe[i] = dataframe[i].map(encodings)

impact_encoding_model1(scaling_train1)
impact_encoding_model2(scaling_train2)

#We drop the readmitted columns that have nothing to do with each model
scaling_train1.drop(['readmitted','readmitted_type'], axis=1,inplace=True)
scaling_train2.drop(['readmitted','readmitted_general'], axis=1,inplace=True)

# Target variables are not scaled
no_scale_model1 = ['readmitted_general']
no_scale_model2 = ['readmitted_type']

#Defining feature columns
features_model1 = scaling_train1.drop(no_scale_model1, axis=1).columns
features_model2 = scaling_train2.drop(no_scale_model2, axis=1).columns

#Defining scalers
scaler1 = StandardScaler()
scaler2 = StandardScaler()

#Fitting scalers
scaler1.fit(scaling_train1[features_model1])
scaler2.fit(scaling_train2[features_model2])