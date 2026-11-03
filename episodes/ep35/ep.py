from engine.epkit import *
SPEC = dict(ep=35,
dig_q='Why carve a temple out of one rock?', tags=['Site: Mamallapuram', 'Era: 7th to 8th century CE'], q_at='Why carve',
dig="The brush clears a stone boat, with a tall mast. It stands for the port of Mamallapuram, where Pallava kings carved temples out of single rocks, beside the sea. Why carve a temple out of one rock?",
lit=['inscriptions', 'dug up', 'texts'], lit_cues=['Pallava copper', 'Archaeologists dug', 'The Tamil hymns'], notes={'inscriptions': 'Copper plates, Aihole', 'dug up': 'Mamallapuram', 'texts': 'Tamil bhakti hymns'},
sources="How do we know? Pallava copper plates and stone inscriptions give lists of kings. Archaeologists dug up the port at Mamallapuram. The Tamil hymns of the Nayanars and Alvars describe the age.",
frieze="The Pallavas ruled from Kanchipuram, about the sixth to the ninth century CE. Simhavishnu, about 575 CE, defeated the Kalabhras and began the great age. "
"His son Mahendravarman the First was a patron of rock-cut temples, and wrote a comic play, the Mattavilasa Prahasana. "
"Narasimhavarman the First, called Mamalla, defeated the Chalukya king Pulakeshin the Second, and took his capital, Vatapi, in 642 CE. He founded Mamallapuram. "
"There, the Pancha Rathas are five temples carved from single rocks, with chariot-like shapes. The Shore Temple, built by Rajasimha, is a structural temple of stone blocks, beside the sea. "
"At Kanchipuram, Rajasimha built the Kailasanatha temple. "
"In these centuries, the bhakti poets, the Nayanars and Alvars, sang in Tamil. Their songs carried devotion to the people.",
scenes=[
 sc(None, 'Kanchipuram, 6th century CE', fg(-130, 'Simhavishnu', crown=1), tx(-340, 'The Kalabhras defeated', 36, 200)),
 sc('His son Mahendravarman', 'Mahendravarman I', fg(-130, 'Mahendravarman', crown=1), ar(190, 'shelter', 'Rock-cut shrines', 1.0)),
 sc('Narasimhavarman the First', 'Mamalla takes Vatapi, 642 CE', fg(-190, 'Narasimhavarman', crown=1), ar(160, 'wall', 'Vatapi', .9)),
 sc('There, the Pancha Rathas', 'Pancha Rathas', ar(-250, 'temple', None, .8), ar(-80, 'temple', None, .8), ar(90, 'temple', None, .8), ar(260, 'temple', None, .8), tx(-380, 'Five temples, five rocks', 34, 0)),
 sc('At Kanchipuram', 'Shore Temple, Kailasanatha', ar(-170, 'ship', 'Shore Temple', 1.0), ar(190, 'temple', 'Kailasanatha', 1.1)),
 sc('In these centuries', 'The bhakti poets', fg(-130, 'Nayanar', col='clay'), fg(110, 'Alvar', col='ochre'), tx(-340, 'Songs in Tamil', 36, 220)),
],
plaque_say="Old name, new name. The Pallava port is called Mamallapuram, after Mamalla, the title of Narasimhavarman. The modern name of the town is Mahabalipuram, and both names are in use.",
plaque=dict(kind='rename', old='Mamallapuram', new='Mahabalipuram', cue_b='The modern name', sub='A Pallava port, 7th century'),
tip=['Pallava: rathas, Shore Temple,', 'Kanchi, Mamalla.'], tip_close="Remember the rock-cut chariots and the Shore Temple, and name Mamalla as the founder.",
quiz=[('ship', 'Which seaside temple was built by Rajasimha?', 'the Shore Temple'),
      ('temple', 'How many rathas stand at Mamallapuram?', 'five'),
      ('wall', 'Name the Pallava capital.', 'Kanchipuram')],
mains='Discuss the contribution of the Pallavas to art and architecture.',
exhibit_say="The boat goes into its case. It recalls the port beside the Shore Temple.",
facts=['A boat of the Pallava port', 'Mamallapuram, 7th century CE', 'Rock-cut rathas and a Shore Temple'],
)
build(SPEC, globals())
