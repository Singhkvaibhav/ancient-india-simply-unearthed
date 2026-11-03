from engine.epkit import *
SPEC = dict(ep=29,
dig_q='How can iron stay bright for 1,600 years?', tags=['Site: Mehrauli, Delhi', 'Era: about 375 to 415 CE'], q_at='How can iron',
dig="The brush clears a gold coin, stamped with a king in armour. It is a dinara of the Gupta age. Gold coins like this were issued in large numbers. The age of Chandragupta the Second is often called a golden age. How can iron stay bright for sixteen hundred years?",
lit=['coins', "travellers' accounts", 'inscriptions'], lit_cues=['Gold dinaras', 'Fa-Hien, a Chinese', 'The iron pillar at'], notes={'coins': 'Gold dinaras', "travellers' accounts": 'Fa-Hien', 'inscriptions': 'Mehrauli pillar'},
sources="How do we know? Gold dinaras of many kinds survive. Fa-Hien, a Chinese Buddhist monk, travelled in India for several years. The iron pillar at Mehrauli has an inscription naming a king Chandra.",
frieze="Chandragupta the Second ruled about 375 to 415 CE. He took the title Vikramaditya, the sun of valour. "
"He defeated the Shaka rulers of western India, and gained Malwa and Gujarat, with its ports. Ujjain became a second capital. "
"He made marriage alliances too. His daughter Prabhavati Gupta married a Vakataka king, and ruled as regent after his death. "
"Fa-Hien visited about 399 to 414 CE. He found the people prosperous and the roads safe, and he noted that punishments were mild. "
"Tradition says that nine scholars, the Navaratnas, adorned his court. Kalidasa is the most famous name. Scholars debate this tradition. "
"In Delhi, the Mehrauli iron pillar, which has not rusted, is linked to a king named Chandra, often identified with him.",
scenes=[
 sc(None, 'Vikramaditya', fg(-100, 'Chandragupta II', crown=1, col='ochre'), tx(-340, 'About 375 to 415 CE', 36, 200)),
 sc('He defeated the Shaka', 'Malwa and Gujarat', fg(-190, 'Chandragupta II', crown=1), ar(130, 'ship', 'Western ports', 1.0)),
 sc('He made marriage', 'Prabhavati Gupta', fg(-190, 'Prabhavati', col='ochre'), fg(110, 'Vakataka king', crown=1, col='basalt')),
 sc('Fa-Hien visited', 'Fa-Hien’s visit', fg(-130, 'Fa-Hien', col='clay'), tx(-340, 'Prosperous. Safe roads.', 36, 200)),
 sc('Tradition says', 'The Navaratnas', ar(-170, 'manuscript', 'Kalidasa', 1.0), tx(-330, 'Nine scholars, by tradition', 34, 150)),
 sc('In Delhi', 'Mehrauli iron pillar', ar(0, 'pillar', 'Rust-free iron', 1.3)),
],
plaque_say="Old name, new name. The Chinese monk, once written as Fa-Hien, is now usually spelled Faxian in modern Chinese romanisation. The name means Splendour of the Law. He left a record called A Record of Buddhist Kingdoms.",
plaque=dict(kind='rename', old='Fa-Hien', new='Faxian', cue_b='is now usually', sub='Chinese pilgrim, c. 400 CE'),
tip=['Vikramaditya: Malwa won,', 'Fa-Hien watched.'], tip_close="A title, a conquest and a witness. Those three are the core of Chandragupta the Second.",
quiz=[('coin', 'Name the Gupta gold coin.', 'the dinara'),
      ('pillar', 'Where in Delhi stands the famous iron pillar?', 'Mehrauli'),
      ('manuscript', 'Which Chinese monk visited in his time?', 'Fa-Hien')],
mains='Why is the age of the Guptas called a golden age? Is it justified?',
exhibit_say="The gold coin goes into its case. It is a dinara of the Gupta age.",
facts=['Gupta gold dinara', 'Of Chandragupta II, about 375 to 415 CE', 'Fa-Hien visited in his reign'],
)
build(SPEC, globals())
