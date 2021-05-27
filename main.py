from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

def havaDurumuGetir():
    return ['Gunesli', 'Gunesli', 'Gunesli', 'Gunesli', 'Gunesli', 'Gunesli',
            'Yagmurlu', 'Yagmurlu', 'Yagmurlu', 'Yagmurlu', 'Yagmurlu', 'Yagmurlu',
            'Karlı', 'Karlı', 'Karlı', 'Karlı', 'Karlı', 'Karlı']

def haftaninDurumunuGetir():
    return ['haftaIci', 'haftaIci', 'haftaIci',
            'haftaSonu', 'haftaSonu', 'haftaSonu',
            'haftaIci', 'haftaIci', 'haftaIci',
            'haftaSonu', 'haftaSonu', 'haftaSonu',
            'haftaIci', 'haftaIci', 'haftaIci',
            'haftaSonu', 'haftaSonu', 'haftaSonu']

def gununDurumunuGetir():
    return ['Sabah', 'Ogle', 'Aksam',
            'Sabah', 'Ogle', 'Aksam',
            'Sabah', 'Ogle', 'Aksam',
            'Sabah', 'Ogle', 'Aksam',
            'Sabah', 'Ogle', 'Aksam',
            'Sabah', 'Ogle', 'Aksam',
            ]

def trafikDurumunuGetir():
    return ['Evet', 'Hayır', 'Evet',
            'Hayır', 'Hayır', 'Hayır',
            'Yes', 'Evet', 'Evet',
            'Hayır', 'Hayır', 'Hayır',
            'Evet', 'Evet', 'Evet',
            'Evet', 'Hayır', 'Evet'
            ]




havaDurumu = ['Gunesli', 'Gunesli', 'Gunesli', 'Gunesli', 'Gunesli', 'Gunesli',
            'Yagmurlu', 'Yagmurlu', 'Yagmurlu', 'Yagmurlu', 'Yagmurlu', 'Yagmurlu',
            'Karlı', 'Karlı', 'Karlı', 'Karlı', 'Karlı', 'Karlı']
labelEncoder = preprocessing.LabelEncoder();
print(labelEncoder.fit_transform(havaDurumu))

trafikDurumu = ['Evet', 'Hayır', 'Evet',
            'Hayır', 'Hayır', 'Hayır',
            'Yes', 'Evet', 'Evet',
            'Hayır', 'Hayır', 'Hayır',
            'Evet', 'Evet', 'Evet',
            'Evet', 'Hayır', 'Evet'
              ]
print(labelEncoder.fit_transform(trafikDurumu))
havaDurumu = havaDurumuGetir()
haftaninZamani = haftaninDurumunuGetir()
gununZamani = gununDurumunuGetir()
trafikDurumu = trafikDurumunuGetir()

labelEncoder = preprocessing.LabelEncoder()


kodlanmisHavaDurumu = labelEncoder.fit_transform(havaDurumu)
kodlanmisHaftaninDurumu = labelEncoder.fit_transform(haftaninZamani)
kodlanmisGununDurumu = labelEncoder.fit_transform(gununZamani)
kodlanmisTrafikDurumu = labelEncoder.fit_transform(trafikDurumu)


features = []
for i in range(len(kodlanmisHavaDurumu)):
        features.append([kodlanmisHavaDurumu[i], kodlanmisHaftaninDurumu[i], kodlanmisGununDurumu[i]])

model = GaussianNB()


model.fit(features, kodlanmisTrafikDurumu)

print(model.predict([[2, 1, 2]]))






