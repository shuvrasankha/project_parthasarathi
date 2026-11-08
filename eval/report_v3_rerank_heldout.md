# Retrieval eval report

- date: 2026-11-08  set: heldout.yaml  queries: 30  runtime: 1036s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: True, linked_first: False, fts_text: all
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 63% (n=27) | 67% (n=15) | 33% (n=3) | 67% (n=3) | 33% (n=3) | 100% (n=3) |
| theme overlap: rewrite themes | 66% (n=30) | 65% (n=15) | 63% (n=5) | 100% (n=4) | 56% (n=3) | 39% (n=3) |
| theme overlap: retrieved situations' themes | 61% (n=30) | 63% (n=15) | 62% (n=5) | 58% (n=4) | 33% (n=3) | 83% (n=3) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| verse relevance, LLM judge (0-2 as %) | 47% (n=30) | 50% (n=15) | 53% (n=5) | 29% (n=4) | 56% (n=3) | 33% (n=3) |
| passage relevance, LLM judge (0-2 as %) | 53% (n=30) | 53% (n=15) | 55% (n=5) | 50% (n=4) | 50% (n=3) | 58% (n=3) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- h02 (en): expected `duryodhana-maya-palace`, got `karna-envy-arjuna-tournament`, `draupadi-disrobing-sabha`
- h03 (en): expected `eklavya-drona-thumb`, got `shalya-karna-charioteer`, `parashurama-kills-mother`
- h05 (en): expected `gandhari-lament-sons`, got `nala-damayanti-teaches-patience`, `savitri-satyavan`
- h09 (en): expected `krishna-peace-mission`, got `yudhishthira-grief-after-victory`, `aswatthaman-night-massacre`
- h13 (en): expected `vidura-truth-dhritarashtra`, got `shalya-karna-charioteer`, `vidura-insomnia-burden-of-knowledge`
- h17 (hinglish): expected `duryodhana-maya-palace`, got `draupadi-jealous-subhadra-arrival`, `karna-envy-arjuna-tournament`
- h20 (hinglish): expected `draupadi-disrobing-sabha`, got `vikarna-protests-draupadi-disrobing`, `bhima-vows-revenge`
- h24 (hi): expected `arjuna-kurukshetra-dilemma`, got `arjuna-jayadratha-vow-sunset`, `nala-damayanti-teaches-patience`
- h25 (banglish): expected `duryodhana-maya-palace`, got `draupadi-jealous-subhadra-arrival`, `karna-envy-arjuna-tournament`
- h27 (banglish): expected `yudhishthira-dice-game`, got `nala-damayanti-teaches-patience`, `yudhishthira-grief-after-victory`

## Per query

### h01 (en) — HIT

> I froze during my job interview and now I'm scared to even apply anywhere again.

- rewritten: The person froze during a job interview and now feels scared to apply anywhere again.
- themes: fear, fear of failure, career, self-worth, paralysis  (expected: fear of failure, career, paralysis)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-kurukshetra-dilemma` 0.0098; `pandavas-mendicants-in-ekachakra` 0.0085
- verses: `11.45` 0.017 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `6.5` 0.003 [direct] Let him raise the self by the Self and not let the self become depress…; `4.40` 0.001 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…
- passages: `santi-220-1` 0.002 [direct]; `santi-138-21` 0.002 [direct]
- judge grades (verses then passages): [1, 1, 1, 2, 1]

### h02 (en) — MISS

> My sister always gets praised at family dinners and nobody even notices what I've achieved.

- rewritten: The person feels overlooked and undervalued because their sister receives praise at family dinners while their own achievements go unnoticed.
- themes: envy, humiliation, family, self-worth  (expected: envy, family, favoritism, self-worth)
- expected situation: duryodhana-maya-palace
- situations: `karna-envy-arjuna-tournament` 0.3005; `draupadi-disrobing-sabha` 0.2279
- verses: `6.6` 0.005 [direct] The Self is the friend of the self of him in whom the self by the Self…; `16.15` 0.003 [direct] "I am wealthy, well-born; what other is there that is like unto me? I …; `1.40` 0.003 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `udyoga-36-4` 0.176 [direct]; `anusasana-44-5` 0.016 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 0]

### h03 (en) — MISS

> My coach makes me give up my weekends and my health so his favourite player can shine.

- rewritten: The person feels forced by their coach to give up weekends and their health so the coach's favourite player can shine, leaving them feeling burdened and resentful.
- themes: duty, sacrifice, injustice, self-worth, loyalty  (expected: exploitation, injustice, sacrifice, mentor)
- expected situation: eklavya-drona-thumb
- situations: `shalya-karna-charioteer` 0.1351; `parashurama-kills-mother` 0.1105
- verses: `6.6` 0.003 [direct] The Self is the friend of the self of him in whom the self by the Self…; `3.35` 0.002 [situation:parashurama-kills-mother] Better one's own duty, though destitute of merit, than the duty of ano…; `17.11` 0.002 [direct] The sacrifice which is offered by men without desire for fruit, as enj…
- passages: `santi-244-4` 0.004 [direct]; `anusasana-149-9` 0.001 [direct]
- judge grades (verses then passages): [1, 2, 1, 1, 0]

### h04 (en) — HIT

> I gambled away the rent money at a card game last night. My family doesn't know yet.

- rewritten: The person gambled away the rent money at a card game and is worried that their family does not yet know.
- themes: guilt, fear, family, loss, despair  (expected: addiction, gambling, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0395; `yudhishthira-grief-after-victory` 0.0116
- verses: `1.40` 0.006 [direct] In the destruction of a family the immemorial family traditions perish…; `1.42` 0.004 [direct] This confusion draggeth to hell the slayers of the family, and the fam…; `16.11` 0.001 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `sabha-58-2` 0.006 [situation:yudhishthira-dice-game]; `adi-162-2` 0.004 [direct]
- judge grades (verses then passages): [1, 1, 0, 2, 2]

### h05 (en) — MISS

> My son died in an accident last year. People tell me to move on but I can't.

- rewritten: The person lost their son in an accident last year and feels unable to move on despite others urging them to.
- themes: grief, loss, death, despair  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `nala-damayanti-teaches-patience` 0.0624; `savitri-satyavan` 0.0613
- verses: `16.11` 0.053 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `18.25` 0.030 [direct] The action undertaken from delusion, without regard to capacity and co…; `13.10` 0.011 [direct] Unattachment, absence of self-identification with son, wife or home, a…
- passages: `santi-139-8` 0.249 [direct]; `santi-174-2` 0.087 [direct]
- judge grades (verses then passages): [0, 0, 2, 2, 2]

### h06 (en) — HIT

> In the meeting, my colleague mocked me and the senior people laughed along. Nobody defended me.

- rewritten: The person feels humiliated after a colleague mocked them in a meeting while senior staff laughed and no one defended them, leaving them feeling exposed and unsupported.
- themes: humiliation, abandonment, self-worth, fear, loneliness  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.8064; `vikarna-protests-draupadi-disrobing` 0.5824
- verses: `12.18` 0.009 [direct] Alike to foe and friend, and also in fame and ignominy, alike in cold …; `6.6` 0.006 [direct] The Self is the friend of the self of him in whom the self by the Self…; `2.34` 0.006 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-111-10` 0.015 [direct]; `santi-80-4` 0.004 [direct]
- judge grades (verses then passages): [2, 1, 2, 2, 1]

### h07 (en) — HIT

> Everyone says I'm the most honest person they know, but to save my team I'd have to twist the truth.

- rewritten: The person is praised as the most honest individual, yet feels compelled to twist the truth in order to save their team.
- themes: integrity, duty, loyalty, deception  (expected: truth, deception, duty, integrity)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `yudhishthira-ashwatthama-lie` 0.8272; `yaksha-prashna` 0.0548
- verses: `18.45` 0.030 [situation:yudhishthira-ashwatthama-lie] Man reacheth perfection by each being intent on his own duty. Listen t…; `18.47` 0.023 [direct] Better is one's own duty though destitute of merits than the well-exec…; `3.35` 0.010 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `karna-69-4` 0.037 [direct]; `drona-191-5` 0.010 [situation:yudhishthira-ashwatthama-lie]
- judge grades (verses then passages): [1, 1, 1, 2, 2]

### h08 (en) — HIT

> I made a public promise that I'd finish this project by Friday or resign. It's Thursday and I'm nowhere close.

- rewritten: The person made a public promise to finish a project by Friday or resign, and now on Thursday they are far from completing it, feeling pressure and anxiety about meeting the commitment.
- themes: duty, fear of failure, career, guilt, pride  (expected: vow, fear of failure, pride)
- expected situation: arjuna-jayadratha-vow-sunset
- situations: `arjuna-jayadratha-vow-sunset` 0.6937; `amba-vow-against-bhishma` 0.1902
- verses: `3.35` 0.009 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `16.10` 0.008 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `18.45` 0.005 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `anusasana-149-9` 0.002 [direct]; `santi-138-21` 0.001 [direct]
- judge grades (verses then passages): [2, 0, 2, 0, 0]

### h09 (en) — MISS

> I tried everything to stop two departments from fighting, but nobody would compromise.

- rewritten: The person has tried everything to stop two departments from fighting, but nobody will compromise, leaving them feeling stuck and frustrated.
- themes: rivalry, anger, leadership, duty, despair  (expected: peace, conflict, mediation, failure)
- expected situation: krishna-peace-mission
- situations: `yudhishthira-grief-after-victory` 0.0175; `aswatthaman-night-massacre` 0.0151
- verses: `3.35` 0.038 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `3.34` 0.004 [direct] Affection and aversion for the objects of sense abide in the senses; l…; `2.63` 0.004 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `santi-102-3` 0.028 [direct]; `santi-227-4` 0.015 [direct]
- judge grades (verses then passages): [1, 0, 1, 2, 1]

### h10 (en) — HIT

> I finally beat my rival for the top job and now I can't sleep thinking about what it cost.

- rewritten: The person has achieved the top job by defeating a rival, but now feels restless and unable to sleep, worrying about the price they paid for the victory.
- themes: rivalry, guilt, fear, despair  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.1233; `karna-envy-arjuna-tournament` 0.0262
- verses: `18.35` 0.362 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …; `16.10` 0.007 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `11.33` 0.004 [direct] Therefore stand up! win for thyself renown, Conquer thy foes, enjoy th…
- passages: `udyoga-72-6` 0.367 [direct]; `santi-104-5` 0.089 [direct]
- judge grades (verses then passages): [1, 1, 1, 2, 1]

### h11 (en) — HIT

> I just found out the man who raised me isn't my real father. I don't know where I belong.

- rewritten: The person has just discovered that the man who raised them is not their biological father and feels uncertain about where they belong.
- themes: identity, family, betrayal, loneliness  (expected: identity, family, abandonment)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.6374; `yudhishthira-regrets-karna` 0.2142
- verses: `13.10` 0.082 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `1.34` 0.016 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `1.41` 0.004 [direct] Owing to predominance of lawlessness, O Krishna, the women of the fami…
- passages: `anusasana-149-9` 0.006 [direct]; `anusasana-105-2` 0.006 [direct]
- judge grades (verses then passages): [0, 1, 0, 0, 0]

### h12 (en) — HIT

> My father always covers for my brother's mistakes, even when they hurt me.

- rewritten: The person feels hurt because their father always covers for their brother's mistakes, even when those mistakes cause them pain.
- themes: favoritism, family, injustice  (expected: favoritism, family, injustice)
- expected situation: dhritarashtra-lac-house
- situations: `dhritarashtra-lac-house` 0.6010; `parashurama-kills-mother` 0.0141
- verses: `1.34` 0.011 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `1.40` 0.006 [direct] In the destruction of a family the immemorial family traditions perish…; `1.41` 0.001 [direct] Owing to predominance of lawlessness, O Krishna, the women of the fami…
- passages: `anusasana-105-2` 0.036 [direct]; `santi-138-15` 0.005 [direct]
- judge grades (verses then passages): [0, 1, 0, 1, 0]

### h13 (en) — MISS

> I keep telling my boss the plan will fail and he keeps ignoring me. Should I keep warning him?

- rewritten: The person keeps warning their boss that the plan will fail, but the boss ignores them, and they wonder whether to continue warning.
- themes: duty, fear of failure, career, loyalty, fear  (expected: truth, loyalty, duty, counsel)
- expected situation: vidura-truth-dhritarashtra
- situations: `shalya-karna-charioteer` 0.1376; `vidura-insomnia-burden-of-knowledge` 0.0443
- verses: `3.35` 0.005 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.45` 0.003 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…; `18.47` 0.001 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-139-10` 0.003 [direct]; `sauptika-5-1` 0.001 [direct]
- judge grades (verses then passages): [2, 2, 1, 1, 1]

### h14 (en) — HIT

> After the layoffs I lost everything, and it has been three years of struggle.

- rewritten: The person lost everything after layoffs and has been struggling for three years, feeling a deep sense of loss and ongoing hardship.
- themes: loss, despair, fear, career, identity  (expected: patience, setback, loss, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.5202; `pandavas-mendicants-in-ekachakra` 0.2277
- verses: `13.10` 0.013 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `4.26` 0.000 [direct] Some pour as sacrifice hearing and the other senses into the fires of …; `9.12` 0.000 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…
- passages: `santi-104-5` 0.086 [direct]; `anusasana-149-9` 0.004 [direct]
- judge grades (verses then passages): [1, 0, 1, 2, 1]

### h15 (en) — HIT

> Someone humiliated my wife and I swore I would make him pay. Now it's eating me up.

- rewritten: The person feels humiliated after someone insulted his wife, swore to make the offender pay, and now the desire for revenge is eating him up.
- themes: humiliation, revenge, anger, guilt  (expected: revenge, humiliation, anger, vow)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.5083; `bhima-kills-duhsasana-drinks-blood` 0.4025
- verses: `2.62` 0.427 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.028 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `16.11` 0.015 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-259-2` 0.010 [direct]; `vana-28-2` 0.010 [direct]
- judge grades (verses then passages): [2, 2, 1, 0, 1]

### h16 (hinglish) 

> Interview mein ghabra gaya, ab lagta hai main kisi kaam ka nahi hoon

- rewritten: The person became nervous during an interview and now feels that they are useless and incapable of doing any work.
- themes: fear of failure, self-worth, career  (expected: fear of failure, self-worth, career)
- expected situation: -
- situations: `draupadi-disrobing-sabha` 0.0204; `arjuna-jayadratha-vow-sunset` 0.0197
- verses: `3.27` 0.004 [direct] All actions are wrought by the quali ties of nature only. The self, de…; `9.12` 0.001 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `4.40` 0.001 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…
- passages: `anusasana-149-9` 0.006 [direct]; `santi-111-10` 0.002 [direct]
- judge grades (verses then passages): [2, 1, 2, 0, 0]

### h17 (hinglish) — MISS

> Meri didi ko sab log zyada maante hain, mujhe andar se jalan hoti hai

- rewritten: The person feels jealous because everyone respects their elder sister more than them.
- themes: envy, family, self-worth, identity  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.0465; `karna-envy-arjuna-tournament` 0.0426
- verses: `6.6` 0.001 [direct] The Self is the friend of the self of him in whom the self by the Self…; `1.40` 0.001 [direct] In the destruction of a family the immemorial family traditions perish…; `6.5` 0.001 [direct] Let him raise the self by the Self and not let the self become depress…
- passages: `santi-138-14` 0.033 [direct]; `anusasana-149-9` 0.010 [direct]
- judge grades (verses then passages): [2, 0, 2, 0, 0]

### h18 (hinglish) 

> Papa ki death ke baad sab khaali khaali lagta hai

- rewritten: The person feels empty and hollow after their father's death.
- themes: grief, loss, loneliness  (expected: grief, loss, emptiness)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.2463; `yudhishthira-grief-after-victory` 0.1041
- verses: `9.12` 0.050 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `16.11` 0.007 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `13.9` 0.001 [direct] Dispassion towards the objects of the senses, and also absence of egoi…
- passages: `santi-174-3` 0.059 [direct]; `santi-139-8` 0.048 [direct]
- judge grades (verses then passages): [0, 0, 1, 2, 1]

### h19 (hinglish) — HIT

> Satta mein saare paise haar gaya, ghar walon ko kaise bataun

- rewritten: The person has lost all their money in gambling and is worried about how to tell their family.
- themes: loss, guilt, fear, family, despair  (expected: gambling, addiction, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0201; `yudhishthira-grief-after-victory` 0.0101
- verses: `1.40` 0.004 [direct] In the destruction of a family the immemorial family traditions perish…; `1.42` 0.003 [direct] This confusion draggeth to hell the slayers of the family, and the fam…; `10.36` 0.000 [situation:yudhishthira-dice-game] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `santi-104-5` 0.016 [direct]; `sabha-58-2` 0.007 [situation:yudhishthira-dice-game]
- judge grades (verses then passages): [2, 1, 0, 2, 2]

### h20 (hinglish) — MISS

> Sabke saamne meri beizzati hui aur koi kuch nahi bola

- rewritten: The person feels humiliated in front of everyone and no one said anything to defend them.
- themes: humiliation, betrayal, loneliness  (expected: humiliation, silence, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `vikarna-protests-draupadi-disrobing` 0.6561; `bhima-vows-revenge` 0.3154
- verses: `2.34` 0.012 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `18.25` 0.001 [direct] The action undertaken from delusion, without regard to capacity and co…; `1.28` 0.000 [situation:vikarna-protests-draupadi-disrobing] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `santi-80-4` 0.005 [direct]; `santi-322-12` 0.003 [direct]
- judge grades (verses then passages): [2, 0, 1, 2, 2]

### h21 (hi) — HIT

> मेरे बेटे की मौत के बाद जीने का मन नहीं करता

- rewritten: The person feels a lack of desire to live following the death of their son.
- themes: grief, loss, death, despair, loneliness  (expected: grief, loss, despair)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.1072; `nala-damayanti-teaches-patience` 0.0794
- verses: `16.11` 0.210 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `17.9` 0.013 [direct] The passionate desire foods that are bitter, sour, saline, over-hot, p…; `2.62` 0.004 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…
- passages: `santi-104-5` 0.667 [direct]; `stri-8-1` 0.519 [direct]
- judge grades (verses then passages): [0, 0, 0, 1, 2]

### h22 (hi) — HIT

> मुझे पता चला कि मुझे बचपन में गोद लिया गया था, अब असली माँ मिलना चाहती है

- rewritten: The person has learned that they were adopted as a child and now wants to meet their biological mother, feeling uncertainty about their identity and family connections.
- themes: identity, family, abandonment, attachment  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.8186; `nala-damayanti-teaches-patience` 0.0162
- verses: `1.34` 0.004 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `2.62` 0.003 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `18.48` 0.001 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…
- passages: `santi-289-2` 0.050 [direct]; `santi-218-6` 0.021 [direct]
- judge grades (verses then passages): [1, 0, 1, 1, 0]

### h23 (hi) 

> मेरा दोस्त गलत रास्ते पर है, पर उसने हमेशा मेरा साथ दिया, मैं क्या करूँ?

- rewritten: The person feels conflicted because their friend has always stood by them, yet now the friend is on a harmful path, and they do not know how to respond.
- themes: loyalty, friendship, duty, integrity  (expected: loyalty, friendship, duty)
- expected situation: -
- situations: `karna-parashurama-curse-lineage` 0.1686; `vikarna-protests-draupadi-disrobing` 0.0737
- verses: `3.35` 0.012 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.008 [direct] Better is one's own duty though destitute of merits than the well-exec…; `2.7` 0.007 [direct] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `santi-138-14` 0.031 [direct]; `santi-80-2` 0.013 [direct]
- judge grades (verses then passages): [1, 1, 2, 2, 1]

### h24 (hi) — MISS

> परीक्षा से पहले हाथ-पैर काँपने लगते हैं, सब भूल जाता हूँ

- rewritten: The person experiences trembling hands and feet and forgets everything before an exam, feeling intense nervousness and inability to recall what they have studied.
- themes: fear, fear of failure, exams  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-jayadratha-vow-sunset` 0.0271; `nala-damayanti-teaches-patience` 0.0240
- verses: `11.45` 0.097 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `10.4` 0.008 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `11.23` 0.007 [direct] Thy mighty Form, with many mouths and eyes, Long armed, with thighs an…
- passages: `anusasana-149-9` 0.003 [direct]; `santi-219-5` 0.000 [direct]
- judge grades (verses then passages): [0, 1, 0, 0, 1]

### h25 (banglish) — MISS

> Amar didi ke shobai beshi bhalobashe, amar khub hingsha hoy

- rewritten: The person feels intense jealousy because everyone loves their sister more, causing them to feel envious and inadequate.
- themes: envy, family, self-worth  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.2196; `karna-envy-arjuna-tournament` 0.1014
- verses: `6.6` 0.004 [direct] The Self is the friend of the self of him in whom the self by the Self…; `1.40` 0.002 [direct] In the destruction of a family the immemorial family traditions perish…; `3.43` 0.001 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-138-14` 0.048 [direct]; `santi-138-15` 0.011 [direct]
- judge grades (verses then passages): [2, 0, 1, 0, 1]

### h26 (banglish) — HIT

> Chele mara jawar por ami r kichu bhabte parchi na

- rewritten: The person feels unable to think about anything after the death of their son.
- themes: grief, loss, death, despair, loneliness  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.1427; `nala-damayanti-teaches-patience` 0.0985
- verses: `16.11` 0.081 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `13.10` 0.079 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.27` 0.018 [direct] For certain is death for the born, and certain is birth for the dead; …
- passages: `stri-8-1` 0.492 [direct]; `santi-139-8` 0.368 [direct]
- judge grades (verses then passages): [1, 2, 2, 2, 1]

### h27 (banglish) — MISS

> Juar nesha amar sansar sesh kore dicche

- rewritten: The person feels that their world is ending and is overwhelmed by a sense of loss and despair.
- themes: despair, grief, loss, fear, loneliness  (expected: addiction, gambling, family)
- expected situation: yudhishthira-dice-game
- situations: `nala-damayanti-teaches-patience` 0.6040; `yudhishthira-grief-after-victory` 0.0965
- verses: `18.35` 0.448 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …; `9.12` 0.082 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `11.45` 0.018 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…
- passages: `santi-104-5` 0.863 [direct]; `santi-25-3` 0.239 [direct]
- judge grades (verses then passages): [1, 0, 1, 0, 2]

### h28 (bn) — HIT

> অফিসে সবার সামনে আমাকে অপমান করা হলো, কেউ একটা কথাও বলল না

- rewritten: The person was publicly humiliated at work and feels isolated because no one defended them.
- themes: humiliation, loneliness, abandonment  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.7973; `duryodhana-hides-lake` 0.7424
- verses: `2.34` 0.013 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `18.25` 0.000 [direct] The action undertaken from delusion, without regard to capacity and co…; `11.42` 0.000 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…
- passages: `sabha-68-1` 0.001 [situation:draupadi-disrobing-sabha]; `santi-168-2` 0.000 [direct]
- judge grades (verses then passages): [2, 0, 0, 2, 1]

### h29 (bn) — HIT

> বহু বছর ধরে চাকরি খুঁজছি, আর পারছি না, তবু থামতেও পারছি না

- rewritten: The person has been searching for a job for many years without success, yet feels unable to stop looking.
- themes: career, despair, purpose, fear of failure, loneliness  (expected: patience, setback, perseverance, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `krishna-peace-mission` 0.0351; `nala-damayanti-teaches-patience` 0.0142
- verses: `9.12` 0.006 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `18.22` 0.001 [direct] While that which clingeth to each one thing as if it were the whole, w…; `2.65` 0.000 [situation:krishna-peace-mission] In that Peace the extinction of all pains ariseth for him, for of him …
- passages: `sauptika-2-3` 0.053 [direct]; `anusasana-149-9` 0.004 [direct]
- judge grades (verses then passages): [0, 1, 1, 2, 0]

### h30 (bn) — HIT

> আমি জানতে পারলাম আমার আসল মা আমাকে ছোটবেলায় ছেড়ে দিয়েছিল

- rewritten: The person has learned that their biological mother left them when they were a child, and they feel hurt, confused, and uncertain about their identity.
- themes: abandonment, grief, identity, loss, betrayal  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.8738; `yudhishthira-regrets-karna` 0.3152
- verses: `2.63` 0.008 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.7` 0.004 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `1.34` 0.002 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…
- passages: `santi-218-6` 0.014 [direct]; `stri-27-2` 0.008 [situation:yudhishthira-regrets-karna]
- judge grades (verses then passages): [1, 1, 0, 0, 2]
