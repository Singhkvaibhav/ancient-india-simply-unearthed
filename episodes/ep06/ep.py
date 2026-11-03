from engine.epkit import *
SPEC = dict(ep=6,
dig_q='Why did the great cities fade away?', tags=['Site: Harappa', 'Age: about 3,900 years'], q_at='Why did',
dig="The brush reveals a set of cubic stone weights. In the early layers they are neat and standard. In the later layers they are gone. The cities that once used them were fading. Why did the great cities fade away?",
lit=['dug up'], lit_cues=['Archaeologists dug'], notes={'dug up': 'Late layers, river beds'},
sources="How do we know? We read the soil. Archaeologists dug up late layers at Harappa and other sites, and study old river beds and climate. The script is still unread, so no document tells us why.",
frieze="Around nineteen hundred BCE, the mature cities declined. This is called the Late Harappan phase. "
"Town planning weakened. The drains were not kept up. Standard weights and the script go out of use. Long trade routes shrink. "
"People did not vanish. Many moved east, toward the Ganga and Yamuna plains, and south into Gujarat and Maharashtra. Villages replaced cities. "
"At Harappa, a later cemetery, called Cemetery H, shows new burial customs. "
"Rivers matter in this story. The Ghaggar-Hakra river system seems to have dried up in parts. The Indus is also known to shift its course. "
"In 1944, the archaeologist Mortimer Wheeler suggested that invaders destroyed the cities. Most scholars today find that evidence weak. "
"The question is still open, and historians keep testing each idea against new finds.",
scenes=[
 sc(None, 'Around 1900 BCE', ar(0, 'scales', 'Late Harappan', 1.3), tx(-380, 'The mature cities decline', 40)),
 sc('Town planning weakened', 'Neglected cities', hs(-250), hs(-60), hs(130), tx(-330, 'Drains. Weights. Script. Fading.', 34)),
 sc('People did not vanish', 'Moving east and south', fg(-220, 'Villager'), fg(10, 'Villager', col='clay'), fg(230, 'Villager', col='basalt'), tx(-360, 'To the Ganga plains and Gujarat', 36)),
 sc('At Harappa', 'Cemetery H', ar(0, 'pot', 'Burial urn', 1.2), tx(-380, 'New burial customs', 38)),
 sc('Rivers matter', 'Rivers shift and dry', rv(800, -20), rv(800, 40), tx(-350, 'Ghaggar-Hakra  ·  Indus', 38)),
 sc('In 1944', 'Wheeler\'s idea, 1944', fg(-200, 'M. Wheeler', col='basalt'), tx(-300, 'Invasion? Most now doubt it', 34, 160), tr(400)),
],
plaque_say="Scholars disagree. Why did the cities decline? One view stresses the environment: changing climate, drying rivers and floods. Another view stresses society: the end of long-distance trade and the breakdown of city life. Many scholars combine the two.",
plaque=dict(kind='disagree', heading='Scholars disagree', a=('Environment', 'Drying rivers, a changing climate and floods made the great cities hard to sustain.'), b=('Society and trade', 'Trade networks weakened, and city institutions broke down, so people moved to villages.'), cue_a='One view', cue_b='Another view'),
tip=['Rivers, trade, no invaders:', 'cities became villages.'], tip_close="Remember rivers, trade and movement. Do not blame a single cause in your answer.",
quiz=[('scales', 'Name these standard cubes that disappear in the Late Harappan phase.', 'weights'),
      ('pot', 'Which later cemetery at Harappa shows new burial customs?', 'Cemetery H'),
      ('ship', 'Which archaeologist suggested in 1944 that invaders destroyed the cities?', 'Mortimer Wheeler')],
mains='Critically examine the causes of the decline of the Harappan civilisation.',
exhibit_say="The chert weights go into their case. They once helped to keep trade fair.",
facts=['Cubes of chert, in neat ratios', 'Standard weights fade after 1900 BCE', 'No single cause is accepted'],
)
build(SPEC, globals())
