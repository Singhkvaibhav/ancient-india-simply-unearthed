from engine.epkit import *
SPEC = dict(ep=31,
dig_q='Who first said that the Earth turns?', tags=['Text: Aryabhatiya', 'Date: 499 CE'], q_at='Who first said',
dig="The brush clears a ring of metal, an armillary sphere, a model of the heavens. Astronomers of the Gupta age used instruments like this. One of them, Aryabhata, wrote that the Earth turns on its axis. Who first said that the Earth turns?",
lit=['texts', 'inscriptions'], lit_cues=['Aryabhatiya', 'Inscriptions'], notes={'texts': 'Aryabhatiya, Kalidasa', 'inscriptions': 'Court records'},
sources="How do we know? From the texts themselves. The Aryabhatiya was composed in 499 CE. Plays and poems of Kalidasa survive. Inscriptions record the patronage of Gupta kings.",
frieze="Aryabhata, born in 476 CE, wrote the Aryabhatiya in 499 CE. He used place value and gave a good value of pi, about three point one four one six. He explained eclipses as shadows, not as demons, and he wrote that the Earth rotates on its axis. "
"Varahamihira wrote the Panchasiddhantika and the Brihat Samhita, on astronomy, weather and many other topics. "
"The decimal system, with a symbol for zero, was in use. Arab scholars later carried it west, and it became known as the Hindu-Arabic numerals. "
"In medicine, the Charaka Samhita and Sushruta Samhita were in use. Vagbhata compiled later work. "
"The age was also great in letters. Kalidasa wrote the play Abhijnanashakuntalam, and poems like the Meghaduta and Raghuvamsha. "
"The Panchatantra, a book of fables, and the Amarakosha, a word list, also belong here.",
scenes=[
 sc(None, 'Aryabhata, 476 CE', fg(-190, 'Aryabhata', col='basalt'), ar(130, 'sphere', 'The Earth rotates', 1.0), tx(-360, 'Place value · Pi ≈ 3.1416', 34, 300)),
 sc('Varahamihira wrote', 'Varahamihira', fg(-130, 'Varahamihira', col='clay'), ar(180, 'manuscript', 'Brihat Samhita', 1.0)),
 sc('The decimal system', 'Zero and place value', tx(-300, '0 1 2 3 4 5 6 7 8 9', 60, 0), tx(-220, 'Later: Hindu-Arabic numerals', 34, 0)),
 sc('In medicine', 'Medicine', ar(-170, 'manuscript', 'Charaka Samhita', 1.0), ar(190, 'manuscript', 'Sushruta Samhita', 1.0)),
 sc('The age was also', 'Kalidasa', fg(-130, 'Kalidasa', col='ochre'), ar(180, 'palmleaf', 'Shakuntalam', 1.0)),
 sc('The Panchatantra', 'Fables and words', ar(-170, 'manuscript', 'Panchatantra', 1.0), ar(190, 'manuscript', 'Amarakosha', 1.0)),
],
plaque_say="Old name, new name. The numerals we use are often called Arabic numerals. A better name is Hindu-Arabic numerals, because the system began in India, and Arab scholars carried it west.",
plaque=dict(kind='rename', old='Arabic numerals', new='Hindu-Arabic numerals', cue_b='A better name', sub='Born in India, carried west'),
tip=['Aryabhata: zero, pi, Earth spins;', 'Kalidasa: Shakuntalam.'], tip_close="One scientist, one poet. Each with two works you can name.",
quiz=[('sphere', 'Who wrote the Aryabhatiya?', 'Aryabhata'),
      ('manuscript', 'Which play did Kalidasa write about a forest-born heroine?', 'Abhijnanashakuntalam'),
      ('palmleaf', 'Which book of fables belongs to the Gupta age?', 'the Panchatantra')],
mains='Discuss the achievements of the Gupta age in science and literature.',
exhibit_say="The armillary sphere goes into its case. It models the sky as the Gupta astronomers saw it.",
facts=['A ring model of the heavens', 'Aryabhata wrote in 499 CE', 'Zero and place value in use'],
)
build(SPEC, globals())
