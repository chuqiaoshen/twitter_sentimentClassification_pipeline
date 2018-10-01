
from lib_import import *

# load the model from disk
#predict_result_prob = loaded_model.predict_proba(vec_X)#this get:[negative, positive]
def GetPositiveProb(feature_name, file_name, df_X_processed,Logger):
    '''Given one text file, output its sentiemnt score based on our pretrained model
       feature_name: the model loaded
       file_name: the feature stored in the countervectorizer
       df_X_processed: the input text '''
    try:
        loaded_model = pickle.load(open(file_name, 'rb'))
    except Exception as e:
        print('failed model loading {}'.format(e))
        Logger.write('failed model loading {}'.format(e))
    try:
        transformer = TfidfTransformer()
        loaded_vec = CountVectorizer(decode_error="replace",vocabulary=pickle.load(open(feature_name , "rb")))
        tfidf_X = transformer.fit_transform(loaded_vec.fit_transform(df_X_processed))
        transformer = TfidfTransformer()
        vec_X = transformer.fit_transform(tfidf_X)
    except Exception as e:
        print('failed tfidf {}.format(e)')
        Logger.write('failed tfidf {}.format(e)')
    #y_pred = loaded_model.predict(df_X_processed)
    try:
        prob_arr = loaded_model.predict_proba(vec_X)
        prob_positive = np.hsplit(prob_arr, 2)[1]
    except Exception as e:
        print('failed model predict {}.format(e)')
        Logger.write('failed model predict {}.format(e)')
    return prob_positive,Logger
