from dataset import dtTest, dtTrain, n_feature, CFold, kNN
from euclidean import y_pred, data_prediksi, n_dataTesting, data_sebenarnya

for a in range(0, n_dataTesting):
    # for j in range(0, n_feature ):
    print(dtTest[4,a])
    print(data_sebenarnya[a]) 
    print(data_prediksi[a])
    print('\n')    