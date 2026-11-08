# Retrieval eval report

- date: 2026-11-08  set: heldout.yaml  queries: 30  runtime: 121s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: False, linked_first: True, fts_text: all
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 67% (n=27) | 67% (n=15) | 67% (n=3) | 67% (n=3) | 33% (n=3) | 100% (n=3) |
| theme overlap: rewrite themes | 66% (n=30) | 65% (n=15) | 63% (n=5) | 100% (n=4) | 56% (n=3) | 39% (n=3) |
| theme overlap: retrieved situations' themes | 59% (n=30) | 61% (n=15) | 55% (n=5) | 50% (n=4) | 44% (n=3) | 83% (n=3) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| verse relevance, LLM judge (0-2 as %) | 31% (n=30) | 39% (n=15) | 27% (n=5) | 4% (n=4) | 33% (n=3) | 33% (n=3) |
| passage relevance, LLM judge (0-2 as %) | 48% (n=30) | 48% (n=15) | 50% (n=5) | 44% (n=4) | 58% (n=3) | 42% (n=3) |

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
- verses: `7.27` 0.467 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …; `18.4` 0.447 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…; `18.62` 0.393 [situation:pandavas-mendicants-in-ekachakra] Flee unto Him for shelter with all thy being, O Bhârata; by His grace …
- passages: `vana-65-6` 0.456 [situation:nala-damayanti-teaches-patience]; `santi-138-21` 0.496 [direct]
- judge grades (verses then passages): [0, 1, 1, 0, 1]

### h02 (en) — MISS

> My sister always gets praised at family dinners and nobody even notices what I've achieved.

- rewritten: The person feels overlooked and undervalued because their sister receives praise at family dinners while their own achievements go unnoticed.
- themes: envy, humiliation, family, self-worth  (expected: envy, family, favoritism, self-worth)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-disrobing-sabha` 0.0325; `draupadi-jealous-subhadra-arrival` 0.0317
- verses: `2.34` 0.487 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `17.6` 0.457 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…; `2.45` 0.425 [situation:draupadi-jealous-subhadra-arrival] The Vedas deal with the three attributes; be thou above these three at…
- passages: `sabha-68-3` 0.490 [situation:draupadi-disrobing-sabha]; `adi-223-3` 0.378 [situation:draupadi-jealous-subhadra-arrival]
- judge grades (verses then passages): [2, 0, 1, 0, 0]

### h03 (en) — MISS

> My coach makes me give up my weekends and my health so his favourite player can shine.

- rewritten: The person feels forced by their coach to give up weekends and their health so the coach's favourite player can shine, leaving them feeling burdened and resentful.
- themes: duty, sacrifice, injustice, self-worth, loyalty  (expected: exploitation, injustice, sacrifice, mentor)
- expected situation: eklavya-drona-thumb
- situations: `shalya-karna-charioteer` 0.0308; `arjuna-kurukshetra-dilemma` 0.0304
- verses: `2.7` 0.632 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `18.43` 0.519 [situation:shalya-karna-charioteer] Prowess, splendour, firmness, dexterity, and also not flying from batt…; `3.36` 0.492 [situation:shalya-karna-charioteer] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `bhishma-26-5` 0.508 [situation:arjuna-kurukshetra-dilemma]; `karna-32-6` 0.446 [situation:shalya-karna-charioteer]
- judge grades (verses then passages): [1, 0, 2, 1, 1]

### h04 (en) — HIT

> I gambled away the rent money at a card game last night. My family doesn't know yet.

- rewritten: The person gambled away the rent money at a card game and is worried that their family does not yet know.
- themes: guilt, fear, family, loss, despair  (expected: addiction, gambling, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `yudhishthira-grief-after-victory` 0.0323
- verses: `16.15` 0.543 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …; `16.11` 0.523 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `10.36` 0.488 [situation:yudhishthira-dice-game] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `sabha-58-2` 0.519 [situation:yudhishthira-dice-game]; `stri-15-2` 0.422 [situation:yudhishthira-grief-after-victory]
- judge grades (verses then passages): [1, 0, 1, 2, 0]

### h05 (en) — HIT

> My son died in an accident last year. People tell me to move on but I can't.

- rewritten: The person lost their son in an accident last year and feels unable to move on despite others urging them to.
- themes: grief, loss, death, despair  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0323
- verses: `16.16` 0.565 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `1.28` 0.502 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `1.31` 0.478 [situation:gandhari-lament-sons] And I see adverse omens, O Keshava. Nor do I foresee any advantage fro…
- passages: `vana-65-6` 0.583 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.526 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [1, 0, 0, 1, 2]

### h06 (en) — HIT

> In the meeting, my colleague mocked me and the senior people laughed along. Nobody defended me.

- rewritten: The person feels humiliated after a colleague mocked them in a meeting while senior staff laughed and no one defended them, leaving them feeling exposed and unsupported.
- themes: humiliation, abandonment, self-worth, fear, loneliness  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0325; `vikarna-protests-draupadi-disrobing` 0.0315
- verses: `2.34` 0.522 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `17.6` 0.483 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…; `1.28` 0.446 [situation:vikarna-protests-draupadi-disrobing] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `sabha-66-17` 0.503 [situation:draupadi-disrobing-sabha]; `santi-111-10` 0.620 [direct]
- judge grades (verses then passages): [2, 0, 0, 2, 2]

### h07 (en) — HIT

> Everyone says I'm the most honest person they know, but to save my team I'd have to twist the truth.

- rewritten: The person is praised as the most honest individual, yet feels compelled to twist the truth in order to save their team.
- themes: integrity, duty, loyalty, deception  (expected: truth, deception, duty, integrity)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `yudhishthira-ashwatthama-lie` 0.0328; `yudhishthira-seeks-blessings-from-elders` 0.0310
- verses: `18.45` 0.607 [situation:yudhishthira-ashwatthama-lie] Man reacheth perfection by each being intent on his own duty. Listen t…; `2.7` 0.581 [situation:yudhishthira-seeks-blessings-from-elders] My heart is weighed down with the vice of faintness; my mind is confus…; `2.34` 0.545 [situation:yudhishthira-ashwatthama-lie] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `drona-191-5` 0.457 [situation:yudhishthira-ashwatthama-lie]; `bhishma-43-6` 0.433 [situation:yudhishthira-seeks-blessings-from-elders]
- judge grades (verses then passages): [1, 0, 0, 2, 0]

### h08 (en) — HIT

> I made a public promise that I'd finish this project by Friday or resign. It's Thursday and I'm nowhere close.

- rewritten: The person made a public promise to finish a project by Friday or resign, and now on Thursday they are far from completing it, feeling pressure and anxiety about meeting the commitment.
- themes: duty, fear of failure, career, guilt, pride  (expected: vow, fear of failure, pride)
- expected situation: arjuna-jayadratha-vow-sunset
- situations: `arjuna-jayadratha-vow-sunset` 0.0323; `shalya-karna-charioteer` 0.0323
- verses: `2.7` 0.603 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `18.9` 0.526 [situation:arjuna-jayadratha-vow-sunset] He who performeth a prescribed action, saying, "it ought to be done," …; `18.43` 0.466 [situation:shalya-karna-charioteer] Prowess, splendour, firmness, dexterity, and also not flying from batt…
- passages: `drona-79-5` 0.441 [situation:arjuna-jayadratha-vow-sunset]; `karna-32-5` 0.407 [situation:shalya-karna-charioteer]
- judge grades (verses then passages): [2, 2, 1, 0, 0]

### h09 (en) — MISS

> I tried everything to stop two departments from fighting, but nobody would compromise.

- rewritten: The person has tried everything to stop two departments from fighting, but nobody will compromise, leaving them feeling stuck and frustrated.
- themes: rivalry, anger, leadership, duty, despair  (expected: peace, conflict, mediation, failure)
- expected situation: krishna-peace-mission
- situations: `nala-damayanti-teaches-patience` 0.0320; `aswatthaman-night-massacre` 0.0300
- verses: `2.63` 0.571 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `7.27` 0.518 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `16.18` 0.480 [situation:aswatthaman-night-massacre] Given over to egoism, power, insolence, lust and wrath, these maliciou…
- passages: `vana-65-6` 0.498 [situation:nala-damayanti-teaches-patience]; `sauptika-10-2` 0.486 [situation:aswatthaman-night-massacre]
- judge grades (verses then passages): [1, 1, 1, 0, 0]

### h10 (en) — HIT

> I finally beat my rival for the top job and now I can't sleep thinking about what it cost.

- rewritten: The person has achieved the top job by defeating a rival, but now feels restless and unable to sleep, worrying about the price they paid for the victory.
- themes: rivalry, guilt, fear, despair  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0325; `vidura-insomnia-burden-of-knowledge` 0.0315
- verses: `2.63` 0.572 [situation:vidura-insomnia-burden-of-knowledge] From anger proceedeth delusion; from delusion confused memory; from co…; `2.8` 0.511 [situation:yudhishthira-grief-after-victory] For I see not that it would drive away this anguish that withers up my…; `2.6` 0.508 [situation:yudhishthira-grief-after-victory] Nor know I which for us be the better, that we conquer them or they co…
- passages: `stri-15-2` 0.468 [situation:yudhishthira-grief-after-victory]; `udyoga-72-6` 0.621 [direct]
- judge grades (verses then passages): [1, 2, 1, 2, 2]

### h11 (en) — HIT

> I just found out the man who raised me isn't my real father. I don't know where I belong.

- rewritten: The person has just discovered that the man who raised them is not their biological father and feels uncertain about where they belong.
- themes: identity, family, betrayal, loneliness  (expected: identity, family, abandonment)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `yudhishthira-regrets-karna` 0.0315
- verses: `2.14` 0.425 [situation:kunti-reveals-karna] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…; `1.28` 0.413 [situation:yudhishthira-regrets-karna] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `18.48` 0.398 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…
- passages: `udyoga-146-1` 0.434 [situation:kunti-reveals-karna]; `stri-27-2` 0.413 [situation:yudhishthira-regrets-karna]
- judge grades (verses then passages): [0, 1, 1, 2, 2]

### h12 (en) — HIT

> My father always covers for my brother's mistakes, even when they hurt me.

- rewritten: The person feels hurt because their father always covers for their brother's mistakes, even when those mistakes cause them pain.
- themes: favoritism, family, injustice  (expected: favoritism, family, injustice)
- expected situation: dhritarashtra-lac-house
- situations: `dhritarashtra-lac-house` 0.0325; `yayati-sons-refuse-youth` 0.0313
- verses: `11.44` 0.520 [situation:yayati-sons-refuse-youth] Therefore I fall before Thee; with my body I worship as it fitting; bl…; `2.6` 0.456 [situation:dhritarashtra-lac-house] Nor know I which for us be the better, that we conquer them or they co…; `2.13` 0.449 [situation:yayati-sons-refuse-youth] As the dweller in the body experienceth in the body childhood, youth, …
- passages: `adi-85-2` 0.468 [situation:yayati-sons-refuse-youth]; `adi-61-2` 0.418 [situation:dhritarashtra-lac-house]
- judge grades (verses then passages): [0, 0, 0, 0, 1]

### h13 (en) — MISS

> I keep telling my boss the plan will fail and he keeps ignoring me. Should I keep warning him?

- rewritten: The person keeps warning their boss that the plan will fail, but the boss ignores them, and they wonder whether to continue warning.
- themes: duty, fear of failure, career, loyalty, fear  (expected: truth, loyalty, duty, counsel)
- expected situation: vidura-truth-dhritarashtra
- situations: `shalya-karna-charioteer` 0.0328; `vidura-insomnia-burden-of-knowledge` 0.0308
- verses: `2.7` 0.565 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `2.63` 0.488 [situation:vidura-insomnia-burden-of-knowledge] From anger proceedeth delusion; from delusion confused memory; from co…; `18.43` 0.448 [situation:shalya-karna-charioteer] Prowess, splendour, firmness, dexterity, and also not flying from batt…
- passages: `karna-32-4` 0.423 [situation:shalya-karna-charioteer]; `sauptika-5-1` 0.547 [direct]
- judge grades (verses then passages): [1, 0, 1, 0, 1]

### h14 (en) — HIT

> After the layoffs I lost everything, and it has been three years of struggle.

- rewritten: The person lost everything after layoffs and has been struggling for three years, feeling a deep sense of loss and ongoing hardship.
- themes: loss, despair, fear, career, identity  (expected: patience, setback, loss, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0328; `pandavas-mendicants-in-ekachakra` 0.0323
- verses: `7.27` 0.466 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.4` 0.461 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…; `18.62` 0.392 [situation:pandavas-mendicants-in-ekachakra] Flee unto Him for shelter with all thy being, O Bhârata; by His grace …
- passages: `vana-65-6` 0.513 [situation:nala-damayanti-teaches-patience]; `santi-174-3` 0.551 [direct]
- judge grades (verses then passages): [0, 0, 2, 2, 1]

### h15 (en) — HIT

> Someone humiliated my wife and I swore I would make him pay. Now it's eating me up.

- rewritten: The person feels humiliated after someone insulted his wife, swore to make the offender pay, and now the desire for revenge is eating him up.
- themes: humiliation, revenge, anger, guilt  (expected: revenge, humiliation, anger, vow)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.0328; `bhima-kills-duhsasana-drinks-blood` 0.0323
- verses: `2.34` 0.578 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `3.36` 0.501 [situation:bhima-vows-revenge] Arjuna said: But dragged on by what does a man commit sin, reluctantly…; `11.30` 0.465 [situation:bhima-kills-duhsasana-drinks-blood] On every side, all-swallowing, fiery-tongued, Thou lickest up mankind,…
- passages: `sabha-70-2` 0.475 [situation:bhima-vows-revenge]; `karna-83-3` 0.470 [situation:bhima-kills-duhsasana-drinks-blood]
- judge grades (verses then passages): [1, 2, 0, 1, 1]

### h16 (hinglish) 

> Interview mein ghabra gaya, ab lagta hai main kisi kaam ka nahi hoon

- rewritten: The person became nervous during an interview and now feels that they are useless and incapable of doing any work.
- themes: fear of failure, self-worth, career  (expected: fear of failure, self-worth, career)
- expected situation: -
- situations: `pandavas-mendicants-in-ekachakra` 0.0313; `nala-damayanti-teaches-patience` 0.0310
- verses: `7.27` 0.451 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …; `18.4` 0.448 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…; `18.1` 0.402 [situation:nala-damayanti-teaches-patience] Arjuna said: I desire, O mighty-armed, to know severally the essence o…
- passages: `vana-65-6` 0.459 [situation:nala-damayanti-teaches-patience]; `santi-111-10` 0.577 [direct]
- judge grades (verses then passages): [0, 0, 0, 1, 0]

### h17 (hinglish) — MISS

> Meri didi ko sab log zyada maante hain, mujhe andar se jalan hoti hai

- rewritten: The person feels jealous because everyone respects their elder sister more than them.
- themes: envy, family, self-worth, identity  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `arjuna-yudhishthira-gandiva-conflict` 0.0325; `draupadi-jealous-subhadra-arrival` 0.0323
- verses: `1.28` 0.447 [situation:arjuna-yudhishthira-gandiva-conflict] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `2.45` 0.440 [situation:draupadi-jealous-subhadra-arrival] The Vedas deal with the three attributes; be thou above these three at…; `18.34` 0.427 [situation:draupadi-jealous-subhadra-arrival] But the firmness, O Arjuna, by which, from attachment desirous of frui…
- passages: `karna-70-4` 0.445 [situation:arjuna-yudhishthira-gandiva-conflict]; `adi-223-1` 0.394 [situation:draupadi-jealous-subhadra-arrival]
- judge grades (verses then passages): [0, 1, 1, 0, 0]

### h18 (hinglish) 

> Papa ki death ke baad sab khaali khaali lagta hai

- rewritten: The person feels empty and hollow after their father's death.
- themes: grief, loss, loneliness  (expected: grief, loss, emptiness)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0320
- verses: `16.16` 0.557 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `7.27` 0.461 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `1.31` 0.459 [situation:gandhari-lament-sons] And I see adverse omens, O Keshava. Nor do I foresee any advantage fro…
- passages: `vana-65-6` 0.578 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.546 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [0, 0, 1, 1, 2]

### h19 (hinglish) — HIT

> Satta mein saare paise haar gaya, ghar walon ko kaise bataun

- rewritten: The person has lost all their money in gambling and is worried about how to tell their family.
- themes: loss, guilt, fear, family, despair  (expected: gambling, addiction, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0320; `yudhishthira-grief-after-victory` 0.0320
- verses: `16.11` 0.574 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `16.15` 0.569 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …; `10.36` 0.517 [situation:yudhishthira-dice-game] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `sabha-58-2` 0.556 [situation:yudhishthira-dice-game]; `stri-15-3` 0.431 [situation:yudhishthira-grief-after-victory]
- judge grades (verses then passages): [1, 1, 0, 2, 0]

### h20 (hinglish) — HIT

> Sabke saamne meri beizzati hui aur koi kuch nahi bola

- rewritten: The person feels humiliated in front of everyone and no one said anything to defend them.
- themes: humiliation, betrayal, loneliness  (expected: humiliation, silence, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `vikarna-protests-draupadi-disrobing` 0.0323; `draupadi-disrobing-sabha` 0.0318
- verses: `2.34` 0.525 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `17.6` 0.490 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…; `1.28` 0.440 [situation:vikarna-protests-draupadi-disrobing] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `sabha-66-17` 0.505 [situation:draupadi-disrobing-sabha]; `santi-80-4` 0.579 [direct]
- judge grades (verses then passages): [2, 0, 1, 2, 2]

### h21 (hi) — HIT

> मेरे बेटे की मौत के बाद जीने का मन नहीं करता

- rewritten: The person feels a lack of desire to live following the death of their son.
- themes: grief, loss, death, despair, loneliness  (expected: grief, loss, despair)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0323
- verses: `16.16` 0.566 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `1.31` 0.525 [situation:gandhari-lament-sons] And I see adverse omens, O Keshava. Nor do I foresee any advantage fro…; `1.28` 0.498 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `vana-65-6` 0.585 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.529 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [0, 0, 1, 1, 2]

### h22 (hi) — HIT

> मुझे पता चला कि मुझे बचपन में गोद लिया गया था, अब असली माँ मिलना चाहती है

- rewritten: The person has learned that they were adopted as a child and now wants to meet their biological mother, feeling uncertainty about their identity and family connections.
- themes: identity, family, abandonment, attachment  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `nala-damayanti-teaches-patience` 0.0312
- verses: `2.14` 0.456 [situation:kunti-reveals-karna] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…; `7.27` 0.453 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.1` 0.427 [situation:nala-damayanti-teaches-patience] Arjuna said: I desire, O mighty-armed, to know severally the essence o…
- passages: `vana-65-6` 0.488 [situation:nala-damayanti-teaches-patience]; `udyoga-146-1` 0.414 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [0, 0, 0, 1, 2]

### h23 (hi) 

> मेरा दोस्त गलत रास्ते पर है, पर उसने हमेशा मेरा साथ दिया, मैं क्या करूँ?

- rewritten: The person feels conflicted because their friend has always stood by them, yet now the friend is on a harmful path, and they do not know how to respond.
- themes: loyalty, friendship, duty, integrity  (expected: loyalty, friendship, duty)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0318; `karna-parashurama-curse-lineage` 0.0313
- verses: `7.27` 0.509 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.4` 0.504 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…; `18.1` 0.453 [situation:nala-damayanti-teaches-patience] Arjuna said: I desire, O mighty-armed, to know severally the essence o…
- passages: `vana-65-6` 0.503 [situation:nala-damayanti-teaches-patience]; `santi-3-4` 0.432 [situation:karna-parashurama-curse-lineage]
- judge grades (verses then passages): [0, 0, 0, 1, 0]

### h24 (hi) — MISS

> परीक्षा से पहले हाथ-पैर काँपने लगते हैं, सब भूल जाता हूँ

- rewritten: The person experiences trembling hands and feet and forgets everything before an exam, feeling intense nervousness and inability to recall what they have studied.
- themes: fear, fear of failure, exams  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `nala-damayanti-teaches-patience` 0.0318; `karna-envy-arjuna-tournament` 0.0310
- verses: `7.27` 0.469 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.34` 0.410 [situation:karna-envy-arjuna-tournament] But the firmness, O Arjuna, by which, from attachment desirous of frui…; `18.4` 0.407 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…
- passages: `vana-65-6` 0.437 [situation:nala-damayanti-teaches-patience]; `adi-136-3` 0.421 [situation:karna-envy-arjuna-tournament]
- judge grades (verses then passages): [0, 0, 0, 0, 0]

### h25 (banglish) — MISS

> Amar didi ke shobai beshi bhalobashe, amar khub hingsha hoy

- rewritten: The person feels intense jealousy because everyone loves their sister more, causing them to feel envious and inadequate.
- themes: envy, family, self-worth  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.0328; `bhima-spares-jayadratha` 0.0313
- verses: `18.34` 0.447 [situation:draupadi-jealous-subhadra-arrival] But the firmness, O Arjuna, by which, from attachment desirous of frui…; `2.45` 0.442 [situation:draupadi-jealous-subhadra-arrival] The Vedas deal with the three attributes; be thou above these three at…; `3.36` 0.395 [situation:draupadi-jealous-subhadra-arrival] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `vana-270-4` 0.415 [situation:bhima-spares-jayadratha]; `adi-223-3` 0.396 [situation:draupadi-jealous-subhadra-arrival]
- judge grades (verses then passages): [0, 1, 1, 0, 0]

### h26 (banglish) — HIT

> Chele mara jawar por ami r kichu bhabte parchi na

- rewritten: The person feels unable to think about anything after the death of their son.
- themes: grief, loss, death, despair, loneliness  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0320
- verses: `16.16` 0.558 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `1.31` 0.507 [situation:gandhari-lament-sons] And I see adverse omens, O Keshava. Nor do I foresee any advantage fro…; `1.28` 0.461 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `vana-65-6` 0.578 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.541 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [1, 0, 1, 1, 2]

### h27 (banglish) — MISS

> Juar nesha amar sansar sesh kore dicche

- rewritten: The person feels that their world is ending and is overwhelmed by a sense of loss and despair.
- themes: despair, grief, loss, fear, loneliness  (expected: addiction, gambling, family)
- expected situation: yudhishthira-dice-game
- situations: `nala-damayanti-teaches-patience` 0.0325; `gandhari-lament-sons` 0.0320
- verses: `16.16` 0.630 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `7.27` 0.549 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `1.28` 0.497 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `vana-65-6` 0.585 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.553 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [1, 0, 1, 2, 2]

### h28 (bn) — HIT

> অফিসে সবার সামনে আমাকে অপমান করা হলো, কেউ একটা কথাও বলল না

- rewritten: The person was publicly humiliated at work and feels isolated because no one defended them.
- themes: humiliation, loneliness, abandonment  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0325; `duryodhana-hides-lake` 0.0320
- verses: `13.11` 0.568 [situation:duryodhana-hides-lake] Unflinching devotion to Me by yoga, without other objects, resort to s…; `2.34` 0.497 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `6.10` 0.495 [situation:duryodhana-hides-lake] Let the Yogî constantly engage himself in yoga, remaining in a secret …
- passages: `sabha-68-1` 0.476 [situation:draupadi-disrobing-sabha]; `shalya-32-6` 0.420 [situation:duryodhana-hides-lake]
- judge grades (verses then passages): [0, 2, 1, 2, 0]

### h29 (bn) — HIT

> বহু বছর ধরে চাকরি খুঁজছি, আর পারছি না, তবু থামতেও পারছি না

- rewritten: The person has been searching for a job for many years without success, yet feels unable to stop looking.
- themes: career, despair, purpose, fear of failure, loneliness  (expected: patience, setback, perseverance, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0328; `krishna-peace-mission` 0.0302
- verses: `7.27` 0.459 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.4` 0.404 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…; `2.65` 0.384 [situation:krishna-peace-mission] In that Peace the extinction of all pains ariseth for him, for of him …
- passages: `vana-65-6` 0.480 [situation:nala-damayanti-teaches-patience]; `udyoga-129-4` 0.460 [situation:krishna-peace-mission]
- judge grades (verses then passages): [2, 0, 1, 0, 1]

### h30 (bn) — HIT

> আমি জানতে পারলাম আমার আসল মা আমাকে ছোটবেলায় ছেড়ে দিয়েছিল

- rewritten: The person has learned that their biological mother left them when they were a child, and they feel hurt, confused, and uncertain about their identity.
- themes: abandonment, grief, identity, loss, betrayal  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `gandhari-lament-sons` 0.0323
- verses: `16.16` 0.550 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `2.14` 0.448 [situation:kunti-reveals-karna] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…; `1.28` 0.445 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `stri-16-5` 0.484 [situation:gandhari-lament-sons]; `udyoga-146-1` 0.412 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [0, 0, 0, 0, 2]
