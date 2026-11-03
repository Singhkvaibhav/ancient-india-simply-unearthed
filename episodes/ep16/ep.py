from engine.epkit import *
SPEC = dict(ep=16,
dig_q='What did a wooden city leave behind?', tags=['Site: Kumrahar, Patna', 'Era: about 300 BCE'], q_at='What did a wooden',
dig="The brush clears the stone gate of a fort, with a wall of heavy timber beside it. Greek visitors described Pataliputra as a great city walled in wood. Archaeologists later found the wooden posts in the soil. What did a wooden city leave behind?",
lit=['dug up', 'texts', "travellers' accounts"], lit_cues=['Archaeologists dug', 'The Arthashastra', 'Megasthenes'], notes={'dug up': 'Kumrahar, wooden palisade', 'texts': 'Arthashastra', "travellers' accounts": 'Megasthenes: Indika'},
sources="How do we know? Archaeologists dug up the Mauryan palace site at Kumrahar. The Arthashastra, a book on statecraft, is linked with Kautilya. Megasthenes, a Greek envoy, wrote an account called Indika, now known only in quotations.",
frieze="The Maurya empire was founded by Chandragupta Maurya. By tradition he was helped by Kautilya, also called Chanakya. About 321 BCE, they overthrew the Nandas, and took Pataliputra. "
"Chandragupta then turned to the north-west, which Alexander had left in disorder. About 305 BCE, he faced Seleucus Nicator, the Greek ruler in the east. "
"They made peace. Seleucus gave up lands in the west, in Afghanistan and Baluchistan. In return, Chandragupta gave him five hundred elephants. "
"Seleucus sent an envoy, Megasthenes, to Pataliputra. He wrote that the city was guarded by a wooden wall with five hundred and seventy towers and sixty-four gates. "
"Chandragupta ruled until about 297 BCE. Jain tradition says that he gave up his throne, and went south to Shravanabelagola. "
"His son Bindusara carried on the work. By then the empire stretched from the Himalayas deep into the south.",
scenes=[
 sc(None, 'The Mauryan founder', fg(-190, 'Chandragupta', crown=1), fg(110, 'Kautilya', col='basalt'), ar(340, 'throne', None, .6)),
 sc('Chandragupta then turned', 'The north-west', fg(-100, 'Chandragupta', crown=1), tx(-340, 'About 305 BCE', 40, 0), hl(300, .9)),
 sc('They made peace', 'Peace with Seleucus', ar(-190, 'helmet', 'Seleucus', 1.0), ar(200, 'elephant', '500 elephants', 1.0)),
 sc('Seleucus sent an envoy', 'Megasthenes at Pataliputra', fg(-190, 'Megasthenes', col='clay'), wl(110, 1.0), tx(-380, '64 gates · 570 towers', 36, 160)),
 sc('Chandragupta ruled until', 'Abdication, by tradition', ar(0, 'throne', 'Left behind', 1.0), tx(-380, 'Shravanabelagola', 40, 0)),
 sc('His son Bindusara', 'Bindusara', fg(-100, 'Bindusara', crown=1), tx(-340, 'From Himalayas to the Deccan', 34, 200)),
],
plaque_say="Old name, new name. Greek writers called Chandragupta Sandrocottus. In 1793, Sir William Jones noticed that the Greek name matched Chandragupta. That link helped to fix the dates of early Indian history.",
plaque=dict(kind='rename', old='Sandrocottus (Greek)', new='Chandragupta', cue_b='In 1793', sub='The link fixes Indian dates'),
tip=['Nanda fall, Seleucus peace,', 'Megasthenes, wooden walls.'], tip_close="Four facts in the order they happened. They carry the entire reign of Chandragupta.",
quiz=[('fort', 'Name the capital of the Mauryan empire.', 'Pataliputra'),
      ('helmet', 'Which Greek ruler did Chandragupta make peace with?', 'Seleucus Nicator'),
      ('manuscript', 'Name the Greek envoy who wrote Indika.', 'Megasthenes')],
mains='Evaluate the sources for the study of the Mauryan empire.',
exhibit_say="The fort goes into its case. Pataliputra was walled in wood and ruled an empire.",
facts=['A gate of Pataliputra, the capital', 'Chandragupta ruled until about 297 BCE', 'Megasthenes wrote Indika'],
)
build(SPEC, globals())
