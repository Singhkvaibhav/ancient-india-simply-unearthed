from engine.epkit import *
SPEC = dict(ep=41,
dig_q='Why do coins from far away turn up in an Indian field?', tags=['Era: about 711 to 1200 CE', 'Silver dirham'], q_at='Why do coins',
dig="The brush clears a silver coin, with lines of Arabic script. It was struck far from India, yet it is found here. From the eighth century, people, goods and ideas came to the subcontinent from the west, by sea and by the passes. Why do coins from far away turn up in an Indian field?",
lit=['coins', 'texts', "travellers' accounts"], lit_cues=['Arab and Ghaznavid', 'The Chachnama', 'Al-Biruni'], notes={'coins': 'Arab and Ghaznavid', 'texts': 'Chachnama', "travellers' accounts": 'Al-Biruni'},
sources="How do we know? Arab and Ghaznavid coins survive. The Chachnama, a Persian text, tells the story of Sind. And Al-Biruni, a scholar, wrote a detailed book on India. Each source has its own point of view, so historians compare them.",
frieze="In 711 to 712 CE, an Arab army led by Muhammad bin Qasim entered Sind. Dahir, its ruler, was defeated. Arab rule stayed in Sind and Multan, and did not extend far. "
"Arab merchants had long traded along the west coast, and settled in places such as Kerala and Gujarat. "
"In the early eleventh century, Mahmud of Ghazni raided northern India many times, between 997 and 1030. The best-known raid was on Somnath, in 1025. His aim was wealth as well as power. "
"With Mahmud came Al-Biruni, a scholar who learnt Sanskrit. His book, the Kitab-ul-Hind, describes Indian science, religion, society and customs, with fairness. "
"In 1191, Prithviraj the Third defeated Muhammad of Ghor at Tarain. In 1192, Ghor won the second battle at Tarain. "
"This opened the way for new rule in north India. Contact also meant new ideas, and the exchange of knowledge between India and the Arab world.",
scenes=[
 sc(None, 'Sind, 711 to 712 CE', fg(-190, 'Muhammad bin Qasim', col='basalt'), fg(100, 'Dahir', crown=1, col='terra')),
 sc('Arab merchants had', 'Arab traders', ar(-130, 'ship', 'West-coast trade', 1.2), fg(190, 'Merchant', col='clay')),
 sc('In the early eleventh', 'Mahmud of Ghazni', fg(-130, 'Mahmud', crown=1, col='basalt'), tx(-340, '17 raids, 997 to 1030', 36, 200)),
 sc('With Mahmud came', 'Al-Biruni', fg(-130, 'Al-Biruni', col='clay'), ar(180, 'manuscript', 'Kitab-ul-Hind', 1.1)),
 sc('In 1191', 'Tarain, 1191 and 1192', fg(-190, 'Prithviraj III', crown=1), fg(150, 'Muhammad of Ghor', crown=1, col='basalt')),
 sc('This opened the way', 'Exchange of ideas', ar(-130, 'manuscript', 'Sanskrit and Arabic', 1.0), ar(180, 'coin', None, 1.0)),
],
plaque_say="Scholars disagree. How should we read these events? One view relies on the chroniclers of the time, who often described them in religious terms. Another view, held by many modern historians, stresses wealth, politics and trade as motives, and also the exchange of ideas. Most scholars treat the sources with care, since they were written by people on one side or the other.",
plaque=dict(kind='disagree', heading='Scholars disagree: reading the sources', a=('The chroniclers', 'Court chroniclers of the time often framed raids and wars in religious terms.'), b=('Modern historians', 'Many stress wealth, politics, trade and exchange of ideas as motives and results.'), cue_a='One view', cue_b='Another view'),
tip=['711 Sind, 1025 Somnath,', '1192 Tarain.'], tip_close="Three dates in a row. Add Al-Biruni's book for the cultural side.",
quiz=[('coin', 'Who led the Arab army into Sind in 711?', 'Muhammad bin Qasim'),
      ('manuscript', 'Who wrote the Kitab-ul-Hind?', 'Al-Biruni'),
      ('ship', 'Where did Prithviraj and Muhammad of Ghor fight in 1191?', 'Tarain')],
mains='Evaluate the impact of Arab and Turkish contacts before 1200 CE.',
exhibit_say="The silver coin goes into its case. It is a small trace of a long contact.",
facts=['Silver dirham with Arabic script', 'Arabs reached Sind in 711 to 712 CE', 'Al-Biruni wrote on India in about 1030 CE'],
)
build(SPEC, globals())
