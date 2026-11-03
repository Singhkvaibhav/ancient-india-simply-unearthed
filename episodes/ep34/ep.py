from engine.epkit import *
SPEC = dict(ep=34,
dig_q='Why would a king give away everything every five years?', tags=['Site: Kannauj', 'Era: 606 to 647 CE'], q_at='Why would a king',
dig="The brush clears a wheel carved with spokes, the wheel of dharma. It stands for a faith that a king, Harsha, supported with all his wealth. Every five years, he is said to have given away everything but his clothes. Why would a king give away everything every five years?",
lit=['texts', "travellers' accounts", 'inscriptions'], lit_cues=['The Harshacharita', 'Hiuen Tsang', 'And inscriptions'], notes={'texts': 'Harshacharita, Harsha’s plays', "travellers' accounts": 'Hiuen Tsang', 'inscriptions': 'Banskhera, Aihole'},
sources="How do we know? The Harshacharita was written by Bana, Harsha's court poet. Hiuen Tsang, a Chinese monk, travelled in India for fourteen years. And inscriptions, such as the Banskhera plate and the Aihole inscription, give more.",
frieze="Harshavardhana was born into the Pushyabhuti family of Thanesar. His brother Rajyavardhana was killed by Shashanka of Gauda. Harsha became king in 606 CE, at sixteen. "
"He made Kannauj his capital, and united much of north India. He then moved against the south, but was defeated by the Chalukya king Pulakeshin the Second on the Narmada, about 618 CE. "
"Hiuen Tsang visited his court, and stayed at Nalanda. He describes a great assembly at Kannauj, and a gathering at Prayag, held every five years, where Harsha gave away his wealth. "
"Harsha was also a writer. He is credited with three plays: Ratnavali, Priyadarshika and Nagananda. "
"His state was less centralised than the Mauryas, and relied on feudatories. Officers were often paid with land. "
"Harsha died in 647 CE without an heir, and his empire broke up.",
scenes=[
 sc(None, 'Thanesar, 606 CE', fg(-190, 'Rajyavardhana', crown=1, col='basalt'), fg(90, 'Harsha', crown=1), fg(300, 'Shashanka', col='clay')),
 sc('He made Kannauj', 'Kannauj and the Narmada', wl(-190, 1.0), rv(400, 60), fg(280, 'Pulakeshin II', crown=1, col='ochre')),
 sc('Hiuen Tsang visited', 'Hiuen Tsang and Nalanda', fg(-130, 'Hiuen Tsang', col='clay'), ar(180, 'wheel', 'Nalanda', 1.1)),
 sc('Harsha was also', 'A writer-king', ar(-190, 'manuscript', 'Ratnavali', 1.0), ar(40, 'manuscript', 'Priyadarshika', 1.0), ar(250, 'manuscript', 'Nagananda', 1.0)),
 sc('His state was', 'A feudal state', fg(-190, 'Harsha', crown=1), fg(40, 'Feudatory', col='basalt'), fg(240, 'Feudatory', col='ochre')),
 sc('Harsha died in', 'About 647 CE', ar(0, 'throne', 'No heir', 1.2)),
],
plaque_say="Old name, new name. The Chinese pilgrim is now written Xuanzang in modern romanisation. Older books spell him Hiuen Tsang, or Hsuan-tsang. He walked to India, studied at Nalanda, and returned with hundreds of Buddhist texts.",
plaque=dict(kind='rename', old='Hiuen Tsang', new='Xuanzang', cue_b='Older books', sub='Chinese pilgrim, 7th century CE'),
tip=['606 to 647, Kannauj capital,', 'Hiuen Tsang watched.'], tip_close="Two dates, one capital and a witness. Add the defeat on the Narmada, and you have full marks.",
quiz=[('wheel', 'Who was Harsha’s court poet and biographer?', 'Bana'),
      ('sword', 'Which Chalukya king defeated Harsha?', 'Pulakeshin the Second'),
      ('wall', 'Name the capital of Harsha.', 'Kannauj')],
mains='Evaluate Harsha’s achievements and the accounts of Hiuen Tsang.',
exhibit_say="The wheel goes into its case. It is a symbol of the teaching that Harsha supported.",
facts=['A wheel, the symbol of dharma', 'Harsha ruled from 606 to 647 CE', 'Hiuen Tsang visited his court'],
)
build(SPEC, globals())
