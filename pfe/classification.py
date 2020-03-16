import numpy as np
import pickle
import math
import time
import sqlite3
import os
import json
import os.path
from django.conf import settings
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.externals import joblib
import numpy as np
import pickle
class ClassificationDiab():
      # patient = [BMI,ponds,taille, tension systolique, tension dyastolique, age, sexe, diabétique ou pas]
     # How many patient to train the model on
      test_patients_count = 1
      DP = np.zeros((6, test_patients_count, 2))
      Y_test = []
      #ssc  -------------------   methode ----------
      def SSC(DP):
          FVP = []
          ID = np.array ([])
          HB = []
          epsilon = 0.00000001
          ID = []
          [n_round, n_test, n_class] = DP.shape
          p_x_c = np.zeros (1 * n_round)
          p_x_class = np.zeros (1 * n_class)

          for i in range (0, n_test):
              for j in range (0, n_class):

                   p_x_c = DP[:, i, j]
                   # print(p_x_c)

                   # check if any probability is 1 or 0
                   index = []

                   index = np.where (p_x_c == 0)
                   p_x_c[index] = p_x_c[index] + epsilon

                   index = np.where (p_x_c == 1)
                   p_x_c[index] = p_x_c[index] - epsilon

                   # calculate p_bar S N beta beta_hat(if filterflag is true) beta_out
                   # s_out and final voting probability
                   p_bar = p_x_c - 0.5
                   N = 0.5 - abs (p_bar)
                   for k in range (0, len (N)):
                      if (N[k] == 0):
                          N[k] = epsilon
                          p_bar[k] = p_bar[k] - np.sign (p_bar[k]) * epsilon

                   S = abs (p_bar)

                   beta = np.divide (S, N)
                   # if (filterflag == 1) :
                   #   beta = 1/(1+exp(-alpha*beta))-0.5

                   beta_out = sum (beta * p_bar, 0) / sum (beta * N, 0)
                   s_out = 0.5 * beta_out / (1 + np.sign (beta_out) * beta_out)
                   p_x_class[j:] = 0.5 + s_out
                   # print(p_x_class.shape)

              FVP.extend (p_x_class)

              #if (p_x_class [0] >= p_x_class [1]  ):
               #     val_max = p_x_class [0]
                #    ind_max = 0
              #else :
               #    val_max = p_x_class [1]
                #   ind_max = 1


              # print (FVP)
              val_max = p_x_class.max ()
              ind_max = np.where (p_x_class == val_max)

              ID.insert (i, ind_max[0])
              HB = np.concatenate (ID, axis=0)
              # print("Voici les IDs des classes %d" % ID[i])
              # print("Indice de la valeur max est: %d" % ind_max)
              # print("La valeur max est: %f"% val_max)

              return HB


      def prediction(Patient):


          #  X_array = list of features to be given to clssifiers
          # Y_array = list of target classes to be given to classifiers

          Y_test = []
          test_patients_count = 1
          DP = np.zeros((4, test_patients_count, 2))
          C = ClassificationDiab.SSC(DP)
          resultat = C[0]
          print (" le res", resultat)
          print (" D'apres SSC la prédiction pour que le patient est diabétique est :",bool(resultat))
          seed = 7
          kfold = model_selection.KFold(n_splits=10, random_state=seed)
          scoring = 'accuracy'


          return resultat


      def hasNumbers(inputString):
          return any(char.isdigit() for char in inputString)

#- --------------------------------------------------------------------------------------------------------------------------------------




      def get_classification_result(carca):

          print("Vecteur caractéristique:")
          print(carca)

          print ( "--------------------------------------------------")
          print(carca)
          carcat = []
          for key in carca:
              value = carca[key]
              carcat.append(value)

          print("Valeurs")
          print(carcat)
          test_patients_count = 1

          DP = np.zeros((6, test_patients_count, 2))
          boolean = 0
          start_time = time.time()


          print (" -------------loading ---------------------")
          DT = joblib.load('ArbreDeDecision')
          SVM = joblib.load('SVM_SVC')
          RN = joblib.load('ReseauxNeurones')
          NB = joblib.load('NaiveBayes')
          RF = joblib.load('RandomForest')
          KNN = joblib.load('KNN')




          #-------------------------------------- Test-----------------------------------
          x=0
          Y_test =[]
          #--------  classifieur 1  DT ------
          new_features_list =  []

          new_features_list.append (float (carcat[3]))
          new_features_list.append (float (carcat[6]))
          new_features_list.append (float (carcat[0]) * 100)
          new_features_list.append (float (carcat[5]))
          new_features_list.append (float (carcat[2]))
          if (carcat[1] == 'Homme'):
              new_features_list.append(0)
              k7 = 0

          else:
              new_features_list.append(1)
              k7 = 1
          new_features_list.append (int (carcat[4]) + 65)

          #for facteur in range(0,len (carcat)) :
          print (" ------ k ---------", carca)
          k1 = carcat[3]
          #new_features_list.append(k)
          k3 = carcat[0]
          k2 = carcat[6]
          k4 = carcat[5]
          k5 = carcat[2]
          k6 = carcat[4]


              #new_features_list = np.array(new_features_list).reshape(1, -1)

          print ("new_features_list", new_features_list)
          new_features_list = np.array(new_features_list).reshape(-1, 7)
          print ("new_features_list", new_features_list)

          proba_predicted_dt = DT.predict_proba(new_features_list)[0][0]
          DP[0][x][0] = proba_predicted_dt
          DP[0][x][1] = DT.predict_proba(new_features_list)[0][1]

          print (" this is prob", DT.predict_proba(new_features_list))

          proba_predicted_svm1 = SVM.predict_proba(new_features_list)[0][0]
          DP[1][x][0] = proba_predicted_svm1
          DP[1][x][1] = SVM.predict_proba(new_features_list)[0][1]

          proba_predicted_mlp1 = RN.predict_proba(new_features_list)[0][0]
          DP[2][x][0] = proba_predicted_mlp1
          DP[2][x][1] = RN.predict_proba(new_features_list)[0][1]

          proba_predicted_nb = NB.predict_proba(new_features_list)[0][0]
          DP[3][x][0] = proba_predicted_nb
          DP[3][x][1] = NB.predict_proba(new_features_list)[0][1]

          proba_predicted_rf = RF.predict_proba(new_features_list)[0][1]
          DP[4][x][0] = RF.predict_proba(new_features_list)[0][0]
          DP[4][x][1] = RF.predict_proba(new_features_list)[0][1]

          proba_predicted_knn = KNN.predict_proba(new_features_list)[0][1]
          DP[5][x][0] = KNN.predict_proba(new_features_list)[0][0]
          DP[5][x][1] = KNN.predict_proba(new_features_list)[0][1]








# --------------------------------- le résulatats de validation et evaluation -----------------------------------------------


#--------------------------- prediction


          acc_p = ClassificationDiab.prediction(carcat)
          print (" le patient est daibétique :  " ,acc_p)

          return (acc_p)
