import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore




####################   READING FROM  FIRE BASE

db = firestore.client()






#################### writing on the data base 



doc_ref = db.collection(u'user').document(u'hossary').collection(u'chat').document(u'bot')
        doc_ref.update({
                        u'text': 'How Are You Doing , bezo ??'

        })