# Retrieval eval report

- date: 2026-11-08  set: heldout.yaml  queries: 30  runtime: 139s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: False, linked_first: False, fts_text: all, rewrite: False
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 59% (n=27) | 67% (n=15) | 33% (n=3) | 67% (n=3) | 0% (n=3) | 100% (n=3) |
| theme overlap: rewrite themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| theme overlap: retrieved situations' themes | 55% (n=30) | 62% (n=15) | 27% (n=5) | 75% (n=4) | 11% (n=3) | 83% (n=3) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| verse relevance, LLM judge (0-2 as %) | 27% (n=30) | 33% (n=15) | 27% (n=5) | 29% (n=4) | 17% (n=3) | 6% (n=3) |
| passage relevance, LLM judge (0-2 as %) | 43% (n=30) | 57% (n=15) | 10% (n=5) | 56% (n=4) | 8% (n=3) | 50% (n=3) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- h01 (en): expected `arjuna-kurukshetra-dilemma`, got `pandavas-mendicants-in-ekachakra`, `karna-parashurama-curse-lineage`
- h02 (en): expected `duryodhana-maya-palace`, got `karna-envy-arjuna-tournament`, `draupadi-disrobing-sabha`
- h03 (en): expected `eklavya-drona-thumb`, got `yudhishthira-dice-game`, `yaksha-prashna`
- h09 (en): expected `krishna-peace-mission`, got `duryodhana-hides-lake`, `arjuna-kurukshetra-dilemma`
- h12 (en): expected `dhritarashtra-lac-house`, got `yudhishthira-regrets-karna`, `kunti-reveals-karna`
- h19 (hinglish): expected `yudhishthira-dice-game`, got `savitri-satyavan`, `aswatthaman-night-massacre`
- h20 (hinglish): expected `draupadi-disrobing-sabha`, got `amba-vow-against-bhishma`, `yudhishthira-dice-game`
- h24 (hi): expected `arjuna-kurukshetra-dilemma`, got `uttara-freezes-battle`, `pandavas-mendicants-in-ekachakra`
- h25 (banglish): expected `duryodhana-maya-palace`, got `amba-vow-against-bhishma`, `karna-parashurama-curse-lineage`
- h26 (banglish): expected `gandhari-lament-sons`, got `arjuna-kurukshetra-dilemma`, `bhima-spares-jayadratha`
- h27 (banglish): expected `yudhishthira-dice-game`, got `pandavas-mendicants-in-ekachakra`, `arjuna-jayadratha-vow-sunset`

## Per query

### h01 (en) — MISS

> I froze during my job interview and now I'm scared to even apply anywhere again.

- rewritten: I froze during my job interview and now I'm scared to even apply anywhere again.
- themes: -  (expected: fear of failure, career, paralysis)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `pandavas-mendicants-in-ekachakra` 0.0318; `karna-parashurama-curse-lineage` 0.0310
- verses: `1.29` 0.527 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `1.30` 0.503 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `2.8` 0.446 [direct] For I see not that it would drive away this anguish that withers up my…
- passages: `santi-146-2` 0.483 [direct]; `udyoga-112-2` 0.466 [direct]
- judge grades (verses then passages): [2, 2, 1, 0, 0]

### h02 (en) — MISS

> My sister always gets praised at family dinners and nobody even notices what I've achieved.

- rewritten: My sister always gets praised at family dinners and nobody even notices what I've achieved.
- themes: -  (expected: envy, family, favoritism, self-worth)
- expected situation: duryodhana-maya-palace
- situations: `karna-envy-arjuna-tournament` 0.0320; `draupadi-disrobing-sabha` 0.0315
- verses: `7.3` 0.488 [direct] Among thousands of men scarce one striveth for perfection; of the succ…; `1.38` 0.472 [direct] Although these, with intelligence overpowered by greed, see no guilt i…; `2.40` 0.437 [direct] In this there is no loss of effort, nor is there transgression. Even a…
- passages: `santi-293-1` 0.500 [direct]; `anusasana-123-2` 0.494 [direct]
- judge grades (verses then passages): [0, 0, 1, 0, 0]

### h03 (en) — MISS

> My coach makes me give up my weekends and my health so his favourite player can shine.

- rewritten: My coach makes me give up my weekends and my health so his favourite player can shine.
- themes: -  (expected: exploitation, injustice, sacrifice, mentor)
- expected situation: eklavya-drona-thumb
- situations: `yudhishthira-dice-game` 0.0317; `yaksha-prashna` 0.0315
- verses: `7.21` 0.529 [direct] Any devotee who seeketh to worship with faith any such aspect, I veril…; `10.10` 0.523 [direct] To these, ever harmonious, worshipping in love, I give the yoga of dis…; `10.36` 0.506 [situation:yudhishthira-dice-game] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `sabha-58-3` 0.522 [situation:yudhishthira-dice-game]; `drona-149-3` 0.518 [direct]
- judge grades (verses then passages): [0, 0, 1, 1, 0]

### h04 (en) — HIT

> I gambled away the rent money at a card game last night. My family doesn't know yet.

- rewritten: I gambled away the rent money at a card game last night. My family doesn't know yet.
- themes: -  (expected: addiction, gambling, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `kunti-reveals-karna` 0.0323
- verses: `1.42` 0.492 [direct] This confusion draggeth to hell the slayers of the family, and the fam…; `1.40` 0.464 [direct] In the destruction of a family the immemorial family traditions perish…; `16.15` 0.461 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …
- passages: `adi-162-2` 0.500 [direct]; `vana-65-6` 0.493 [direct]
- judge grades (verses then passages): [0, 0, 2, 2, 2]

### h05 (en) — HIT

> My son died in an accident last year. People tell me to move on but I can't.

- rewritten: My son died in an accident last year. People tell me to move on but I can't.
- themes: -  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0320; `yayati-sons-refuse-youth` 0.0315
- verses: `1.30` 0.506 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `3.2` 0.495 [direct] With these perplexing words Thou only confusest my understanding; ther…; `2.13` 0.457 [situation:yayati-sons-refuse-youth] As the dweller in the body experienceth in the body childhood, youth, …
- passages: `santi-153-6` 0.555 [direct]; `santi-153-9` 0.540 [direct]
- judge grades (verses then passages): [0, 1, 2, 2, 2]

### h06 (en) — HIT

> In the meeting, my colleague mocked me and the senior people laughed along. Nobody defended me.

- rewritten: In the meeting, my colleague mocked me and the senior people laughed along. Nobody defended me.
- themes: -  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0328; `vikarna-protests-draupadi-disrobing` 0.0320
- verses: `9.22` 0.521 [direct] To those men who worship Me alone thinking of no other, to those ever …; `3.26` 0.510 [direct] Let no wise man unsettle the mind of ignorant people attached to actio…; `17.6` 0.509 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…
- passages: `santi-80-4` 0.508 [direct]; `sabha-66-17` 0.502 [situation:draupadi-disrobing-sabha]
- judge grades (verses then passages): [0, 0, 0, 1, 2]

### h07 (en) — HIT

> Everyone says I'm the most honest person they know, but to save my team I'd have to twist the truth.

- rewritten: Everyone says I'm the most honest person they know, but to save my team I'd have to twist the truth.
- themes: -  (expected: truth, deception, duty, integrity)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `yudhishthira-ashwatthama-lie` 0.0328; `vidura-truth-dhritarashtra` 0.0308
- verses: `10.36` 0.554 [direct] I am the gambling of the cheat, and the splendour of splendid things I…; `18.64` 0.534 [direct] Listen thou again to My supreme word, most secret of all; beloved art …; `18.45` 0.508 [situation:yudhishthira-ashwatthama-lie] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `santi-162-1` 0.541 [direct]; `santi-109-1` 0.508 [direct]
- judge grades (verses then passages): [0, 0, 1, 2, 2]

### h08 (en) — HIT

> I made a public promise that I'd finish this project by Friday or resign. It's Thursday and I'm nowhere close.

- rewritten: I made a public promise that I'd finish this project by Friday or resign. It's Thursday and I'm nowhere close.
- themes: -  (expected: vow, fear of failure, pride)
- expected situation: arjuna-jayadratha-vow-sunset
- situations: `karna-refuses-bhishma-command` 0.0323; `arjuna-jayadratha-vow-sunset` 0.0320
- verses: `1.29` 0.485 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `4.20` 0.450 [direct] Having abandoned attachment to the fruit of action, always content, no…; `11.32` 0.443 [direct] Time am I, laying desolate the world, Made manifest on earth to slay m…
- passages: `vana-34-3` 0.462 [direct]; `drona-76-3` 0.409 [situation:arjuna-jayadratha-vow-sunset]
- judge grades (verses then passages): [0, 1, 0, 2, 2]

### h09 (en) — MISS

> I tried everything to stop two departments from fighting, but nobody would compromise.

- rewritten: I tried everything to stop two departments from fighting, but nobody would compromise.
- themes: -  (expected: peace, conflict, mediation, failure)
- expected situation: krishna-peace-mission
- situations: `duryodhana-hides-lake` 0.0315; `arjuna-kurukshetra-dilemma` 0.0304
- verses: `1.22` 0.505 [direct] That I may behold these standing, longing for battle, with whom I must…; `3.34` 0.505 [direct] Affection and aversion for the objects of sense abide in the senses; l…; `3.24` 0.476 [direct] These worlds would fall into ruin, if I did not perform action; I shou…
- passages: `bhishma-44-4` 0.513 [direct]; `shalya-32-6` 0.476 [situation:duryodhana-hides-lake]
- judge grades (verses then passages): [0, 1, 0, 1, 0]

### h10 (en) — HIT

> I finally beat my rival for the top job and now I can't sleep thinking about what it cost.

- rewritten: I finally beat my rival for the top job and now I can't sleep thinking about what it cost.
- themes: -  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0325; `karna-envy-arjuna-tournament` 0.0311
- verses: `1.22` 0.538 [direct] That I may behold these standing, longing for battle, with whom I must…; `16.13` 0.533 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…; `2.8` 0.509 [situation:yudhishthira-grief-after-victory] For I see not that it would drive away this anguish that withers up my…
- passages: `santi-229-3` 0.527 [direct]; `santi-177-2` 0.521 [direct]
- judge grades (verses then passages): [0, 2, 2, 1, 1]

### h11 (en) — HIT

> I just found out the man who raised me isn't my real father. I don't know where I belong.

- rewritten: I just found out the man who raised me isn't my real father. I don't know where I belong.
- themes: -  (expected: identity, family, abandonment)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0325; `yudhishthira-regrets-karna` 0.0320
- verses: `7.25` 0.551 [direct] Nor am I of all discovered, enveloped in My creation-illusion. This de…; `9.4` 0.538 [direct] By Me all this world is pervaded in My unmanifested aspect; all beings…; `4.32` 0.351 [direct] Many and various sacrifices are thus spread out before the Eternal. Kn…
- passages: `santi-308-4` 0.532 [direct]; `santi-266-5` 0.508 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 1]

### h12 (en) — MISS

> My father always covers for my brother's mistakes, even when they hurt me.

- rewritten: My father always covers for my brother's mistakes, even when they hurt me.
- themes: -  (expected: favoritism, family, injustice)
- expected situation: dhritarashtra-lac-house
- situations: `yudhishthira-regrets-karna` 0.0328; `kunti-reveals-karna` 0.0320
- verses: `18.56` 0.510 [direct] Though ever performing all actions, taking refuge in Me, by My grace h…; `18.48` 0.465 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…; `4.11` 0.448 [direct] However men approach Me, even so do I welcome them, for the path men t…
- passages: `anusasana-105-2` 0.550 [direct]; `adi-36-2` 0.501 [direct]
- judge grades (verses then passages): [0, 1, 0, 2, 1]

### h13 (en) — HIT

> I keep telling my boss the plan will fail and he keeps ignoring me. Should I keep warning him?

- rewritten: I keep telling my boss the plan will fail and he keeps ignoring me. Should I keep warning him?
- themes: -  (expected: truth, loyalty, duty, counsel)
- expected situation: vidura-truth-dhritarashtra
- situations: `vidura-truth-dhritarashtra` 0.0320; `shalya-karna-charioteer` 0.0315
- verses: `1.29` 0.487 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `3.32` 0.474 [direct] Who carp at My teaching and act not thereon, senseless, deluded in all…; `2.7` 0.460 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `santi-138-21` 0.521 [direct]; `santi-137-1` 0.509 [direct]
- judge grades (verses then passages): [0, 1, 1, 1, 2]

### h14 (en) — HIT

> After the layoffs I lost everything, and it has been three years of struggle.

- rewritten: After the layoffs I lost everything, and it has been three years of struggle.
- themes: -  (expected: patience, setback, loss, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0323; `duryodhana-hides-lake` 0.0320
- verses: `13.11` 0.485 [situation:duryodhana-hides-lake] Unflinching devotion to Me by yoga, without other objects, resort to s…; `16.21` 0.474 [direct] Triple is the gate of this hell, destructive of the self—lust, wrath, …; `9.21` 0.467 [direct] They, having enjoyed the spacious heaven-world, their holiness withere…
- passages: `vana-65-6` 0.516 [situation:nala-damayanti-teaches-patience]; `santi-7-2` 0.503 [direct]
- judge grades (verses then passages): [0, 2, 1, 2, 1]

### h15 (en) — HIT

> Someone humiliated my wife and I swore I would make him pay. Now it's eating me up.

- rewritten: Someone humiliated my wife and I swore I would make him pay. Now it's eating me up.
- themes: -  (expected: revenge, humiliation, anger, vow)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.0328; `bhima-spares-jayadratha` 0.0315
- verses: `16.18` 0.606 [direct] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `1.29` 0.587 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.34` 0.570 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `adi-162-2` 0.589 [direct]; `santi-266-7` 0.580 [direct]
- judge grades (verses then passages): [2, 1, 2, 0, 1]

### h16 (hinglish) 

> Interview mein ghabra gaya, ab lagta hai main kisi kaam ka nahi hoon

- rewritten: Interview mein ghabra gaya, ab lagta hai main kisi kaam ka nahi hoon
- themes: -  (expected: fear of failure, self-worth, career)
- expected situation: -
- situations: `pandavas-mendicants-in-ekachakra` 0.0164; `arjuna-jayadratha-vow-sunset` 0.0161
- verses: `10.20` 0.476 [direct] I, O Gudakesha, am the Self, seated in the heart of all beings; I am t…; `16.13` 0.473 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…; `10.36` 0.471 [direct] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `aswamedha-42-1` 0.487 [direct]; `santi-361-3` 0.480 [direct]
- judge grades (verses then passages): [0, 1, 1, 0, 0]

### h17 (hinglish) — HIT

> Meri didi ko sab log zyada maante hain, mujhe andar se jalan hoti hai

- rewritten: Meri didi ko sab log zyada maante hain, mujhe andar se jalan hoti hai
- themes: -  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `pandavas-mendicants-in-ekachakra` 0.0164; `duryodhana-maya-palace` 0.0161
- verses: `15.13` 0.483 [direct] Permeating the soil, I support beings by my vital energy, and having b…; `14.11` 0.483 [direct] When the wisdom-light streameth forth from all the gates of the body, …; `3.3` 0.479 [direct] The Blessed Lord said: In this world there is a twofold path, as I bef…
- passages: `vana-296-2` 0.483 [direct]; `vana-206-1` 0.481 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 0]

### h18 (hinglish) 

> Papa ki death ke baad sab khaali khaali lagta hai

- rewritten: Papa ki death ke baad sab khaali khaali lagta hai
- themes: -  (expected: grief, loss, emptiness)
- expected situation: -
- situations: `savitri-satyavan` 0.0325; `gandhari-lament-sons` 0.0315
- verses: `14.4` 0.496 [direct] In whatsoever wombs mortals are produced, O Kaunteya, the great Eterna…; `12.7` 0.462 [direct] These I speedily lift up from the ocean of death and existence, O Pârt…; `2.34` 0.460 [direct] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `drona-125-5` 0.488 [direct]; `udyoga-72-3` 0.463 [direct]
- judge grades (verses then passages): [0, 1, 0, 1, 0]

### h19 (hinglish) — MISS

> Satta mein saare paise haar gaya, ghar walon ko kaise bataun

- rewritten: Satta mein saare paise haar gaya, ghar walon ko kaise bataun
- themes: -  (expected: gambling, addiction, guilt, family)
- expected situation: yudhishthira-dice-game
- situations: `savitri-satyavan` 0.0164; `aswatthaman-night-massacre` 0.0161
- verses: `16.13` 0.458 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…; `1.29` 0.448 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `3.40` 0.445 [direct] The senses, the mind and the Reason are said to be its seat; by these …
- passages: `sabha-3-4` 0.471 [direct]; `santi-337-4` 0.463 [direct]
- judge grades (verses then passages): [2, 1, 1, 0, 0]

### h20 (hinglish) — MISS

> Sabke saamne meri beizzati hui aur koi kuch nahi bola

- rewritten: Sabke saamne meri beizzati hui aur koi kuch nahi bola
- themes: -  (expected: humiliation, silence, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `amba-vow-against-bhishma` 0.0164; `yudhishthira-dice-game` 0.0161
- verses: `15.13` 0.430 [direct] Permeating the soil, I support beings by my vital energy, and having b…; `1.22` 0.428 [direct] That I may behold these standing, longing for battle, with whom I must…; `2.43` 0.423 [direct] With desire for self, with heaven for goal, they offer birth as the fr…
- passages: `anusasana-19-10` 0.461 [direct]; `udyoga-190-1` 0.457 [direct]
- judge grades (verses then passages): [0, 1, 0, 0, 1]

### h21 (hi) — HIT

> मेरे बेटे की मौत के बाद जीने का मन नहीं करता

- rewritten: मेरे बेटे की मौत के बाद जीने का मन नहीं करता
- themes: -  (expected: grief, loss, despair)
- expected situation: gandhari-lament-sons
- situations: `gandhari-lament-sons` 0.0164; `savitri-satyavan` 0.0161
- verses: `2.8` 0.545 [direct] For I see not that it would drive away this anguish that withers up my…; `1.30` 0.507 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `1.31` 0.503 [situation:gandhari-lament-sons] And I see adverse omens, O Keshava. Nor do I foresee any advantage fro…
- passages: `vana-137-2` 0.546 [direct]; `adi-159-5` 0.543 [direct]
- judge grades (verses then passages): [0, 0, 0, 2, 2]

### h22 (hi) — HIT

> मुझे पता चला कि मुझे बचपन में गोद लिया गया था, अब असली माँ मिलना चाहती है

- rewritten: मुझे पता चला कि मुझे बचपन में गोद लिया गया था, अब असली माँ मिलना चाहती है
- themes: -  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0164; `pandavas-mendicants-in-ekachakra` 0.0161
- verses: `4.8` 0.566 [direct] For the protection of the good, for the destruction of evil-doers, for…; `7.6` 0.537 [direct] Know this to be the womb of all beings. I am the source of the forthgo…; `7.29` 0.536 [direct] They who, refuged in Me, strive for liberation from birth and death, t…
- passages: `anusasana-14-14` 0.533 [direct]; `anusasana-12-5` 0.521 [direct]
- judge grades (verses then passages): [0, 1, 0, 0, 1]

### h23 (hi) 

> मेरा दोस्त गलत रास्ते पर है, पर उसने हमेशा मेरा साथ दिया, मैं क्या करूँ?

- rewritten: मेरा दोस्त गलत रास्ते पर है, पर उसने हमेशा मेरा साथ दिया, मैं क्या करूँ?
- themes: -  (expected: loyalty, friendship, duty)
- expected situation: -
- situations: `karna-parashurama-curse-lineage` 0.0164; `vidura-truth-dhritarashtra` 0.0161
- verses: `7.18` 0.551 [direct] Noble are all these, but I hold the wise as verily Myself; he, Self un…; `4.11` 0.551 [direct] However men approach Me, even so do I welcome them, for the path men t…; `3.2` 0.539 [direct] With these perplexing words Thou only confusest my understanding; ther…
- passages: `udyoga-136-1` 0.535 [direct]; `santi-82-3` 0.528 [direct]
- judge grades (verses then passages): [0, 1, 0, 2, 1]

### h24 (hi) — MISS

> परीक्षा से पहले हाथ-पैर काँपने लगते हैं, सब भूल जाता हूँ

- rewritten: परीक्षा से पहले हाथ-पैर काँपने लगते हैं, सब भूल जाता हूँ
- themes: -  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `uttara-freezes-battle` 0.0164; `pandavas-mendicants-in-ekachakra` 0.0161
- verses: `1.29` 0.619 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `1.30` 0.614 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `8.12` 0.537 [direct] All the gates closed, the mind confined in the heart, the life-breath …
- passages: `santi-318-2` 0.499 [direct]; `santi-240-4` 0.495 [direct]
- judge grades (verses then passages): [2, 2, 1, 0, 1]

### h25 (banglish) — MISS

> Amar didi ke shobai beshi bhalobashe, amar khub hingsha hoy

- rewritten: Amar didi ke shobai beshi bhalobashe, amar khub hingsha hoy
- themes: -  (expected: envy, family, favoritism)
- expected situation: duryodhana-maya-palace
- situations: `amba-vow-against-bhishma` 0.0164; `karna-parashurama-curse-lineage` 0.0161
- verses: `1.11` 0.438 [direct] Therefore in the rank and file let all, standing firmly in their respe…; `11.7` 0.426 [direct] Here, to-day, behold the whole universe, movable and immovable, standi…; `1.29` 0.418 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…
- passages: `udyoga-28-3` 0.419 [direct]; `vana-16-4` 0.417 [direct]
- judge grades (verses then passages): [0, 0, 1, 0, 0]

### h26 (banglish) — MISS

> Chele mara jawar por ami r kichu bhabte parchi na

- rewritten: Chele mara jawar por ami r kichu bhabte parchi na
- themes: -  (expected: grief, loss, death)
- expected situation: gandhari-lament-sons
- situations: `arjuna-kurukshetra-dilemma` 0.0164; `bhima-spares-jayadratha` 0.0161
- verses: `18.76` 0.463 [direct] O King, remembering, remembering this marvellous and holy dialogue bet…; `18.6` 0.458 [direct] But even these actions should be done leaving aside attachment and fru…; `4.11` 0.447 [direct] However men approach Me, even so do I welcome them, for the path men t…
- passages: `udyoga-141-7` 0.448 [direct]; `aswamedha-90-5` 0.445 [direct]
- judge grades (verses then passages): [0, 1, 1, 0, 0]

### h27 (banglish) — MISS

> Juar nesha amar sansar sesh kore dicche

- rewritten: Juar nesha amar sansar sesh kore dicche
- themes: -  (expected: addiction, gambling, family)
- expected situation: yudhishthira-dice-game
- situations: `pandavas-mendicants-in-ekachakra` 0.0164; `arjuna-jayadratha-vow-sunset` 0.0161
- verses: `18.76` 0.407 [direct] O King, remembering, remembering this marvellous and holy dialogue bet…; `7.7` 0.405 [direct] There is naught whatsoever higher than I, O Dhananjaya. All this is th…; `10.14` 0.389 [direct] All this I believe true that Thou sayest to me, O Keshava. Thy manifes…
- passages: `adi-36-4` 0.421 [direct]; `adi-76-7` 0.414 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 1]

### h28 (bn) — HIT

> অফিসে সবার সামনে আমাকে অপমান করা হলো, কেউ একটা কথাও বলল না

- rewritten: অফিসে সবার সামনে আমাকে অপমান করা হলো, কেউ একটা কথাও বলল না
- themes: -  (expected: humiliation, silence, injustice, workplace)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0164; `vikarna-protests-draupadi-disrobing` 0.0161
- verses: `18.67` 0.534 [direct] Never is this to be spoken by thee to anyone who is without asceticism…; `13.11` 0.513 [direct] Unflinching devotion to Me by yoga, without other objects, resort to s…; `7.26` 0.506 [direct] I know the beings that are past, that are present, that are to come, O…
- passages: `udyoga-96-1` 0.482 [direct]; `udyoga-189-2` 0.479 [direct]
- judge grades (verses then passages): [0, 0, 0, 1, 0]

### h29 (bn) — HIT

> বহু বছর ধরে চাকরি খুঁজছি, আর পারছি না, তবু থামতেও পারছি না

- rewritten: বহু বছর ধরে চাকরি খুঁজছি, আর পারছি না, তবু থামতেও পারছি না
- themes: -  (expected: patience, setback, perseverance, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0164; `amba-vow-against-bhishma` 0.0161
- verses: `1.29` 0.533 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `1.30` 0.520 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `9.8` 0.516 [direct] Hidden in Nature, which is mine own, I emanate again and again all thi…
- passages: `vana-65-6` 0.449 [situation:nala-damayanti-teaches-patience]; `udyoga-189-2` 0.431 [situation:amba-vow-against-bhishma]
- judge grades (verses then passages): [0, 0, 1, 1, 0]

### h30 (bn) — HIT

> আমি জানতে পারলাম আমার আসল মা আমাকে ছোটবেলায় ছেড়ে দিয়েছিল

- rewritten: আমি জানতে পারলাম আমার আসল মা আমাকে ছোটবেলায় ছেড়ে দিয়েছিল
- themes: -  (expected: abandonment, identity, family)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0164; `pandavas-mendicants-in-ekachakra` 0.0161
- verses: `9.8` 0.506 [direct] Hidden in Nature, which is mine own, I emanate again and again all thi…; `1.30` 0.494 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `1.29` 0.483 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…
- passages: `adi-72-2` 0.498 [direct]; `adi-74-8` 0.489 [direct]
- judge grades (verses then passages): [0, 0, 0, 2, 2]
