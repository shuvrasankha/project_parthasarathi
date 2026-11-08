# Retrieval eval report

- date: 2026-11-08  set: queries.yaml  queries: 50  runtime: 330s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: False, linked_first: False, fts_text: all, rewrite: False
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 36% (n=22) | 50% (n=12) | 0% (n=3) | 50% (n=2) | 0% (n=3) | 50% (n=2) |
| theme overlap: rewrite themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| theme overlap: retrieved situations' themes | 45% (n=50) | 52% (n=25) | 19% (n=8) | 67% (n=6) | 22% (n=6) | 55% (n=5) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| verse relevance, LLM judge (0-2 as %) | 29% (n=50) | 37% (n=25) | 25% (n=8) | 14% (n=6) | 17% (n=6) | 30% (n=5) |
| passage relevance, LLM judge (0-2 as %) | 44% (n=50) | 56% (n=25) | 22% (n=8) | 50% (n=6) | 0% (n=6) | 60% (n=5) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- q01 (en): expected `arjuna-kurukshetra-dilemma`, got `uttara-freezes-battle`, `karna-envy-arjuna-tournament`
- q05 (en): expected `draupadi-disrobing-sabha`, got `vikarna-protests-draupadi-disrobing`, `silence-of-elders-udyoga`
- q15 (en): expected `eklavya-drona-thumb`, got `vikarna-protests-draupadi-disrobing`, `vidura-truth-dhritarashtra`
- q16 (en): expected `dhritarashtra-lac-house`, got `yayati-sons-refuse-youth`, `kunti-reveals-karna`
- q19 (en): expected `savitri-satyavan`, got `yayati-sons-refuse-youth`, `karna-refuses-bhishma-command`
- q24 (en): expected `duryodhana-maya-palace`, got `eklavya-drona-thumb`, `yudhishthira-dice-game`
- q26 (hinglish): expected `arjuna-kurukshetra-dilemma`, got `arjuna-jayadratha-vow-sunset`, `amba-vow-against-bhishma`
- q28 (hinglish): expected `bhima-vows-revenge`, got `uttara-freezes-battle`, `shalya-karna-charioteer`
- q32 (hinglish): expected `yudhishthira-ashwatthama-lie`, got `yudhishthira-grief-after-victory`, `parashurama-kills-mother`
- q35 (hi): expected `duryodhana-maya-palace`, got `karna-envy-arjuna-tournament`, `draupadi-jealous-subhadra-arrival`
- q40 (banglish): expected `draupadi-disrobing-sabha`, got `bhima-vows-revenge`, `silence-of-elders-udyoga`
- q41 (banglish): expected `arjuna-kurukshetra-dilemma`, got `yayati-sons-refuse-youth`, `pandavas-mendicants-in-ekachakra`
- q45 (banglish): expected `yudhishthira-dice-game`, got `eklavya-drona-thumb`, `yudhishthira-ashwatthama-lie`
- q49 (bn): expected `nala-damayanti-teaches-patience`, got `arjuna-jayadratha-vow-sunset`, `duryodhana-maya-palace`

## Per query

### q01 (en) — MISS

> My exams start next week and I can't study at all. I just freeze every time I open the book.

- rewritten: My exams start next week and I can't study at all. I just freeze every time I open the book.
- themes: -  (expected: fear of failure, anxiety, paralysis, duty)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `uttara-freezes-battle` 0.0320; `karna-envy-arjuna-tournament` 0.0320
- verses: `1.29` 0.571 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `6.24` 0.467 [direct] Abandoning without reserve all desires born of the imagination, by the…; `8.7` 0.459 [direct] Therefore at all times think upon Me only and fight. With mind and Rea…
- passages: `santi-322-6` 0.488 [direct]; `santi-227-12` 0.473 [direct]
- judge grades (verses then passages): [2, 1, 2, 0, 1]

### q02 (en) 

> My girlfriend broke up with me after four years and I don't know who I am without her.

- rewritten: My girlfriend broke up with me after four years and I don't know who I am without her.
- themes: -  (expected: grief, loss, attachment, identity)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0328; `pandavas-mendicants-in-ekachakra` 0.0317
- verses: `1.30` 0.531 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `4.13` 0.452 [direct] The four castes were emanated by Me, by the different distribution of …; `18.1` 0.397 [situation:nala-damayanti-teaches-patience] Arjuna said: I desire, O mighty-armed, to know severally the essence o…
- passages: `santi-308-4` 0.518 [direct]; `santi-144-1` 0.501 [direct]
- judge grades (verses then passages): [1, 0, 2, 2, 2]

### q03 (en) 

> My parents want me to become a doctor but I want to study music. I feel like I'm betraying them.

- rewritten: My parents want me to become a doctor but I want to study music. I feel like I'm betraying them.
- themes: -  (expected: career, family, duty, guilt)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0323; `yayati-sons-refuse-youth` 0.0309
- verses: `2.7` 0.539 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.11` 0.435 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `11.44` 0.428 [situation:yayati-sons-refuse-youth] Therefore I fall before Thee; with my body I worship as it fitting; bl…
- passages: `vana-112-3` 0.470 [direct]; `bhishma-40-2` 0.455 [direct]
- judge grades (verses then passages): [2, 1, 1, 1, 1]

### q04 (en) 

> My mother passed away last month and I keep thinking I should have done more for her.

- rewritten: My mother passed away last month and I keep thinking I should have done more for her.
- themes: -  (expected: grief, guilt, loss)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0320; `pandavas-final-journey-renunciation` 0.0310
- verses: `11.45` 0.521 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `2.7` 0.515 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `18.31` 0.420 [direct] That by which one understandeth away Right and Wrong and also what oug…
- passages: `anusasana-117-4` 0.570 [direct]; `santi-277-2` 0.481 [direct]
- judge grades (verses then passages): [1, 2, 1, 2, 1]

### q05 (en) — MISS

> My manager shouted at me in front of the whole team and everyone just stayed quiet.

- rewritten: My manager shouted at me in front of the whole team and everyone just stayed quiet.
- themes: -  (expected: humiliation, anger, injustice, silence)
- expected situation: draupadi-disrobing-sabha
- situations: `vikarna-protests-draupadi-disrobing` 0.0328; `silence-of-elders-udyoga` 0.0317
- verses: `8.12` 0.503 [direct] All the gates closed, the mind confined in the heart, the life-breath …; `12.6` 0.472 [direct] Those verily who, renouncing all actions in Me and intent on Me, worsh…; `2.34` 0.409 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `bhishma-65-4` 0.497 [direct]; `shalya-1-6` 0.496 [direct]
- judge grades (verses then passages): [1, 0, 1, 0, 1]

### q06 (en) — HIT

> My best friend got the promotion I worked for and I can't stop feeling bitter about it.

- rewritten: My best friend got the promotion I worked for and I can't stop feeling bitter about it.
- themes: -  (expected: envy, rivalry, resentment)
- expected situation: karna-envy-arjuna-tournament
- situations: `karna-envy-arjuna-tournament` 0.0325; `yudhishthira-grief-after-victory` 0.0323
- verses: `6.5` 0.486 [direct] Let him raise the self by the Self and not let the self become depress…; `4.3` 0.484 [direct] This same ancient yoga hath been to-day declared to thee by Me, for th…; `2.49` 0.479 [direct] Far lower than the Yoga of Discrimination is action, O Dhananjaya. Tak…
- passages: `santi-111-10` 0.539 [direct]; `santi-80-2` 0.506 [direct]
- judge grades (verses then passages): [1, 0, 2, 1, 0]

### q07 (en) 

> I moved to a new city and I have nobody to talk to. Weekends are the worst.

- rewritten: I moved to a new city and I have nobody to talk to. Weekends are the worst.
- themes: -  (expected: loneliness, isolation)
- expected situation: -
- situations: `pandavas-mendicants-in-ekachakra` 0.0320; `karna-parashurama-curse-lineage` 0.0311
- verses: `13.11` 0.552 [direct] Unflinching devotion to Me by yoga, without other objects, resort to s…; `1.29` 0.542 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.22` 0.443 [direct] As a man, casting off worn-out garments, taketh new ones, so the dwell…
- passages: `vana-65-6` 0.487 [direct]; `santi-141-3` 0.485 [direct]
- judge grades (verses then passages): [1, 0, 0, 1, 0]

### q08 (en) 

> I lied to my wife about money and now the lie has become so big I can't take it back.

- rewritten: I lied to my wife about money and now the lie has become so big I can't take it back.
- themes: -  (expected: guilt, deception, truth, marriage)
- expected situation: -
- situations: `yudhishthira-ashwatthama-lie` 0.0323; `shalya-karna-charioteer` 0.0299
- verses: `2.34` 0.552 [situation:yudhishthira-ashwatthama-lie] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `1.29` 0.550 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `1.41` 0.468 [direct] Owing to predominance of lawlessness, O Krishna, the women of the fami…
- passages: `adi-162-2` 0.563 [direct]; `adi-74-3` 0.512 [direct]
- judge grades (verses then passages): [1, 1, 0, 1, 2]

### q09 (en) — HIT

> I lost all my savings on crypto trading and I keep betting more to win it back.

- rewritten: I lost all my savings on crypto trading and I keep betting more to win it back.
- themes: -  (expected: addiction, gambling, loss, recklessness)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `savitri-satyavan` 0.0318
- verses: `10.36` 0.546 [situation:yudhishthira-dice-game] I am the gambling of the cheat, and the splendour of splendid things I…; `16.13` 0.519 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…; `16.15` 0.491 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …
- passages: `santi-177-2` 0.519 [direct]; `sabha-64-1` 0.514 [situation:yudhishthira-dice-game]
- judge grades (verses then passages): [1, 1, 1, 2, 2]

### q10 (en) 

> My friend is doing something clearly unethical at work but he helped me get this job. Should I report him?

- rewritten: My friend is doing something clearly unethical at work but he helped me get this job. Should I report him?
- themes: -  (expected: loyalty, truth, duty, friendship)
- expected situation: -
- situations: `karna-parashurama-curse-lineage` 0.0328; `parashurama-kills-mother` 0.0312
- verses: `4.3` 0.474 [direct] This same ancient yoga hath been to-day declared to thee by Me, for th…; `15.20` 0.468 [direct] Thus by Me this most secret teaching hath been told O sinless one. Thi…; `6.6` 0.460 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-82-3` 0.523 [direct]; `vana-32-6` 0.510 [direct]
- judge grades (verses then passages): [0, 0, 0, 1, 1]

### q11 (en) 

> I promised my dying father I'd take over his shop, but I hate it and it's ruining my life.

- rewritten: I promised my dying father I'd take over his shop, but I hate it and it's ruining my life.
- themes: -  (expected: vow, duty, family, career)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0328; `arjuna-jayadratha-vow-sunset` 0.0315
- verses: `16.18` 0.556 [direct] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `3.24` 0.503 [direct] These worlds would fall into ruin, if I did not perform action; I shou…; `16.10` 0.475 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …
- passages: `vana-34-3` 0.526 [direct]; `adi-162-2` 0.524 [direct]
- judge grades (verses then passages): [0, 1, 1, 2, 1]

### q12 (en) 

> My brother cheated me out of my share of the family property. I want revenge.

- rewritten: My brother cheated me out of my share of the family property. I want revenge.
- themes: -  (expected: revenge, betrayal, family, anger, injustice)
- expected situation: -
- situations: `bhima-spares-jayadratha` 0.0328; `bhima-vows-revenge` 0.0320
- verses: `16.18` 0.550 [direct] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `10.36` 0.542 [direct] I am the gambling of the cheat, and the splendour of splendid things I…; `1.40` 0.470 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `adi-162-2` 0.539 [direct]; `anusasana-105-2` 0.531 [direct]
- judge grades (verses then passages): [1, 0, 1, 1, 2]

### q13 (en) — HIT

> I found out I was adopted and my birth mother now wants to meet me. I feel angry and confused.

- rewritten: I found out I was adopted and my birth mother now wants to meet me. I feel angry and confused.
- themes: -  (expected: abandonment, identity, family, anger)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `bhima-spares-jayadratha` 0.0313
- verses: `4.4` 0.510 [direct] Arjuna said: Later was Thy birth, earlier the birth of Vivasvân; how t…; `2.7` 0.508 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `4.9` 0.497 [direct] He who thus knoweth My divine birth and action, in its essence, having…
- passages: `asramavasika-30-1` 0.540 [direct]; `udyoga-147-5` 0.500 [direct]
- judge grades (verses then passages): [0, 2, 0, 1, 1]

### q14 (en) 

> Everyone at college mocks me because I come from a village and my English is weak.

- rewritten: Everyone at college mocks me because I come from a village and my English is weak.
- themes: -  (expected: humiliation, exclusion, self-worth, background)
- expected situation: -
- situations: `duryodhana-maya-palace` 0.0328; `arjuna-yudhishthira-gandiva-conflict` 0.0315
- verses: `1.29` 0.558 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.7` 0.495 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.16` 0.388 [situation:duryodhana-maya-palace] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `karna-45-5` 0.496 [direct]; `karna-40-3` 0.474 [direct]
- judge grades (verses then passages): [0, 2, 1, 0, 0]

### q15 (en) — MISS

> My professor took credit for my research and told me to keep quiet if I want my degree.

- rewritten: My professor took credit for my research and told me to keep quiet if I want my degree.
- themes: -  (expected: exploitation, injustice, mentor, sacrifice)
- expected situation: eklavya-drona-thumb
- situations: `vikarna-protests-draupadi-disrobing` 0.0317; `vidura-truth-dhritarashtra` 0.0305
- verses: `12.16` 0.510 [direct] He who wants nothing, is pure, expert, passionless, untroubled, renoun…; `15.20` 0.504 [direct] Thus by Me this most secret teaching hath been told O sinless one. Thi…; `13.19` 0.483 [direct] Thus the Field, Wisdom and the Object of Wisdom, have been briefly tol…
- passages: `bhishma-123-6` 0.512 [direct]; `santi-9-1` 0.503 [direct]
- judge grades (verses then passages): [0, 0, 0, 1, 0]

### q16 (en) — MISS

> My parents always defend my younger brother no matter what he does wrong.

- rewritten: My parents always defend my younger brother no matter what he does wrong.
- themes: -  (expected: favoritism, family, injustice, resentment)
- expected situation: dhritarashtra-lac-house
- situations: `yayati-sons-refuse-youth` 0.0328; `kunti-reveals-karna` 0.0323
- verses: `18.56` 0.517 [direct] Though ever performing all actions, taking refuge in Me, by My grace h…; `9.14` 0.509 [direct] Always magnifying Me, strenuous, firm in vows, prostrating themselves …; `1.34` 0.471 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…
- passages: `anusasana-105-2` 0.553 [direct]; `anusasana-105-1` 0.541 [direct]
- judge grades (verses then passages): [0, 0, 1, 1, 1]

### q17 (en) — HIT

> I won the lawsuit against my old business partner but I feel empty instead of happy.

- rewritten: I won the lawsuit against my old business partner but I feel empty instead of happy.
- themes: -  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0320; `draupadi-doubts-yudhishthira-dharma` 0.0318
- verses: `18.66` 0.530 [direct] Abandoning all duties come unto Me alone for shelter; sorrow not, I wi…; `16.13` 0.501 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…; `2.8` 0.497 [situation:yudhishthira-grief-after-victory] For I see not that it would drive away this anguish that withers up my…
- passages: `santi-177-5` 0.549 [direct]; `santi-25-3` 0.497 [direct]
- judge grades (verses then passages): [0, 2, 2, 2, 1]

### q18 (en) 

> I get so angry that I say things I regret. Yesterday I screamed at my kids.

- rewritten: I get so angry that I say things I regret. Yesterday I screamed at my kids.
- themes: -  (expected: anger, regret, self-control, family)
- expected situation: -
- situations: `bhima-spares-jayadratha` 0.0308; `bhima-vows-revenge` 0.0304
- verses: `16.18` 0.591 [direct] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `1.29` 0.570 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.34` 0.474 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-146-3` 0.549 [direct]; `vana-29-1` 0.544 [direct]
- judge grades (verses then passages): [1, 0, 0, 1, 2]

### q19 (en) — MISS

> My husband has a serious illness and the doctors have given up, but I refuse to give up on him.

- rewritten: My husband has a serious illness and the doctors have given up, but I refuse to give up on him.
- themes: -  (expected: devotion, death, perseverance, love)
- expected situation: savitri-satyavan
- situations: `yayati-sons-refuse-youth` 0.0323; `karna-refuses-bhishma-command` 0.0318
- verses: `1.29` 0.547 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.3` 0.484 [situation:karna-refuses-bhishma-command] Yield not to impotence, O Partha! it doth not befit thee. Shake off th…; `11.8` 0.459 [direct] But verily thou art not able to behold Me with these thine eyes; the d…
- passages: `vana-231-4` 0.531 [direct]; `vana-65-6` 0.530 [direct]
- judge grades (verses then passages): [0, 2, 0, 1, 1]

### q20 (en) — HIT

> I've been unemployed for two years. Every rejection makes me feel more worthless, but I keep going.

- rewritten: I've been unemployed for two years. Every rejection makes me feel more worthless, but I keep going.
- themes: -  (expected: patience, setback, self-worth, perseverance)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0312; `amba-vow-against-bhishma` 0.0306
- verses: `18.57` 0.531 [direct] Renouncing mentally all works in Me, intent on Me, resorting to the yo…; `1.29` 0.523 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `16.10` 0.433 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …
- passages: `santi-179-4` 0.488 [direct]; `sauptika-2-3` 0.488 [direct]
- judge grades (verses then passages): [1, 0, 0, 2, 1]

### q21 (en) 

> My team leader keeps making terrible decisions and I'm expected to support him in public.

- rewritten: My team leader keeps making terrible decisions and I'm expected to support him in public.
- themes: -  (expected: loyalty, duty, leadership, integrity)
- expected situation: -
- situations: `karna-refuses-bhishma-command` 0.0313; `vidura-truth-dhritarashtra` 0.0308
- verses: `1.29` 0.556 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.7` 0.537 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `2.3` 0.481 [situation:karna-refuses-bhishma-command] Yield not to impotence, O Partha! it doth not befit thee. Shake off th…
- passages: `udyoga-136-1` 0.522 [direct]; `udyoga-169-3` 0.502 [situation:karna-refuses-bhishma-command]
- judge grades (verses then passages): [0, 1, 1, 2, 0]

### q22 (en) — HIT

> I'm 70 and my children are settled. I want to let go of everything but I'm afraid.

- rewritten: I'm 70 and my children are settled. I want to let go of everything but I'm afraid.
- themes: -  (expected: renunciation, letting go, death, fear)
- expected situation: pandavas-final-journey-renunciation
- situations: `pandavas-final-journey-renunciation` 0.0323; `kunti-reveals-karna` 0.0306
- verses: `18.66` 0.554 [direct] Abandoning all duties come unto Me alone for shelter; sorrow not, I wi…; `11.49` 0.474 [direct] Be not bewildered, be thou not afraid, Because thou hast beheld this a…; `9.21` 0.396 [situation:pandavas-final-journey-renunciation] They, having enjoyed the spacious heaven-world, their holiness withere…
- passages: `santi-177-5` 0.535 [direct]; `adi-159-5` 0.523 [direct]
- judge grades (verses then passages): [2, 1, 0, 2, 1]

### q23 (en) 

> I told my team we would never miss a deadline, and now keeping that promise means everyone burns out.

- rewritten: I told my team we would never miss a deadline, and now keeping that promise means everyone burns out.
- themes: -  (expected: vow, pride, duty)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0325; `arjuna-jayadratha-vow-sunset` 0.0323
- verses: `1.30` 0.545 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `9.31` 0.505 [direct] Speedily he becometh dutiful and goeth to eternal peace; O Kaunteya, k…; `3.5` 0.503 [direct] Nor can anyone, even for an instant, remain really actionless; for hel…
- passages: `vana-34-3` 0.530 [direct]; `santi-147-1` 0.493 [direct]
- judge grades (verses then passages): [0, 0, 1, 2, 1]

### q24 (en) — MISS

> My cousin is always compared with me and the family celebrates everything he does.

- rewritten: My cousin is always compared with me and the family celebrates everything he does.
- themes: -  (expected: envy, rivalry, family, comparison)
- expected situation: duryodhana-maya-palace
- situations: `eklavya-drona-thumb` 0.0303; `yudhishthira-dice-game` 0.0301
- verses: `9.14` 0.570 [direct] Always magnifying Me, strenuous, firm in vows, prostrating themselves …; `6.32` 0.532 [direct] He who, through the likeness of the Self, O Arjuna, seeth equality in …; `6.30` 0.523 [direct] He who seeth Me everywhere, and seeth everything in Me, of him will I …
- passages: `vana-231-4` 0.530 [direct]; `anusasana-141-17` 0.521 [direct]
- judge grades (verses then passages): [0, 2, 0, 0, 2]

### q25 (en) 

> I don't know what I'm supposed to do with my life. Everyone else seems to have a plan.

- rewritten: I don't know what I'm supposed to do with my life. Everyone else seems to have a plan.
- themes: -  (expected: purpose, career, confusion, duty)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0313; `vidura-insomnia-burden-of-knowledge` 0.0313
- verses: `2.7` 0.561 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `11.31` 0.534 [direct] Reveal Thy Self; what awful Form art Thou? I worship Thee! Have mercy,…; `1.30` 0.531 [situation:vidura-insomnia-burden-of-knowledge] Gândîva slips from my hand, and my skin burns all over, I am not able …
- passages: `adi-159-5` 0.589 [direct]; `santi-322-12` 0.576 [direct]
- judge grades (verses then passages): [2, 0, 0, 1, 1]

### q26 (hinglish) — MISS

> Yaar boards ke exam aa rahe hain aur mujhe lagta hai main fail ho jaunga, kuch padha hi nahi jaata

- rewritten: Yaar boards ke exam aa rahe hain aur mujhe lagta hai main fail ho jaunga, kuch padha hi nahi jaata
- themes: -  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-jayadratha-vow-sunset` 0.0313; `amba-vow-against-bhishma` 0.0306
- verses: `1.29` 0.491 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.50` 0.467 [direct] United to the Pure Reason one abandoneth here both good and evil deeds…; `16.10` 0.454 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …
- passages: `udyoga-32-5` 0.475 [direct]; `vana-189-5` 0.455 [direct]
- judge grades (verses then passages): [0, 2, 0, 0, 0]

### q27 (hinglish) 

> Mere papa chahte hain main engineering karu par mera mann art mein hai, ghar mein roz ladai hoti hai

- rewritten: Mere papa chahte hain main engineering karu par mera mann art mein hai, ghar mein roz ladai hoti hai
- themes: -  (expected: career, family, duty, conflict)
- expected situation: -
- situations: `arjuna-yudhishthira-gandiva-conflict` 0.0307; `dhritarashtra-lac-house` 0.0164
- verses: `4.11` 0.476 [direct] However men approach Me, even so do I welcome them, for the path men t…; `18.6` 0.455 [direct] But even these actions should be done leaving aside attachment and fru…; `3.4` 0.383 [direct] Man winneth not freedom from action by abstaining from activity, nor b…
- passages: `vana-32-3` 0.455 [direct]; `anusasana-23-14` 0.453 [direct]
- judge grades (verses then passages): [2, 1, 1, 1, 0]

### q28 (hinglish) — MISS

> Usne mujhe sabke saamne zaleel kiya, main badla lena chahta hoon

- rewritten: Usne mujhe sabke saamne zaleel kiya, main badla lena chahta hoon
- themes: -  (expected: humiliation, revenge, anger)
- expected situation: bhima-vows-revenge
- situations: `uttara-freezes-battle` 0.0164; `shalya-karna-charioteer` 0.0161
- verses: `5.18` 0.441 [direct] Sages look equally on a Brâhmana adorned with learning and humility, a…; `9.18` 0.439 [direct] The Path, Husband, Lord, Witness, Abode, Shelter, Lover, Origin, Disso…; `18.6` 0.431 [direct] But even these actions should be done leaving aside attachment and fru…
- passages: `santi-185-2` 0.462 [direct]; `udyoga-46-1` 0.451 [direct]
- judge grades (verses then passages): [0, 0, 1, 0, 0]

### q29 (hinglish) 

> Breakup ke baad se neend nahi aati, har cheez mein uski yaad aati hai

- rewritten: Breakup ke baad se neend nahi aati, har cheez mein uski yaad aati hai
- themes: -  (expected: grief, loss, attachment, loneliness)
- expected situation: -
- situations: `yudhishthira-grief-after-victory` 0.0164; `nala-damayanti-teaches-patience` 0.0161
- verses: `1.29` 0.522 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `18.58` 0.495 [direct] Thinking on Me, thou shalt overcome all obstacles by My grace: but if …; `12.8` 0.493 [direct] Place thy mind in me, into Me let thy Reason enter; then without doubt…
- passages: `santi-177-5` 0.444 [direct]; `vana-65-6` 0.430 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [0, 1, 2, 2, 1]

### q30 (hinglish) 

> Mera dost galat kaam kar raha hai par usne mushkil time mein mera saath diya tha, ab kya karu

- rewritten: Mera dost galat kaam kar raha hai par usne mushkil time mein mera saath diya tha, ab kya karu
- themes: -  (expected: loyalty, friendship, duty, truth)
- expected situation: -
- situations: `bhima-spares-jayadratha` 0.0299; `yudhishthira-dice-game` 0.0295
- verses: `4.11` 0.504 [direct] However men approach Me, even so do I welcome them, for the path men t…; `16.13` 0.495 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…; `10.36` 0.426 [situation:yudhishthira-dice-game] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `karna-47-3` 0.492 [direct]; `santi-224-5` 0.469 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 0]

### q31 (hinglish) 

> Office mein sab mujhse aage nikal gaye, mujhe bahut jalan hoti hai

- rewritten: Office mein sab mujhse aage nikal gaye, mujhe bahut jalan hoti hai
- themes: -  (expected: envy, career, rivalry, comparison)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0323; `pandavas-mendicants-in-ekachakra` 0.0164
- verses: `4.11` 0.444 [direct] However men approach Me, even so do I welcome them, for the path men t…; `9.10` 0.440 [direct] Under Me as supervisor, Nature sends forth the moving and unmoving: be…; `1.29` 0.438 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…
- passages: `santi-326-4` 0.461 [direct]; `bhishma-7-3` 0.442 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 0]

### q32 (hinglish) — MISS

> Maine jhooth bola taaki meri behen ki shaadi ho jaye, ab guilt se mar raha hoon

- rewritten: Maine jhooth bola taaki meri behen ki shaadi ho jaye, ab guilt se mar raha hoon
- themes: -  (expected: deception, guilt, family, truth)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `yudhishthira-grief-after-victory` 0.0318; `parashurama-kills-mother` 0.0290
- verses: `9.30` 0.479 [direct] Even if the most sinful worship Me, with un divided heart, he too must…; `16.18` 0.475 [direct] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `1.38` 0.418 [direct] Although these, with intelligence overpowered by greed, see no guilt i…
- passages: `drona-73-4` 0.457 [direct]; `santi-34-4` 0.448 [direct]
- judge grades (verses then passages): [0, 0, 1, 1, 0]

### q33 (hinglish) 

> Bahut gussa aata hai, chhoti chhoti baat pe sab pe chilla deta hoon

- rewritten: Bahut gussa aata hai, chhoti chhoti baat pe sab pe chilla deta hoon
- themes: -  (expected: anger, self-control, regret)
- expected situation: -
- situations: `pandavas-mendicants-in-ekachakra` 0.0164; `shakuntala-rejected-dushyanta` 0.0161
- verses: `2.30` 0.531 [direct] This dweller in the body of everyone is ever invulnerable, O Bhârata; …; `2.25` 0.490 [direct] Unmanifest, unthinkable, immutable, he is called; therefore knowing hi…; `2.14` 0.486 [direct] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…
- passages: `aswamedha-28-1` 0.488 [direct]; `vana-196-4` 0.478 [direct]
- judge grades (verses then passages): [0, 0, 1, 2, 0]

### q34 (hi) 

> मेरे पिताजी का देहांत हो गया है और मैं खुद को संभाल नहीं पा रहा हूँ

- rewritten: मेरे पिताजी का देहांत हो गया है और मैं खुद को संभाल नहीं पा रहा हूँ
- themes: -  (expected: grief, loss, death)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0164; `yayati-sons-refuse-youth` 0.0161
- verses: `1.29` 0.583 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `1.30` 0.567 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `2.8` 0.545 [direct] For I see not that it would drive away this anguish that withers up my…
- passages: `vana-295-11` 0.574 [direct]; `vana-112-3` 0.564 [direct]
- judge grades (verses then passages): [0, 0, 1, 1, 0]

### q35 (hi) — MISS

> मेरे भाई को हमेशा ज़्यादा प्यार मिलता है, मुझे उससे जलन होती है

- rewritten: मेरे भाई को हमेशा ज़्यादा प्यार मिलता है, मुझे उससे जलन होती है
- themes: -  (expected: envy, family, favoritism, sibling rivalry)
- expected situation: duryodhana-maya-palace
- situations: `karna-envy-arjuna-tournament` 0.0164; `draupadi-jealous-subhadra-arrival` 0.0161
- verses: `7.17` 0.532 [direct] Of these the wise, constantly harmonised, worshipping the One, is the …; `12.14` 0.532 [direct] Ever content, harmonious, with the self-controlled, resolute, with min…; `10.8` 0.529 [direct] I am the Generator of all; all evolves from Me; understanding thus, th…
- passages: `santi-179-4` 0.508 [direct]; `santi-138-15` 0.505 [direct]
- judge grades (verses then passages): [0, 0, 0, 1, 1]

### q36 (hi) 

> मैंने एक वादा किया था जो अब मेरे लिए जाल बन गया है

- rewritten: मैंने एक वादा किया था जो अब मेरे लिए जाल बन गया है
- themes: -  (expected: vow, trap, duty)
- expected situation: -
- situations: `shalya-karna-charioteer` 0.0164; `amba-vow-against-bhishma` 0.0161
- verses: `16.13` 0.607 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…; `4.3` 0.545 [direct] This same ancient yoga hath been to-day declared to thee by Me, for th…; `10.36` 0.542 [direct] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `adi-162-2` 0.526 [direct]; `santi-177-5` 0.506 [direct]
- judge grades (verses then passages): [0, 0, 1, 1, 1]

### q37 (hi) 

> नौकरी छूट गई है, समझ नहीं आता आगे क्या करूँ, बहुत डर लगता है

- rewritten: नौकरी छूट गई है, समझ नहीं आता आगे क्या करूँ, बहुत डर लगता है
- themes: -  (expected: fear, career, uncertainty, setback)
- expected situation: -
- situations: `uttara-freezes-battle` 0.0164; `nala-damayanti-teaches-patience` 0.0161
- verses: `1.30` 0.567 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `1.29` 0.541 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.7` 0.511 [direct] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `santi-111-10` 0.513 [direct]; `adi-159-5` 0.506 [direct]
- judge grades (verses then passages): [0, 0, 2, 2, 1]

### q38 (hi) — HIT

> मेरी सास मुझे सबके सामने ताने मारती है और मेरे पति कुछ नहीं बोलते

- rewritten: मेरी सास मुझे सबके सामने ताने मारती है और मेरे पति कुछ नहीं बोलते
- themes: -  (expected: humiliation, silence, family, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0164; `vikarna-protests-draupadi-disrobing` 0.0161
- verses: `13.11` 0.509 [direct] Unflinching devotion to Me by yoga, without other objects, resort to s…; `1.29` 0.508 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `5.13` 0.495 [direct] Mentally renouncing all actions, the sovereign dweller in the body res…
- passages: `santi-266-4` 0.497 [direct]; `vana-231-4` 0.481 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 1]

### q39 (hi) 

> जिस इंसान ने मेरा दिल तोड़ा, उसे माफ़ करूँ या नहीं?

- rewritten: जिस इंसान ने मेरा दिल तोड़ा, उसे माफ़ करूँ या नहीं?
- themes: -  (expected: forgiveness, betrayal, anger)
- expected situation: -
- situations: `bhima-spares-jayadratha` 0.0164; `yudhishthira-regrets-karna` 0.0161
- verses: `9.30` 0.534 [direct] Even if the most sinful worship Me, with un divided heart, he too must…; `1.29` 0.533 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `2.7` 0.531 [direct] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `vana-28-3` 0.550 [direct]; `santi-177-5` 0.550 [direct]
- judge grades (verses then passages): [0, 0, 1, 2, 1]

### q40 (banglish) — MISS

> Amar boss amake shobar shamne opoman korlo

- rewritten: Amar boss amake shobar shamne opoman korlo
- themes: -  (expected: humiliation, workplace, anger)
- expected situation: draupadi-disrobing-sabha
- situations: `bhima-vows-revenge` 0.0323; `silence-of-elders-udyoga` 0.0323
- verses: `1.41` 0.412 [direct] Owing to predominance of lawlessness, O Krishna, the women of the fami…; `16.18` 0.362 [direct] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `1.29` 0.359 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…
- passages: `vana-223-1` 0.422 [direct]; `anusasana-27-2` 0.419 [direct]
- judge grades (verses then passages): [0, 1, 0, 0, 0]

### q41 (banglish) — MISS

> Porikkhar age bhoy lagche, mone hocche ami kichu parbo na

- rewritten: Porikkhar age bhoy lagche, mone hocche ami kichu parbo na
- themes: -  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `yayati-sons-refuse-youth` 0.0315; `pandavas-mendicants-in-ekachakra` 0.0164
- verses: `1.29` 0.513 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `4.8` 0.454 [direct] For the protection of the good, for the destruction of evil-doers, for…; `9.7` 0.420 [direct] All beings, O Kaunteya, enter my lower nature at the end of a world-ag…
- passages: `shalya-45-8` 0.471 [direct]; `vana-191-1` 0.470 [direct]
- judge grades (verses then passages): [2, 0, 0, 0, 0]

### q42 (banglish) 

> Ma baba chay ami chakri kori, kintu ami nijer business korte chai

- rewritten: Ma baba chay ami chakri kori, kintu ami nijer business korte chai
- themes: -  (expected: career, family, duty)
- expected situation: -
- situations: `shalya-karna-charioteer` 0.0323; `yaksha-prashna` 0.0308
- verses: `7.7` 0.476 [direct] There is naught whatsoever higher than I, O Dhananjaya. All this is th…; `9.27` 0.467 [direct] Whatsoever thou doest, whatsoever thou eatest, whatsoever thou offeres…; `18.43` 0.424 [situation:shalya-karna-charioteer] Prowess, splendour, firmness, dexterity, and also not flying from batt…
- passages: `anusasana-84-3` 0.469 [direct]; `udyoga-25-2` 0.469 [direct]
- judge grades (verses then passages): [0, 1, 1, 0, 0]

### q43 (banglish) 

> Amar bondhu amar pith e chhuri marlo, ami ki korbo bujhte parchi na

- rewritten: Amar bondhu amar pith e chhuri marlo, ami ki korbo bujhte parchi na
- themes: -  (expected: betrayal, friendship, anger, confusion)
- expected situation: -
- situations: `yudhishthira-seeks-blessings-from-elders` 0.0164; `duryodhana-maya-palace` 0.0161
- verses: `1.29` 0.489 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `18.6` 0.482 [direct] But even these actions should be done leaving aside attachment and fru…; `4.11` 0.478 [direct] However men approach Me, even so do I welcome them, for the path men t…
- passages: `virata-48-2` 0.450 [direct]; `vana-112-2` 0.443 [direct]
- judge grades (verses then passages): [0, 1, 0, 0, 0]

### q44 (banglish) 

> Khub eka lage, kotha bolar keu nei

- rewritten: Khub eka lage, kotha bolar keu nei
- themes: -  (expected: loneliness, isolation)
- expected situation: -
- situations: `uttara-freezes-battle` 0.0164; `pandavas-mendicants-in-ekachakra` 0.0161
- verses: `6.43` 0.463 [direct] There he recovereth the characteristics belonging to this former body,…; `9.10` 0.446 [direct] Under Me as supervisor, Nature sends forth the moving and unmoving: be…; `1.13` 0.442 [direct] Then conches and kettledrums, tabors and drums and cowhorns, suddenly …
- passages: `mahaprasthanika-1-6` 0.421 [direct]; `vana-166-2` 0.421 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 0]

### q45 (banglish) — MISS

> Online juar nesha hoye geche, shob taka hariye felechi

- rewritten: Online juar nesha hoye geche, shob taka hariye felechi
- themes: -  (expected: addiction, gambling, loss)
- expected situation: yudhishthira-dice-game
- situations: `eklavya-drona-thumb` 0.0164; `yudhishthira-ashwatthama-lie` 0.0161
- verses: `11.7` 0.412 [direct] Here, to-day, behold the whole universe, movable and immovable, standi…; `11.8` 0.410 [direct] But verily thou art not able to behold Me with these thine eyes; the d…; `4.3` 0.409 [direct] This same ancient yoga hath been to-day declared to thee by Me, for th…
- passages: `santi-333-4` 0.408 [direct]; `santi-354-5` 0.394 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 0]

### q46 (bn) 

> আমার বাবা মারা গেছেন, আমি কিছুতেই মেনে নিতে পারছি না

- rewritten: আমার বাবা মারা গেছেন, আমি কিছুতেই মেনে নিতে পারছি না
- themes: -  (expected: grief, loss, death)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0164; `savitri-satyavan` 0.0161
- verses: `2.8` 0.545 [direct] For I see not that it would drive away this anguish that withers up my…; `1.29` 0.523 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `1.30` 0.514 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …
- passages: `vana-295-11` 0.557 [situation:savitri-satyavan]; `karna-8-4` 0.556 [direct]
- judge grades (verses then passages): [0, 1, 1, 0, 2]

### q47 (bn) 

> আমার ছোট ভাইকে সবাই বেশি ভালোবাসে, আমার খুব হিংসা হয়

- rewritten: আমার ছোট ভাইকে সবাই বেশি ভালোবাসে, আমার খুব হিংসা হয়
- themes: -  (expected: envy, family, favoritism)
- expected situation: -
- situations: `bhima-spares-jayadratha` 0.0164; `draupadi-jealous-subhadra-arrival` 0.0161
- verses: `16.18` 0.566 [direct] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `10.8` 0.504 [direct] I am the Generator of all; all evolves from Me; understanding thus, th…; `16.19` 0.494 [direct] These haters, evil, pitiless, vilest among men in the world, I ever th…
- passages: `santi-321-19` 0.541 [direct]; `virata-19-3` 0.535 [direct]
- judge grades (verses then passages): [1, 0, 0, 1, 0]

### q48 (bn) — HIT

> আমি জানি আমার দাদা ভুল করছে, কিন্তু পরিবারের সবাই চুপ করে আছে

- rewritten: আমি জানি আমার দাদা ভুল করছে, কিন্তু পরিবারের সবাই চুপ করে আছে
- themes: -  (expected: silence, injustice, family, complicity)
- expected situation: silence-of-elders-udyoga
- situations: `silence-of-elders-udyoga` 0.0164; `vikarna-protests-draupadi-disrobing` 0.0161
- verses: `3.27` 0.489 [direct] All actions are wrought by the quali ties of nature only. The self, de…; `17.6` 0.477 [direct] Unintelligent, tormenting the aggregated elements forming the body, an…; `1.40` 0.475 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `sabha-66-17` 0.512 [direct]; `asramavasika-3-3` 0.510 [direct]
- judge grades (verses then passages): [0, 0, 2, 2, 2]

### q49 (bn) — MISS

> চাকরির ইন্টারভিউতে বারবার ব্যর্থ হচ্ছি, আর ধৈর্য রাখতে পারছি না

- rewritten: চাকরির ইন্টারভিউতে বারবার ব্যর্থ হচ্ছি, আর ধৈর্য রাখতে পারছি না
- themes: -  (expected: patience, failure, setback, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `arjuna-jayadratha-vow-sunset` 0.0164; `duryodhana-maya-palace` 0.0161
- verses: `1.29` 0.605 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `1.30` 0.549 [direct] Gândîva slips from my hand, and my skin burns all over, I am not able …; `2.7` 0.496 [direct] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `santi-111-10` 0.492 [direct]; `santi-177-2` 0.482 [direct]
- judge grades (verses then passages): [0, 0, 2, 1, 1]

### q50 (bn) 

> রাগের মাথায় এমন কিছু করে ফেলেছি যার জন্য এখন অনুশোচনা হচ্ছে

- rewritten: রাগের মাথায় এমন কিছু করে ফেলেছি যার জন্য এখন অনুশোচনা হচ্ছে
- themes: -  (expected: anger, regret, guilt)
- expected situation: -
- situations: `arjuna-yudhishthira-gandiva-conflict` 0.0164; `karna-envy-arjuna-tournament` 0.0161
- verses: `16.18` 0.604 [direct] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `1.29` 0.571 [direct] My limbs fail and my mouth is parched, my body quivers, and my hair st…; `16.17` 0.561 [direct] Self-glorifying, stubborn, filled with the pride and intoxication of w…
- passages: `santi-266-7` 0.553 [direct]; `santi-146-3` 0.551 [direct]
- judge grades (verses then passages): [2, 0, 0, 1, 2]
