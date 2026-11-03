from engine.epkit import *
SPEC = dict(ep=36,
dig_q='What did an elephant stand for in a king’s army?', tags=['Dynasty: Chalukya of Badami', 'Era: 543 to 753 CE'], q_at='What did an',
dig="The brush clears a carved elephant, large and steady. Elephants carried kings into battle, and carried honour into stone. The Chalukyas of Badami left many of them in their temples. What did an elephant stand for in a king's army?",
lit=['inscriptions', 'dug up'], lit_cues=['The Aihole', 'Archaeologists dug'], notes={'inscriptions': 'Aihole, by Ravikirti', 'dug up': 'Aihole, Badami, Pattadakal'},
sources="How do we know? The Aihole inscription, composed by the poet Ravikirti in 634 CE, praises Pulakeshin the Second. Archaeologists dug up and recorded the temples at Aihole, Badami and Pattadakal.",
frieze="The Chalukyas of Badami rose in Karnataka. Pulakeshin the First, about 543 CE, made Vatapi, now Badami, his capital. "
"Pulakeshin the Second was the greatest king, ruling from about 610 to 642 CE. He defeated Harsha on the Narmada, and added much of the Deccan. "
"The Aihole inscription of 634 CE, by the poet Ravikirti, praises his victories. "
"In 642 CE, the Pallava king Narasimhavarman defeated him and entered Vatapi. "
"Vikramaditya the First restored Chalukya power. The dynasty lasted until about 753 CE, when it fell to the Rashtrakutas. "
"The Chalukyas were great builders. At Aihole, there are the Durga and Ladkhan temples. At Badami, there are rock-cut cave temples. At Pattadakal, the Virupaksha and Sangameshvara temples show a blend of northern and southern styles.",
scenes=[
 sc(None, 'Pulakeshin I, 543 CE', fg(-130, 'Pulakeshin I', crown=1), ar(190, 'wall', 'Vatapi', 1.0)),
 sc('Pulakeshin the Second', 'Pulakeshin II, 610 to 642 CE', fg(-190, 'Pulakeshin II', crown=1), fg(120, 'Harsha', crown=1, col='basalt')),
 sc('The Aihole inscription', 'The Aihole inscription', fg(-130, 'Ravikirti', col='clay'), ar(170, 'tablet', '634 CE', 1.1)),
 sc('In 642 CE', 'The Pallava reply', fg(-190, 'Narasimhavarman', crown=1, col='terra'), ar(160, 'wall', 'Vatapi falls', .9)),
 sc('Vikramaditya the First', 'Restoration and end', fg(-130, 'Vikramaditya I', crown=1), tx(-330, 'Fell to the Rashtrakutas, 753 CE', 34, 120)),
 sc('The Chalukyas were', 'Builders', ar(-250, 'temple', 'Aihole', .9), ar(-30, 'shelter', 'Badami', .9), ar(210, 'temple', 'Pattadakal', .9)),
],
plaque_say="Old name, new name. The Chalukya capital was called Vatapi in inscriptions. Today the town is called Badami, in Karnataka. It lies in a valley of red sandstone hills, and is famed for its cave temples.",
plaque=dict(kind='rename', old='Vatapi', new='Badami', cue_b='Today the town', sub='Capital of the early Chalukyas'),
tip=['Vatapi, Pulakeshin II, Aihole,', 'Pattadakal.'], tip_close="A capital, a king, an inscription and a temple town. Four anchors for the Chalukyas.",
quiz=[('elephant', 'Who composed the Aihole inscription?', 'Ravikirti'),
      ('wall', 'What is Vatapi called today?', 'Badami'),
      ('temple', 'At which site do the Virupaksha and Sangameshvara temples stand?', 'Pattadakal')],
mains='Assess the role of the Chalukyas of Badami in Deccan history.',
exhibit_say="The elephant goes into its case. It stands for the power of the early Deccan kings.",
facts=['A carved elephant of the Deccan', 'Chalukyas of Badami, 543 to 753 CE', 'Builders at Aihole and Pattadakal'],
)
build(SPEC, globals())
