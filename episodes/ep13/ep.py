from engine.epkit import *
SPEC = dict(ep=13,
dig_q='Why build a mound over a relic?', tags=['Site: Sanchi', 'Age: over 2,000 years'], q_at='Why build a mound',
dig="The brush clears a half-round mound of stone, topped by a small square railing and an umbrella. It is a stupa, a monument that holds a relic, a small piece of what remained after cremation. Why build a mound over a relic?",
lit=['texts', 'dug up', 'inscriptions'], lit_cues=['Buddhist texts', 'Archaeologists dug', 'Inscriptions'], notes={'texts': 'Pali and Sanskrit', 'dug up': 'Sanchi, Bharhut', 'inscriptions': 'Donor records'},
sources="How do we know? Buddhist texts record the councils. Archaeologists dug up stupas at Sanchi, Bharhut and Amaravati. Inscriptions on the railings name the donors who paid for them.",
frieze="After the death of the Buddha, the teachings needed to be kept. Four councils met. "
"The first, at Rajagriha, was about 483 BCE, under Ajatashatru. Upali recited the rules of the order, and Ananda recited the teachings. "
"The second, at Vaishali, was about a century later, and ended with a split in the order. "
"The third was at Pataliputra, under Ashoka, led by Moggaliputta Tissa. After it, missions were sent out, including to Sri Lanka. "
"The fourth was in Kashmir, under Kanishka. Here the Mahayana branch took shape, with texts in Sanskrit. "
"The teachings were collected in three baskets, the Tripitaka: Vinaya, Sutta and Abhidhamma. "
"Stupas spread, with carved gateways and railings at Sanchi, Bharhut and Amaravati. Monks also lived in viharas, and prayed in chaitya halls.",
scenes=[
 sc(None, 'Four councils', tx(-380, 'Rajagriha · Vaishali', 42, 0), tx(-310, 'Pataliputra · Kashmir', 42, 0), ar(0, 'stupa', None, .9)),
 sc('The first, at Rajagriha', 'Rajagriha, about 483 BCE', fg(-210, 'Ananda', col='clay'), fg(60, 'Upali', col='basalt'), fg(260, 'Ajatashatru', crown=1)),
 sc('The second, at Vaishali', 'Vaishali: a split', fg(-120, 'Elder', col='clay'), fg(120, 'Elder', col='basalt'), tx(-340, 'The order divides', 38, 0)),
 sc('The third was', 'Pataliputra: missions', fg(-170, 'Ashoka', crown=1), ar(130, 'ship', 'To Sri Lanka', 1.1)),
 sc('The fourth was', 'Kashmir: Mahayana', fg(-170, 'Kanishka', crown=1), ar(150, 'manuscript', 'Sanskrit texts', 1.0)),
 sc('The teachings were', 'Tripitaka and stupas', ar(-170, 'palmleaf', 'Three baskets', 1.0), ar(150, 'stupa', 'Sanchi', 1.2), ar(380, 'gate', None, .6)),
],
plaque_say="Old name, new name. The older branch of Buddhism is often called Hinayana, the lesser vehicle. That is a name used by its critics, and many now consider it unfair. The name Theravada, the way of the elders, is preferred today.",
plaque=dict(kind='rename', old='Hinayana', new='Theravada', cue_b='The name Theravada', sub='Theravada = the way of the elders'),
tip=['Rajagriha, Vaishali, Pataliputra,', 'Kashmir: four councils.'], tip_close="Four places, in order. Add a king to each, and you can write the whole answer.",
quiz=[('stupa', 'Name this mound that holds a relic.', 'a stupa'),
      ('manuscript', 'Which three baskets make the Buddhist canon?', 'the Tripitaka'),
      ('gate', 'Where was the third council held?', 'Pataliputra')],
mains='Trace the spread of Buddhism after the death of the Buddha.',
exhibit_say="The stupa goes into its case. A small model stands for a great monument.",
facts=['A mound that holds a relic', 'Four councils, three baskets', 'Great stupas at Sanchi and Bharhut'],
)
build(SPEC, globals())
