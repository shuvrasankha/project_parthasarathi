# Retrieval eval report

- date: 2026-11-08  set: heldout.yaml  queries: 30  runtime: 169s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: False, linked_first: False, fts_text: all
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 67% (n=27) | 67% (n=15) | 67% (n=3) | 67% (n=3) | 33% (n=3) | 100% (n=3) |
| theme overlap: rewrite themes | 66% (n=30) | 65% (n=15) | 63% (n=5) | 100% (n=4) | 56% (n=3) | 39% (n=3) |
| theme overlap: retrieved situations' themes | 59% (n=30) | 61% (n=15) | 55% (n=5) | 50% (n=4) | 44% (n=3) | 83% (n=3) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| verse relevance, LLM judge (0-2 as %) | 45% (n=30) | 51% (n=15) | 50% (n=5) | 25% (n=4) | 50% (n=3) | 28% (n=3) |
| passage relevance, LLM judge (0-2 as %) | 55% (n=30) | 52% (n=15) | 60% (n=5) | 44% (n=4) | 58% (n=3) | 75% (n=3) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- h01 (en): expected `arjuna-kurukshetra-dilemma`, got `pandavas-mendicants-in-ekachakra`, `nala-damayanti-teaches-patience`
- h02 (en): expected `duryodhana-maya-palace`, got `draupadi-disrobing-sabha`, `draupadi-jealous-subhadra-arrival`
- h03 (en): expected `eklavya-drona-thumb`, got `shalya-karna-charioteer`, `arjuna-kurukshetra-dilemma`
- h09 (en): expected `krishna-peace-mission`, got `nala-damayanti-teaches-patience`, `aswatthaman-night-massacre`
- h13 (en): expected `vidura-truth-dhritarashtra`, got `shalya-karna-charioteer`, `vidura-insomnia-burden-of-knowledge`
- h17 (hinglish): expected `duryodhana-maya-palace`, got `arjuna-yudhishthira-gandiva-conflict`, `draupadi-jealous-subhadra-arrival`
- h24 (hi): expected `arjuna-kurukshetra-dilemma`, got `nala-damayanti-teaches-patience`, `karna-envy-arjuna-tournament`
- h25 (banglish): expected `duryodhana-maya-palace`, got `draupadi-jealous-subhadra-arrival`, `bhima-spares-jayadratha`
- h27 (banglish): expected `yudhishthira-dice-game`, got `nala-damayanti-teaches-patience`, `gandhari-lament-sons`

## Per query

### h01 (en) — MISS

> I froze during my job interview and now I'm scared to even apply anywhere again.

- rewritten: The person froze during a job interview and now feels scared to apply anywhere again.
- themes: fear, fear of failure, career, self-worth, paralysis  (expected: fear of failure, career, paralysis)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `pandavas-mendicants-in-ekachakra` 0.0308; `nala-damayanti-teaches-patience` 0.0306
- verses: `11.45` 0.544 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `4.40` 0.525 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `7.27` 0.467 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `santi-138-21` 0.496 [direct]; `vana-65-6` 0.456 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [1, 1, 0, 1, 0]

### h02 (en) — MISS

> My sister always gets praised at family dinners and nobody even notices what I've achieved.

- rewritten: The person feels overlooked and undervalued because their sister receives praise at family dinners while their own achievements go unnoticed.
- themes: envy, humiliation, family, self-worth  (expected: envy, family, favoritism, self-worth)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-disrobing-sabha` 0.0325; `draupadi-jealous-subhadra-arrival` 0.0317
- verses: `16.15` 0.567 [direct] "I am wealthy, well-born; what other is there that is like unto me? I …; `1.40` 0.557 [direct] In the destruction of a family the immemorial family traditions perish…; `6.6` 0.546 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `anusasana-105-2` 0.577 [direct]; `anusasana-44-5` 0.574 [direct]
- judge grades (verses then passages): [1, 1, 1, 1, 0]

### h03 (en) — MISS

> My coach makes me give up my weekends and my health so his favourite player can shine.

- rewritten: The person feels forced by their coach to give up weekends and their health so the coach's favourite player can shine, leaving them feeling burdened and resentful.
- themes: duty, sacrifice, injustice, self-worth, loyalty  (expected: exploitation, injustice, sacrifice, mentor)
- expected situation: eklavya-drona-thumb
- situations: `shalya-karna-charioteer` 0.0308; `arjuna-kurukshetra-dilemma` 0.0304
- verses: `2.7` 0.632 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.624 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `17.11` 0.570 [direct] The sacrifice which is offered by men without desire for fruit, as enj…
- passages: `bhishma-26-5` 0.508 [situation:arjuna-kurukshetra-dilemma]; `santi-244-4` 0.472 [direct]
- judge grades (verses then passages): [1, 2, 1, 1, 1]

### h04 (en) — HIT

> I gambled away the rent money at a card game last night. My family doesn't know yet.

- rewritten: The person gambled away the rent money at a card game and is worried that their family does not yet know.
- themes: guilt, fear, family, loss, despair  (expected: addiction, gambling, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `yudhishthira-grief-after-victory` 0.0323
- verses: `1.40` 0.583 [direct] In the destruction of a family the immemorial family traditions perish…; `1.42` 0.551 [direct] This confusion draggeth to hell the slayers of the family, and the fam…; `16.15` 0.543 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …
- passages: `adi-162-2` 0.560 [direct]; `vana-65-6` 0.541 [direct]
- judge grades (verses then passages): [1, 1, 1, 2, 2]

### h05 (en) — HIT

> My son died in an accident last year. People tell me to move on but I can't.

- rewritten: The person lost their son in an accident last year and feels unable to move on despite others urging them to.
- themes: grief, loss, death, despair  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0323
- verses: `13.10` 0.607 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `16.16` 0.565 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `16.11` 0.554 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-139-8` 0.606 [direct]; `vana-65-6` 0.583 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [2, 1, 0, 2, 1]

### h06 (en) — HIT

> In the meeting, my colleague mocked me and the senior people laughed along. Nobody defended me.

- rewritten: The person feels humiliated after a colleague mocked them in a meeting while senior staff laughed and no one defended them, leaving them feeling exposed and unsupported.
- themes: humiliation, abandonment, self-worth, fear, loneliness  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0325; `vikarna-protests-draupadi-disrobing` 0.0315
- verses: `12.18` 0.600 [direct] Alike to foe and friend, and also in fame and ignominy, alike in cold …; `6.6` 0.558 [direct] The Self is the friend of the self of him in whom the self by the Self…; `3.35` 0.526 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `santi-111-10` 0.620 [direct]; `santi-80-4` 0.586 [direct]
- judge grades (verses then passages): [2, 1, 2, 2, 1]

### h07 (en) — HIT

> Everyone says I'm the most honest person they know, but to save my team I'd have to twist the truth.

- rewritten: The person is praised as the most honest individual, yet feels compelled to twist the truth in order to save their team.
- themes: integrity, duty, loyalty, deception  (expected: truth, deception, duty, integrity)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `yudhishthira-ashwatthama-lie` 0.0328; `yudhishthira-seeks-blessings-from-elders` 0.0310
- verses: `3.35` 0.631 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.615 [direct] Better is one's own duty though destitute of merits than the well-exec…; `18.45` 0.607 [situation:yudhishthira-ashwatthama-lie] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `anusasana-75-4` 0.586 [direct]; `santi-162-1` 0.574 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 2]

### h08 (en) — HIT

> I made a public promise that I'd finish this project by Friday or resign. It's Thursday and I'm nowhere close.

- rewritten: The person made a public promise to finish a project by Friday or resign, and now on Thursday they are far from completing it, feeling pressure and anxiety about meeting the commitment.
- themes: duty, fear of failure, career, guilt, pride  (expected: vow, fear of failure, pride)
- expected situation: arjuna-jayadratha-vow-sunset
- situations: `arjuna-jayadratha-vow-sunset` 0.0323; `shalya-karna-charioteer` 0.0323
- verses: `3.35` 0.612 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `16.10` 0.603 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.7` 0.603 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `santi-138-21` 0.507 [direct]; `anusasana-138-2` 0.451 [direct]
- judge grades (verses then passages): [2, 0, 2, 0, 0]

### h09 (en) — MISS

> I tried everything to stop two departments from fighting, but nobody would compromise.

- rewritten: The person has tried everything to stop two departments from fighting, but nobody will compromise, leaving them feeling stuck and frustrated.
- themes: rivalry, anger, leadership, duty, despair  (expected: peace, conflict, mediation, failure)
- expected situation: krishna-peace-mission
- situations: `nala-damayanti-teaches-patience` 0.0320; `aswatthaman-night-massacre` 0.0300
- verses: `3.34` 0.574 [direct] Affection and aversion for the objects of sense abide in the senses; l…; `2.63` 0.571 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `3.35` 0.567 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `santi-102-3` 0.573 [direct]; `santi-227-4` 0.560 [direct]
- judge grades (verses then passages): [0, 1, 1, 2, 1]

### h10 (en) — HIT

> I finally beat my rival for the top job and now I can't sleep thinking about what it cost.

- rewritten: The person has achieved the top job by defeating a rival, but now feels restless and unable to sleep, worrying about the price they paid for the victory.
- themes: rivalry, guilt, fear, despair  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0325; `vidura-insomnia-burden-of-knowledge` 0.0315
- verses: `16.10` 0.615 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `11.33` 0.613 [direct] Therefore stand up! win for thyself renown, Conquer thy foes, enjoy th…; `2.63` 0.572 [situation:vidura-insomnia-burden-of-knowledge] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `udyoga-72-6` 0.621 [direct]; `santi-140-5` 0.585 [direct]
- judge grades (verses then passages): [1, 1, 1, 2, 1]

### h11 (en) — HIT

> I just found out the man who raised me isn't my real father. I don't know where I belong.

- rewritten: The person has just discovered that the man who raised them is not their biological father and feels uncertain about where they belong.
- themes: identity, family, betrayal, loneliness  (expected: identity, family, abandonment)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `yudhishthira-regrets-karna` 0.0315
- verses: `13.10` 0.603 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `1.34` 0.530 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `1.41` 0.528 [direct] Owing to predominance of lawlessness, O Krishna, the women of the fami…
- passages: `anusasana-105-2` 0.511 [direct]; `udyoga-146-1` 0.434 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [0, 1, 0, 0, 2]

### h12 (en) — HIT

> My father always covers for my brother's mistakes, even when they hurt me.

- rewritten: The person feels hurt because their father always covers for their brother's mistakes, even when those mistakes cause them pain.
- themes: favoritism, family, injustice  (expected: favoritism, family, injustice)
- expected situation: dhritarashtra-lac-house
- situations: `dhritarashtra-lac-house` 0.0325; `yayati-sons-refuse-youth` 0.0313
- verses: `1.40` 0.581 [direct] In the destruction of a family the immemorial family traditions perish…; `1.41` 0.532 [direct] Owing to predominance of lawlessness, O Krishna, the women of the fami…; `1.34` 0.526 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…
- passages: `anusasana-105-2` 0.589 [direct]; `santi-138-15` 0.544 [direct]
- judge grades (verses then passages): [1, 0, 0, 1, 0]

### h13 (en) — MISS

> I keep telling my boss the plan will fail and he keeps ignoring me. Should I keep warning him?

- rewritten: The person keeps warning their boss that the plan will fail, but the boss ignores them, and they wonder whether to continue warning.
- themes: duty, fear of failure, career, loyalty, fear  (expected: truth, loyalty, duty, counsel)
- expected situation: vidura-truth-dhritarashtra
- situations: `shalya-karna-charioteer` 0.0328; `vidura-insomnia-burden-of-knowledge` 0.0308
- verses: `3.35` 0.615 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `2.7` 0.565 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `18.45` 0.528 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `sauptika-5-1` 0.547 [direct]; `santi-139-10` 0.545 [direct]
- judge grades (verses then passages): [2, 1, 2, 1, 1]

### h14 (en) — HIT

> After the layoffs I lost everything, and it has been three years of struggle.

- rewritten: The person lost everything after layoffs and has been struggling for three years, feeling a deep sense of loss and ongoing hardship.
- themes: loss, despair, fear, career, identity  (expected: patience, setback, loss, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0328; `pandavas-mendicants-in-ekachakra` 0.0323
- verses: `13.10` 0.613 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `9.12` 0.573 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `7.27` 0.466 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `santi-174-3` 0.551 [direct]; `santi-104-5` 0.543 [direct]
- judge grades (verses then passages): [1, 1, 0, 1, 2]

### h15 (en) — HIT

> Someone humiliated my wife and I swore I would make him pay. Now it's eating me up.

- rewritten: The person feels humiliated after someone insulted his wife, swore to make the offender pay, and now the desire for revenge is eating him up.
- themes: humiliation, revenge, anger, guilt  (expected: revenge, humiliation, anger, vow)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.0328; `bhima-kills-duhsasana-drinks-blood` 0.0323
- verses: `2.62` 0.641 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.638 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.34` 0.578 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-259-2` 0.601 [direct]; `vana-28-2` 0.593 [direct]
- judge grades (verses then passages): [2, 2, 1, 0, 1]

### h16 (hinglish) 

> Interview mein ghabra gaya, ab lagta hai main kisi kaam ka nahi hoon

- rewritten: The person became nervous during an interview and now feels that they are useless and incapable of doing any work.
- themes: fear of failure, self-worth, career  (expected: fear of failure, self-worth, career)
- expected situation: -
- situations: `pandavas-mendicants-in-ekachakra` 0.0313; `nala-damayanti-teaches-patience` 0.0310
- verses: `9.12` 0.587 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `4.40` 0.546 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `3.27` 0.534 [direct] All actions are wrought by the quali ties of nature only. The self, de…
- passages: `santi-111-10` 0.577 [direct]; `santi-104-5` 0.537 [direct]
- judge grades (verses then passages): [1, 2, 2, 0, 1]

### h17 (hinglish) — MISS

> Meri didi ko sab log zyada maante hain, mujhe andar se jalan hoti hai

- rewritten: The person feels jealous because everyone respects their elder sister more than them.
- themes: envy, family, self-worth, identity  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `arjuna-yudhishthira-gandiva-conflict` 0.0325; `draupadi-jealous-subhadra-arrival` 0.0323
- verses: `6.6` 0.557 [direct] The Self is the friend of the self of him in whom the self by the Self…; `1.40` 0.539 [direct] In the destruction of a family the immemorial family traditions perish…; `6.5` 0.528 [direct] Let him raise the self by the Self and not let the self become depress…
- passages: `santi-138-15` 0.573 [direct]; `santi-138-14` 0.556 [direct]
- judge grades (verses then passages): [2, 0, 2, 0, 0]

### h18 (hinglish) 

> Papa ki death ke baad sab khaali khaali lagta hai

- rewritten: The person feels empty and hollow after their father's death.
- themes: grief, loss, loneliness  (expected: grief, loss, emptiness)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0320
- verses: `9.12` 0.584 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `16.16` 0.557 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `16.11` 0.545 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `vana-65-6` 0.578 [situation:nala-damayanti-teaches-patience]; `santi-174-3` 0.562 [direct]
- judge grades (verses then passages): [0, 0, 0, 1, 2]

### h19 (hinglish) — HIT

> Satta mein saare paise haar gaya, ghar walon ko kaise bataun

- rewritten: The person has lost all their money in gambling and is worried about how to tell their family.
- themes: loss, guilt, fear, family, despair  (expected: gambling, addiction, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0320; `yudhishthira-grief-after-victory` 0.0320
- verses: `1.40` 0.600 [direct] In the destruction of a family the immemorial family traditions perish…; `16.11` 0.574 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `16.15` 0.569 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …
- passages: `adi-162-2` 0.587 [direct]; `santi-104-5` 0.570 [direct]
- judge grades (verses then passages): [2, 1, 1, 2, 2]

### h20 (hinglish) — HIT

> Sabke saamne meri beizzati hui aur koi kuch nahi bola

- rewritten: The person feels humiliated in front of everyone and no one said anything to defend them.
- themes: humiliation, betrayal, loneliness  (expected: humiliation, silence, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `vikarna-protests-draupadi-disrobing` 0.0323; `draupadi-disrobing-sabha` 0.0318
- verses: `18.25` 0.648 [direct] The action undertaken from delusion, without regard to capacity and co…; `18.22` 0.626 [direct] While that which clingeth to each one thing as if it were the whole, w…; `2.34` 0.525 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-80-4` 0.579 [direct]; `santi-322-12` 0.539 [direct]
- judge grades (verses then passages): [0, 0, 2, 2, 2]

### h21 (hi) — HIT

> मेरे बेटे की मौत के बाद जीने का मन नहीं करता

- rewritten: The person feels a lack of desire to live following the death of their son.
- themes: grief, loss, death, despair, loneliness  (expected: grief, loss, despair)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0323
- verses: `16.11` 0.606 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `17.9` 0.599 [direct] The passionate desire foods that are bitter, sour, saline, over-hot, p…; `16.16` 0.566 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `vana-65-6` 0.585 [situation:nala-damayanti-teaches-patience]; `santi-104-5` 0.576 [direct]
- judge grades (verses then passages): [0, 0, 0, 1, 1]

### h22 (hi) — HIT

> मुझे पता चला कि मुझे बचपन में गोद लिया गया था, अब असली माँ मिलना चाहती है

- rewritten: The person has learned that they were adopted as a child and now wants to meet their biological mother, feeling uncertainty about their identity and family connections.
- themes: identity, family, abandonment, attachment  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `nala-damayanti-teaches-patience` 0.0312
- verses: `2.62` 0.560 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `1.34` 0.554 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `14.7` 0.534 [direct] Motion, the passion nature, know thou, is the source of attachment and…
- passages: `santi-218-6` 0.566 [direct]; `santi-289-2` 0.554 [direct]
- judge grades (verses then passages): [0, 1, 0, 0, 1]

### h23 (hi) 

> मेरा दोस्त गलत रास्ते पर है, पर उसने हमेशा मेरा साथ दिया, मैं क्या करूँ?

- rewritten: The person feels conflicted because their friend has always stood by them, yet now the friend is on a harmful path, and they do not know how to respond.
- themes: loyalty, friendship, duty, integrity  (expected: loyalty, friendship, duty)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0318; `karna-parashurama-curse-lineage` 0.0313
- verses: `2.7` 0.666 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.635 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.569 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-138-14` 0.691 [direct]; `santi-80-2` 0.617 [direct]
- judge grades (verses then passages): [2, 1, 1, 2, 1]

### h24 (hi) — MISS

> परीक्षा से पहले हाथ-पैर काँपने लगते हैं, सब भूल जाता हूँ

- rewritten: The person experiences trembling hands and feet and forgets everything before an exam, feeling intense nervousness and inability to recall what they have studied.
- themes: fear, fear of failure, exams  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `nala-damayanti-teaches-patience` 0.0318; `karna-envy-arjuna-tournament` 0.0310
- verses: `11.45` 0.548 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `10.4` 0.529 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `11.23` 0.525 [direct] Thy mighty Form, with many mouths and eyes, Long armed, with thighs an…
- passages: `santi-219-5` 0.542 [direct]; `santi-194-2` 0.536 [direct]
- judge grades (verses then passages): [0, 1, 0, 1, 0]

### h25 (banglish) — MISS

> Amar didi ke shobai beshi bhalobashe, amar khub hingsha hoy

- rewritten: The person feels intense jealousy because everyone loves their sister more, causing them to feel envious and inadequate.
- themes: envy, family, self-worth  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.0328; `bhima-spares-jayadratha` 0.0313
- verses: `1.40` 0.552 [direct] In the destruction of a family the immemorial family traditions perish…; `6.6` 0.551 [direct] The Self is the friend of the self of him in whom the self by the Self…; `3.43` 0.542 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-25-3` 0.589 [direct]; `santi-138-15` 0.587 [direct]
- judge grades (verses then passages): [0, 2, 1, 2, 1]

### h26 (banglish) — HIT

> Chele mara jawar por ami r kichu bhabte parchi na

- rewritten: The person feels unable to think about anything after the death of their son.
- themes: grief, loss, death, despair, loneliness  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0320
- verses: `13.10` 0.640 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `16.11` 0.598 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `16.16` 0.558 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-139-8` 0.601 [direct]; `vana-65-6` 0.578 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [2, 1, 1, 1, 1]

### h27 (banglish) — MISS

> Juar nesha amar sansar sesh kore dicche

- rewritten: The person feels that their world is ending and is overwhelmed by a sense of loss and despair.
- themes: despair, grief, loss, fear, loneliness  (expected: addiction, gambling, family)
- expected situation: yudhishthira-dice-game
- situations: `nala-damayanti-teaches-patience` 0.0325; `gandhari-lament-sons` 0.0320
- verses: `9.12` 0.694 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `16.16` 0.630 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `11.45` 0.607 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…
- passages: `santi-25-3` 0.651 [direct]; `santi-104-5` 0.638 [direct]
- judge grades (verses then passages): [0, 1, 1, 2, 0]

### h28 (bn) — HIT

> অফিসে সবার সামনে আমাকে অপমান করা হলো, কেউ একটা কথাও বলল না

- rewritten: The person was publicly humiliated at work and feels isolated because no one defended them.
- themes: humiliation, loneliness, abandonment  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0325; `duryodhana-hides-lake` 0.0320
- verses: `18.25` 0.605 [direct] The action undertaken from delusion, without regard to capacity and co…; `13.11` 0.568 [situation:duryodhana-hides-lake] Unflinching devotion to Me by yoga, without other objects, resort to s…; `11.42` 0.539 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…
- passages: `sabha-68-1` 0.476 [situation:draupadi-disrobing-sabha]; `santi-168-2` 0.452 [direct]
- judge grades (verses then passages): [0, 0, 0, 2, 1]

### h29 (bn) — HIT

> বহু বছর ধরে চাকরি খুঁজছি, আর পারছি না, তবু থামতেও পারছি না

- rewritten: The person has been searching for a job for many years without success, yet feels unable to stop looking.
- themes: career, despair, purpose, fear of failure, loneliness  (expected: patience, setback, perseverance, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0328; `krishna-peace-mission` 0.0302
- verses: `9.12` 0.628 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `18.22` 0.554 [direct] While that which clingeth to each one thing as if it were the whole, w…; `7.27` 0.459 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `sauptika-2-3` 0.552 [direct]; `santi-139-10` 0.549 [direct]
- judge grades (verses then passages): [0, 1, 2, 2, 2]

### h30 (bn) — HIT

> আমি জানতে পারলাম আমার আসল মা আমাকে ছোটবেলায় ছেড়ে দিয়েছিল

- rewritten: The person has learned that their biological mother left them when they were a child, and they feel hurt, confused, and uncertain about their identity.
- themes: abandonment, grief, identity, loss, betrayal  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `gandhari-lament-sons` 0.0323
- verses: `2.7` 0.553 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `2.63` 0.551 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `16.16` 0.550 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-174-3` 0.577 [direct]; `santi-218-6` 0.577 [direct]
- judge grades (verses then passages): [1, 1, 0, 2, 0]
