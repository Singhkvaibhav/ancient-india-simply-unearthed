from engine.epkit import *
SPEC = dict(ep=42,
dig_q='Why did kings give away villages?', tags=['Type: copper plate', 'Era: about 600 to 1200 CE'], q_at='Why did kings',
dig="The brush clears a copper plate, covered in lines of text and ending with a royal seal. It records a king's gift of a village. Thousands of such plates survive. Why did kings give away villages?",
lit=['inscriptions', 'texts', "travellers' accounts"], lit_cues=['Copper-plate', 'Smriti', 'Hiuen Tsang'], notes={'inscriptions': 'Thousands of copper plates', 'texts': 'Law books', "travellers' accounts": 'Hiuen Tsang, Al-Biruni'},
sources="How do we know? Copper-plate grants survive in thousands. Smriti law books describe rights and duties. And travellers, such as Hiuen Tsang and Al-Biruni, describe villages and towns.",
frieze="From the Gupta age onward, kings gave land to Brahmins, temples and monks, and to officers. These were called land grants, and the grantees were often exempt from some taxes. "
"Grantees often gained rights over the village, such as collecting revenue, and sometimes justice. "
"A class of local lords, called samantas, grew up. They held land, kept soldiers, and gave loyalty to a king, in return for protection. "
"Many towns declined in this period, and coins were fewer. Trade did not stop, but it often moved to local markets, and temple towns. "
"Peasants grew crops on the land, and paid a share to the lord. Some were tied to the land. "
"Historians use these facts to ask whether early medieval India was feudal.",
scenes=[
 sc(None, 'Land grants', ar(-170, 'tablet', 'A copper-plate grant', 1.0), ar(190, 'sickle', 'A village', 1.0)),
 sc('Grantees often gained', 'Rights over a village', fg(-190, 'Grantee', col='basalt'), hs(130), hs(300, .8)),
 sc('A class of local lords', 'Samantas', fg(-190, 'King', crown=1), fg(40, 'Samanta', col='ochre'), ar(260, 'sword', None, .7)),
 sc('Many towns declined', 'Towns and trade', wl(-190, .8), ar(130, 'coin', 'Fewer coins', 1.0)),
 sc('Peasants grew crops', 'Peasants and lords', fg(-190, 'Peasant', col='clay'), ar(60, 'sickle', 'A share of the crop', .9), fg(260, 'Lord', col='ochre')),
 sc('Historians use these', 'A question for historians', ar(0, 'manuscript', 'Was it feudal?', 1.3)),
],
plaque_say="Scholars disagree. Was early medieval India feudal? One view, by R. S. Sharma, holds that land grants, local lords and falling trade created a feudal order, with peasants bound to the land. Another view holds that the picture is too simple. It argues that peasants stayed largely free, that trade and towns continued in many regions, and that European feudalism is not a good model.",
plaque=dict(kind='disagree', heading='Scholars disagree: Indian feudalism?', a=('A feudal order', 'Land grants, samantas and falling trade created lords and peasants tied to the land.'), b=('Not feudal', 'Peasants stayed largely free, trade and towns continued in many regions, and Europe is a poor model.'), cue_a='One view', cue_b='Another view'),
tip=['Grant, samanta, local market:', 'was it feudal? Two views.'], tip_close="Three terms and a question. Always give both sides in your answer.",
quiz=[('tablet', 'What was the gift of a village to a Brahmin often called?', 'a land grant'),
      ('sword', 'What were the local lords of this age called?', 'samantas'),
      ('manuscript', 'Which historian argued for Indian feudalism?', 'R. S. Sharma')],
mains='Was early medieval India feudal? Discuss both views.',
exhibit_say="The grant plate goes into its case. It records a gift of land, and a change of power.",
facts=['A copper-plate land grant', 'Samantas and tax-free villages', 'Feudalism: a debate between historians'],
)
build(SPEC, globals())
