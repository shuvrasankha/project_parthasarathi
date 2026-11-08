# Retrieval eval report

- date: 2026-11-08  set: queries.yaml  queries: 50  runtime: 378s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: False, linked_first: True, fts_text: all
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 64% (n=22) | 67% (n=12) | 67% (n=3) | 0% (n=2) | 67% (n=3) | 100% (n=2) |
| theme overlap: rewrite themes | 72% (n=50) | 65% (n=25) | 80% (n=8) | 64% (n=6) | 81% (n=6) | 93% (n=5) |
| theme overlap: retrieved situations' themes | 58% (n=50) | 64% (n=25) | 57% (n=8) | 56% (n=6) | 38% (n=6) | 58% (n=5) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| verse relevance, LLM judge (0-2 as %) | 44% (n=50) | 45% (n=25) | 52% (n=8) | 47% (n=6) | 33% (n=6) | 30% (n=5) |
| passage relevance, LLM judge (0-2 as %) | 41% (n=50) | 42% (n=25) | 47% (n=8) | 29% (n=6) | 46% (n=6) | 35% (n=5) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- q01 (en): expected `arjuna-kurukshetra-dilemma`, got `uttara-freezes-battle`, `nala-damayanti-teaches-patience`
- q15 (en): expected `eklavya-drona-thumb`, got `vikarna-protests-draupadi-disrobing`, `silence-of-elders-udyoga`
- q16 (en): expected `dhritarashtra-lac-house`, got `yayati-sons-refuse-youth`, `kunti-reveals-karna`
- q24 (en): expected `duryodhana-maya-palace`, got `draupadi-jealous-subhadra-arrival`, `karna-envy-arjuna-tournament`
- q26 (hinglish): expected `arjuna-kurukshetra-dilemma`, got `draupadi-disrobing-sabha`, `nala-damayanti-teaches-patience`
- q35 (hi): expected `duryodhana-maya-palace`, got `draupadi-jealous-subhadra-arrival`, `kunti-reveals-karna`
- q38 (hi): expected `draupadi-disrobing-sabha`, got `vikarna-protests-draupadi-disrobing`, `bhima-vows-revenge`
- q41 (banglish): expected `arjuna-kurukshetra-dilemma`, got `arjuna-jayadratha-vow-sunset`, `nala-damayanti-teaches-patience`

## Per query

### q01 (en) — MISS

> My exams start next week and I can't study at all. I just freeze every time I open the book.

- rewritten: The person feels unable to study for upcoming exams, freezing every time they open the book and fearing they will fail.
- themes: fear of failure, exams, paralysis, fear, despair  (expected: fear of failure, anxiety, paralysis, duty)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `uttara-freezes-battle` 0.0325; `nala-damayanti-teaches-patience` 0.0325
- verses: `7.27` 0.539 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `2.3` 0.499 [situation:uttara-freezes-battle] Yield not to impotence, O Partha! it doth not befit thee. Shake off th…; `2.14` 0.468 [situation:uttara-freezes-battle] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…
- passages: `vana-67-3` 0.463 [situation:nala-damayanti-teaches-patience]; `virata-38-2` 0.416 [situation:uttara-freezes-battle]
- judge grades (verses then passages): [1, 2, 1, 0, 1]

### q02 (en) 

> My girlfriend broke up with me after four years and I don't know who I am without her.

- rewritten: The person feels lost and uncertain about who they are after their girlfriend ended a four‑year relationship.
- themes: heartbreak, identity, self-worth, loss, grief  (expected: grief, loss, attachment, identity)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0325; `gandhari-lament-sons` 0.0315
- verses: `16.16` 0.525 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `7.27` 0.423 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.4` 0.419 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…
- passages: `vana-65-6` 0.522 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.495 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [1, 2, 1, 2, 0]

### q03 (en) 

> My parents want me to become a doctor but I want to study music. I feel like I'm betraying them.

- rewritten: The person feels torn because their parents want them to become a doctor, but they want to study music, and they feel they are betraying their parents.
- themes: betrayal, duty, family, identity, purpose  (expected: career, family, duty, guilt)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0325; `yayati-sons-refuse-youth` 0.0318
- verses: `11.44` 0.474 [situation:yayati-sons-refuse-youth] Therefore I fall before Thee; with my body I worship as it fitting; bl…; `18.48` 0.445 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…; `2.13` 0.411 [situation:yayati-sons-refuse-youth] As the dweller in the body experienceth in the body childhood, youth, …
- passages: `adi-84-2` 0.416 [situation:yayati-sons-refuse-youth]; `udyoga-146-2` 0.394 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [0, 2, 0, 0, 1]

### q04 (en) 

> My mother passed away last month and I keep thinking I should have done more for her.

- rewritten: The person feels deep guilt and grief after their mother passed away last month, believing they should have done more for her.
- themes: guilt, grief, loss, family  (expected: grief, guilt, loss)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `yudhishthira-regrets-karna` 0.0313
- verses: `16.16` 0.520 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `1.28` 0.447 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `1.47` 0.400 [situation:yudhishthira-regrets-karna] Sanjaya said: Having thus spoken on the battle-field, Arjuna sank down…
- passages: `stri-16-5` 0.518 [situation:gandhari-lament-sons]; `stri-27-3` 0.432 [situation:yudhishthira-regrets-karna]
- judge grades (verses then passages): [1, 0, 1, 0, 1]

### q05 (en) — HIT

> My manager shouted at me in front of the whole team and everyone just stayed quiet.

- rewritten: The person was publicly shouted at by their manager in front of the whole team, and everyone remained silent, leaving them feeling humiliated and upset.
- themes: humiliation, anger, fear, self-worth  (expected: humiliation, anger, injustice, silence)
- expected situation: draupadi-disrobing-sabha
- situations: `vikarna-protests-draupadi-disrobing` 0.0325; `draupadi-disrobing-sabha` 0.0325
- verses: `2.34` 0.519 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `1.28` 0.480 [situation:vikarna-protests-draupadi-disrobing] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `17.6` 0.467 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…
- passages: `sabha-71-2` 0.526 [situation:draupadi-disrobing-sabha]; `santi-134-2` 0.543 [direct]
- judge grades (verses then passages): [1, 0, 0, 1, 1]

### q06 (en) — HIT

> My best friend got the promotion I worked for and I can't stop feeling bitter about it.

- rewritten: The person feels bitter because their best friend received a promotion they had worked for, leading to feelings of envy and resentment.
- themes: envy, rivalry, anger, self-worth, pride  (expected: envy, rivalry, resentment)
- expected situation: karna-envy-arjuna-tournament
- situations: `draupadi-jealous-subhadra-arrival` 0.0325; `karna-envy-arjuna-tournament` 0.0323
- verses: `18.34` 0.477 [situation:draupadi-jealous-subhadra-arrival] But the firmness, O Arjuna, by which, from attachment desirous of frui…; `2.45` 0.409 [situation:draupadi-jealous-subhadra-arrival] The Vedas deal with the three attributes; be thou above these three at…; `3.36` 0.399 [situation:draupadi-jealous-subhadra-arrival] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `adi-137-2` 0.445 [situation:karna-envy-arjuna-tournament]; `adi-223-1` 0.398 [situation:draupadi-jealous-subhadra-arrival]
- judge grades (verses then passages): [2, 1, 1, 0, 0]

### q07 (en) 

> I moved to a new city and I have nobody to talk to. Weekends are the worst.

- rewritten: The person has moved to a new city and feels isolated, having no one to talk to, making weekends especially difficult.
- themes: loneliness, despair  (expected: loneliness, isolation)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0323; `pandavas-final-journey-renunciation` 0.0318
- verses: `8.6` 0.500 [situation:pandavas-final-journey-renunciation] Whosoever at the end abandoneth the body, thinking upon any being, to …; `7.27` 0.492 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `9.21` 0.428 [situation:pandavas-final-journey-renunciation] They, having enjoyed the spacious heaven-world, their holiness withere…
- passages: `vana-67-3` 0.528 [situation:nala-damayanti-teaches-patience]; `mahaprasthanika-3-6` 0.392 [situation:pandavas-final-journey-renunciation]
- judge grades (verses then passages): [0, 1, 0, 2, 1]

### q08 (en) 

> I lied to my wife about money and now the lie has become so big I can't take it back.

- rewritten: The person lied to their spouse about money, and the deception has grown so large that they feel unable to retract it, causing them guilt and fear.
- themes: guilt, fear, deception, betrayal  (expected: guilt, deception, truth, marriage)
- expected situation: -
- situations: `yudhishthira-ashwatthama-lie` 0.0318; `bhima-vows-revenge` 0.0313
- verses: `2.34` 0.594 [situation:yudhishthira-ashwatthama-lie] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `18.45` 0.507 [situation:yudhishthira-ashwatthama-lie] Man reacheth perfection by each being intent on his own duty. Listen t…; `3.36` 0.490 [situation:bhima-vows-revenge] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `sabha-70-2` 0.471 [situation:bhima-vows-revenge]; `drona-191-5` 0.426 [situation:yudhishthira-ashwatthama-lie]
- judge grades (verses then passages): [1, 0, 2, 0, 2]

### q09 (en) — HIT

> I lost all my savings on crypto trading and I keep betting more to win it back.

- rewritten: The person lost all their savings on crypto trading and keeps betting more to try to win it back, feeling trapped and anxious.
- themes: loss, addiction, fear, guilt, despair  (expected: addiction, gambling, loss, recklessness)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `nala-damayanti-teaches-patience` 0.0320
- verses: `16.11` 0.603 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `16.15` 0.537 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …; `10.36` 0.506 [situation:yudhishthira-dice-game] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `vana-65-6` 0.524 [situation:nala-damayanti-teaches-patience]; `sabha-58-2` 0.506 [situation:yudhishthira-dice-game]
- judge grades (verses then passages): [1, 2, 1, 1, 2]

### q10 (en) 

> My friend is doing something clearly unethical at work but he helped me get this job. Should I report him?

- rewritten: The person is uncertain whether to report a coworker who is acting unethically because that coworker helped them obtain their job, and they feel conflicted about loyalty, duty, and doing the right thing.
- themes: integrity, loyalty, duty, fear, guilt  (expected: loyalty, truth, duty, friendship)
- expected situation: -
- situations: `yudhishthira-ashwatthama-lie` 0.0325; `parashurama-kills-mother` 0.0325
- verses: `3.35` 0.635 [situation:parashurama-kills-mother] Better one's own duty, though destitute of merit, than the duty of ano…; `18.45` 0.541 [situation:yudhishthira-ashwatthama-lie] Man reacheth perfection by each being intent on his own duty. Listen t…; `2.34` 0.450 [situation:yudhishthira-ashwatthama-lie] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `drona-191-5` 0.409 [situation:yudhishthira-ashwatthama-lie]; `santi-260-1` 0.591 [direct]
- judge grades (verses then passages): [2, 2, 1, 0, 2]

### q11 (en) 

> I promised my dying father I'd take over his shop, but I hate it and it's ruining my life.

- rewritten: The person promised their dying father to take over the family shop, but now hates the work and feels it is ruining their life.
- themes: duty, family, despair, purpose, self-worth  (expected: vow, duty, family, career)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0323; `kunti-reveals-karna` 0.0313
- verses: `16.10` 0.614 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `18.48` 0.484 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…; `3.36` 0.455 [situation:amba-vow-against-bhishma] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `udyoga-178-1` 0.471 [situation:amba-vow-against-bhishma]; `udyoga-146-2` 0.453 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [1, 2, 1, 0, 1]

### q12 (en) 

> My brother cheated me out of my share of the family property. I want revenge.

- rewritten: The person feels cheated out of their share of the family property by their brother and wants revenge.
- themes: betrayal, revenge, anger, injustice, family  (expected: revenge, betrayal, family, anger, injustice)
- expected situation: -
- situations: `bhima-spares-jayadratha` 0.0325; `bhima-vows-revenge` 0.0320
- verses: `2.34` 0.523 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `3.36` 0.485 [situation:bhima-vows-revenge] Arjuna said: But dragged on by what does a man commit sin, reluctantly…; `1.36` 0.441 [situation:bhima-spares-jayadratha] Slaying these sons of Dhritarâshtra, what pleasure can be ours, O Janâ…
- passages: `sabha-70-2` 0.470 [situation:bhima-vows-revenge]; `vana-270-3` 0.423 [situation:bhima-spares-jayadratha]
- judge grades (verses then passages): [0, 2, 1, 2, 1]

### q13 (en) — HIT

> I found out I was adopted and my birth mother now wants to meet me. I feel angry and confused.

- rewritten: The person discovered they were adopted and now their birth mother wants to meet them, causing feelings of anger and confusion.
- themes: anger, identity, family  (expected: abandonment, identity, family, anger)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `yudhishthira-regrets-karna` 0.0310
- verses: `1.28` 0.465 [situation:yudhishthira-regrets-karna] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `2.14` 0.442 [situation:kunti-reveals-karna] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…; `18.48` 0.387 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…
- passages: `stri-27-2` 0.413 [situation:yudhishthira-regrets-karna]; `udyoga-146-1` 0.395 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [0, 1, 0, 2, 2]

### q14 (en) 

> Everyone at college mocks me because I come from a village and my English is weak.

- rewritten: The person feels humiliated and isolated because classmates at college mock them for coming from a village and having weak English.
- themes: humiliation, self-worth, identity, loneliness  (expected: humiliation, exclusion, self-worth, background)
- expected situation: -
- situations: `draupadi-disrobing-sabha` 0.0325; `pandavas-mendicants-in-ekachakra` 0.0320
- verses: `17.6` 0.494 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…; `2.34` 0.491 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `7.27` 0.456 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `sabha-68-3` 0.467 [situation:draupadi-disrobing-sabha]; `santi-111-10` 0.550 [direct]
- judge grades (verses then passages): [0, 2, 1, 0, 2]

### q15 (en) — MISS

> My professor took credit for my research and told me to keep quiet if I want my degree.

- rewritten: The person feels betrayed and intimidated after their professor claimed credit for their research and warned them to stay silent if they want to obtain their degree.
- themes: betrayal, injustice, fear, career, humiliation  (expected: exploitation, injustice, mentor, sacrifice)
- expected situation: eklavya-drona-thumb
- situations: `vikarna-protests-draupadi-disrobing` 0.0328; `silence-of-elders-udyoga` 0.0323
- verses: `2.34` 0.547 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `14.13` 0.520 [situation:silence-of-elders-udyoga] Darkness, stagnation and heedlessness and also delusion—these are born…; `14.9` 0.501 [situation:silence-of-elders-udyoga] Harmony attacheth to bliss, Motion to action O Bharata. Inertia, veril…
- passages: `udyoga-131-1` 0.368 [situation:silence-of-elders-udyoga]; `santi-138-21` 0.562 [direct]
- judge grades (verses then passages): [2, 0, 0, 0, 2]

### q16 (en) — MISS

> My parents always defend my younger brother no matter what he does wrong.

- rewritten: The person feels frustrated because their parents always defend their younger brother regardless of his wrongdoing, leaving them feeling overlooked and unfairly treated.
- themes: favoritism, family, injustice  (expected: favoritism, family, injustice, resentment)
- expected situation: dhritarashtra-lac-house
- situations: `yayati-sons-refuse-youth` 0.0325; `kunti-reveals-karna` 0.0325
- verses: `11.44` 0.513 [situation:yayati-sons-refuse-youth] Therefore I fall before Thee; with my body I worship as it fitting; bl…; `2.13` 0.458 [situation:yayati-sons-refuse-youth] As the dweller in the body experienceth in the body childhood, youth, …; `18.48` 0.439 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…
- passages: `udyoga-146-2` 0.499 [situation:kunti-reveals-karna]; `adi-85-2` 0.485 [situation:yayati-sons-refuse-youth]
- judge grades (verses then passages): [0, 0, 1, 0, 0]

### q17 (en) — HIT

> I won the lawsuit against my old business partner but I feel empty instead of happy.

- rewritten: The person won a lawsuit against an old business partner but feels empty instead of happy.
- themes: despair, purpose, identity  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0323; `pandavas-mendicants-in-ekachakra` 0.0320
- verses: `7.27` 0.498 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …; `2.8` 0.474 [situation:yudhishthira-grief-after-victory] For I see not that it would drive away this anguish that withers up my…; `1.32` 0.461 [situation:yudhishthira-grief-after-victory] For I desire not victory, O Krishna, nor kingdom, nor pleasures; what …
- passages: `stri-15-1` 0.386 [situation:yudhishthira-grief-after-victory]; `santi-177-5` 0.582 [direct]
- judge grades (verses then passages): [2, 2, 2, 1, 2]

### q18 (en) 

> I get so angry that I say things I regret. Yesterday I screamed at my kids.

- rewritten: The person feels intense anger that leads them to say things they later regret, such as screaming at their children.
- themes: anger, guilt, family, self-control  (expected: anger, regret, self-control, family)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0323; `bhima-vows-revenge` 0.0323
- verses: `16.16` 0.521 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `2.34` 0.490 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `1.28` 0.485 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `stri-14-3` 0.470 [situation:gandhari-lament-sons]; `sabha-70-4` 0.416 [situation:bhima-vows-revenge]
- judge grades (verses then passages): [1, 0, 0, 1, 1]

### q19 (en) — HIT

> My husband has a serious illness and the doctors have given up, but I refuse to give up on him.

- rewritten: The person is facing a serious illness of her husband, with doctors having given up, yet she refuses to give up hope for his recovery.
- themes: grief, fear, duty, love, courage  (expected: devotion, death, perseverance, love)
- expected situation: savitri-satyavan
- situations: `savitri-satyavan` 0.0328; `arjuna-kurukshetra-dilemma` 0.0310
- verses: `2.3` 0.508 [situation:savitri-satyavan] Yield not to impotence, O Partha! it doth not befit thee. Shake off th…; `18.45` 0.466 [situation:savitri-satyavan] Man reacheth perfection by each being intent on his own duty. Listen t…; `9.31` 0.451 [situation:savitri-satyavan] Speedily he becometh dutiful and goeth to eternal peace; O Kaunteya, k…
- passages: `vana-295-11` 0.522 [situation:savitri-satyavan]; `bhishma-26-4` 0.470 [situation:arjuna-kurukshetra-dilemma]
- judge grades (verses then passages): [2, 1, 1, 0, 1]

### q20 (en) — HIT

> I've been unemployed for two years. Every rejection makes me feel more worthless, but I keep going.

- rewritten: The person has been unemployed for two years, and each rejection makes them feel increasingly worthless, yet they continue to persevere.
- themes: career, self-worth, fear of failure, despair, identity  (expected: patience, setback, self-worth, perseverance)
- expected situation: nala-damayanti-teaches-patience
- situations: `pandavas-mendicants-in-ekachakra` 0.0320; `nala-damayanti-teaches-patience` 0.0318
- verses: `7.27` 0.497 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …; `18.4` 0.459 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…; `18.1` 0.420 [situation:nala-damayanti-teaches-patience] Arjuna said: I desire, O mighty-armed, to know severally the essence o…
- passages: `vana-52-3` 0.470 [situation:nala-damayanti-teaches-patience]; `santi-218-6` 0.552 [direct]
- judge grades (verses then passages): [0, 0, 0, 0, 0]

### q21 (en) 

> My team leader keeps making terrible decisions and I'm expected to support him in public.

- rewritten: The person feels forced to publicly support their team leader despite believing the leader makes terrible decisions.
- themes: duty, loyalty, injustice, humiliation  (expected: loyalty, duty, leadership, integrity)
- expected situation: -
- situations: `shalya-karna-charioteer` 0.0325; `vikarna-protests-draupadi-disrobing` 0.0320
- verses: `2.7` 0.608 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `2.34` 0.518 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `18.43` 0.497 [situation:shalya-karna-charioteer] Prowess, splendour, firmness, dexterity, and also not flying from batt…
- passages: `karna-32-6` 0.417 [situation:shalya-karna-charioteer]; `santi-56-1` 0.452 [direct]
- judge grades (verses then passages): [0, 2, 1, 1, 1]

### q22 (en) — HIT

> I'm 70 and my children are settled. I want to let go of everything but I'm afraid.

- rewritten: The person is 70 years old, their children are settled, and they want to let go of everything but feel afraid.
- themes: fear, renunciation, attachment, purpose, identity  (expected: renunciation, letting go, death, fear)
- expected situation: pandavas-final-journey-renunciation
- situations: `pandavas-final-journey-renunciation` 0.0328; `pandavas-mendicants-in-ekachakra` 0.0317
- verses: `8.6` 0.501 [situation:pandavas-final-journey-renunciation] Whosoever at the end abandoneth the body, thinking upon any being, to …; `9.21` 0.484 [situation:pandavas-final-journey-renunciation] They, having enjoyed the spacious heaven-world, their holiness withere…; `7.27` 0.464 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `mahaprasthanika-3-2` 0.441 [situation:pandavas-final-journey-renunciation]; `santi-177-5` 0.592 [direct]
- judge grades (verses then passages): [1, 0, 1, 0, 2]

### q23 (en) 

> I told my team we would never miss a deadline, and now keeping that promise means everyone burns out.

- rewritten: The person promised their team they would never miss a deadline, and now feels compelled to keep that promise even though it is causing the team to become exhausted and burnt out.
- themes: duty, guilt, fear, career, leadership  (expected: vow, pride, duty)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0325; `shalya-karna-charioteer` 0.0320
- verses: `16.10` 0.615 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.7` 0.566 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `18.43` 0.513 [situation:shalya-karna-charioteer] Prowess, splendour, firmness, dexterity, and also not flying from batt…
- passages: `udyoga-179-6` 0.443 [situation:amba-vow-against-bhishma]; `karna-32-5` 0.411 [situation:shalya-karna-charioteer]
- judge grades (verses then passages): [1, 2, 1, 0, 0]

### q24 (en) — MISS

> My cousin is always compared with me and the family celebrates everything he does.

- rewritten: The person feels overlooked because their cousin is constantly compared to them and celebrated by the family, causing feelings of envy, rivalry, and humiliation.
- themes: envy, rivalry, humiliation, family, self-worth  (expected: envy, rivalry, family, comparison)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.0325; `karna-envy-arjuna-tournament` 0.0320
- verses: `2.45` 0.476 [situation:draupadi-jealous-subhadra-arrival] The Vedas deal with the three attributes; be thou above these three at…; `18.34` 0.460 [situation:draupadi-jealous-subhadra-arrival] But the firmness, O Arjuna, by which, from attachment desirous of frui…; `3.36` 0.414 [situation:draupadi-jealous-subhadra-arrival] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `adi-137-2` 0.458 [situation:karna-envy-arjuna-tournament]; `adi-223-9` 0.416 [situation:draupadi-jealous-subhadra-arrival]
- judge grades (verses then passages): [0, 1, 1, 2, 0]

### q25 (en) 

> I don't know what I'm supposed to do with my life. Everyone else seems to have a plan.

- rewritten: The person feels uncertain about their life's direction and worries that others have clear plans while they do not.
- themes: purpose, identity, self-worth, fear, paralysis  (expected: purpose, career, confusion, duty)
- expected situation: -
- situations: `vidura-insomnia-burden-of-knowledge` 0.0318; `pandavas-mendicants-in-ekachakra` 0.0315
- verses: `2.63` 0.543 [situation:vidura-insomnia-burden-of-knowledge] From anger proceedeth delusion; from delusion confused memory; from co…; `7.27` 0.517 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …; `1.30` 0.412 [situation:vidura-insomnia-burden-of-knowledge] Gândîva slips from my hand, and my skin burns all over, I am not able …
- passages: `santi-104-5` 0.584 [direct]; `santi-138-14` 0.574 [direct]
- judge grades (verses then passages): [1, 1, 0, 1, 0]

### q26 (hinglish) — MISS

> Yaar boards ke exam aa rahe hain aur mujhe lagta hai main fail ho jaunga, kuch padha hi nahi jaata

- rewritten: The person feels anxious about the upcoming board exams and believes they will fail because they have not studied.
- themes: fear of failure, exams, self-worth, despair, fear  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `draupadi-disrobing-sabha` 0.0315; `nala-damayanti-teaches-patience` 0.0313
- verses: `17.6` 0.513 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…; `7.27` 0.494 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `2.34` 0.475 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `sabha-68-1` 0.480 [situation:draupadi-disrobing-sabha]; `vana-65-3` 0.464 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [0, 1, 0, 0, 0]

### q27 (hinglish) 

> Mere papa chahte hain main engineering karu par mera mann art mein hai, ghar mein roz ladai hoti hai

- rewritten: The person feels torn because their father wants them to study engineering while they are drawn to art, and there are daily fights at home.
- themes: duty, family, career, purpose, identity  (expected: career, family, duty, conflict)
- expected situation: -
- situations: `arjuna-kurukshetra-dilemma` 0.0325; `kunti-reveals-karna` 0.0323
- verses: `18.48` 0.495 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…; `2.14` 0.462 [situation:kunti-reveals-karna] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…; `1.28` 0.443 [situation:arjuna-kurukshetra-dilemma] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `bhishma-25-4` 0.474 [situation:arjuna-kurukshetra-dilemma]; `udyoga-146-2` 0.425 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [2, 1, 0, 1, 0]

### q28 (hinglish) — HIT

> Usne mujhe sabke saamne zaleel kiya, main badla lena chahta hoon

- rewritten: The person was publicly humiliated and now feels a strong desire to take revenge.
- themes: humiliation, revenge, anger  (expected: humiliation, revenge, anger)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.0328; `bhima-kills-duhsasana-drinks-blood` 0.0323
- verses: `2.34` 0.578 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `11.30` 0.508 [situation:bhima-kills-duhsasana-drinks-blood] On every side, all-swallowing, fiery-tongued, Thou lickest up mankind,…; `3.36` 0.485 [situation:bhima-vows-revenge] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `karna-83-3` 0.499 [situation:bhima-kills-duhsasana-drinks-blood]; `sabha-70-2` 0.474 [situation:bhima-vows-revenge]
- judge grades (verses then passages): [2, 0, 2, 1, 1]

### q29 (hinglish) 

> Breakup ke baad se neend nahi aati, har cheez mein uski yaad aati hai

- rewritten: The person cannot sleep after a breakup and is constantly reminded of their ex in everything.
- themes: heartbreak, grief, loss, despair, loneliness  (expected: grief, loss, attachment, loneliness)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0325; `gandhari-lament-sons` 0.0317
- verses: `16.16` 0.574 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `7.27` 0.499 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `1.31` 0.433 [situation:gandhari-lament-sons] And I see adverse omens, O Keshava. Nor do I foresee any advantage fro…
- passages: `vana-65-6` 0.558 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.505 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [1, 2, 0, 1, 1]

### q30 (hinglish) 

> Mera dost galat kaam kar raha hai par usne mushkil time mein mera saath diya tha, ab kya karu

- rewritten: The person is torn between confronting a friend who is engaged in wrongdoing and the gratitude they feel because the friend supported them during a difficult time.
- themes: loyalty, friendship, duty, guilt, integrity  (expected: loyalty, friendship, duty, truth)
- expected situation: -
- situations: `yudhishthira-seeks-blessings-from-elders` 0.0325; `draupadi-doubts-yudhishthira-dharma` 0.0318
- verses: `2.7` 0.639 [situation:yudhishthira-seeks-blessings-from-elders] My heart is weighed down with the vice of faintness; my mind is confus…; `18.3` 0.564 [situation:draupadi-doubts-yudhishthira-dharma] "Action should be relinquished as an evil," declare some thoughtful me…; `2.3` 0.466 [situation:draupadi-doubts-yudhishthira-dharma] Yield not to impotence, O Partha! it doth not befit thee. Shake off th…
- passages: `vana-30-5` 0.551 [situation:draupadi-doubts-yudhishthira-dharma]; `bhishma-43-6` 0.443 [situation:yudhishthira-seeks-blessings-from-elders]
- judge grades (verses then passages): [2, 1, 1, 1, 2]

### q31 (hinglish) 

> Office mein sab mujhse aage nikal gaye, mujhe bahut jalan hoti hai

- rewritten: The person feels intense jealousy because everyone at work has advanced ahead of them.
- themes: envy, rivalry, self-worth, career, humiliation  (expected: envy, career, rivalry, comparison)
- expected situation: -
- situations: `draupadi-jealous-subhadra-arrival` 0.0323; `duryodhana-maya-palace` 0.0310
- verses: `16.16` 0.538 [situation:duryodhana-maya-palace] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `18.34` 0.470 [situation:draupadi-jealous-subhadra-arrival] But the firmness, O Arjuna, by which, from attachment desirous of frui…; `2.45` 0.427 [situation:draupadi-jealous-subhadra-arrival] The Vedas deal with the three attributes; be thou above these three at…
- passages: `sabha-49-3` 0.487 [situation:duryodhana-maya-palace]; `adi-223-7` 0.396 [situation:draupadi-jealous-subhadra-arrival]
- judge grades (verses then passages): [1, 1, 1, 2, 0]

### q32 (hinglish) — HIT

> Maine jhooth bola taaki meri behen ki shaadi ho jaye, ab guilt se mar raha hoon

- rewritten: The person lied to facilitate their sister's marriage and now feels overwhelming guilt.
- themes: guilt, family, duty  (expected: deception, guilt, family, truth)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `parashurama-kills-mother` 0.0318; `yudhishthira-ashwatthama-lie` 0.0317
- verses: `3.35` 0.543 [situation:parashurama-kills-mother] Better one's own duty, though destitute of merit, than the duty of ano…; `2.34` 0.506 [situation:yudhishthira-ashwatthama-lie] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `18.45` 0.489 [situation:yudhishthira-ashwatthama-lie] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `drona-191-5` 0.411 [situation:yudhishthira-ashwatthama-lie]; `anusasana-162-11` 0.569 [direct]
- judge grades (verses then passages): [1, 0, 1, 2, 2]

### q33 (hinglish) 

> Bahut gussa aata hai, chhoti chhoti baat pe sab pe chilla deta hoon

- rewritten: The person feels intense anger and frequently shouts at others over minor issues.
- themes: anger, self-control  (expected: anger, self-control, regret)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `aswatthaman-night-massacre` 0.0308
- verses: `2.63` 0.576 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `16.18` 0.569 [situation:aswatthaman-night-massacre] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `16.16` 0.519 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `sauptika-10-4` 0.466 [situation:aswatthaman-night-massacre]; `stri-16-5` 0.456 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [2, 2, 1, 1, 0]

### q34 (hi) 

> मेरे पिताजी का देहांत हो गया है और मैं खुद को संभाल नहीं पा रहा हूँ

- rewritten: The person is struggling to cope after the death of their father and feels unable to manage their emotions.
- themes: grief, loss, death, family, despair  (expected: grief, loss, death)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0325; `nala-damayanti-teaches-patience` 0.0325
- verses: `16.16` 0.571 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `1.28` 0.487 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `7.27` 0.478 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `vana-65-6` 0.586 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.557 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [0, 1, 1, 1, 2]

### q35 (hi) — MISS

> मेरे भाई को हमेशा ज़्यादा प्यार मिलता है, मुझे उससे जलन होती है

- rewritten: The person feels jealous because their brother always receives more love.
- themes: envy, family, self-worth, loneliness, attachment  (expected: envy, family, favoritism, sibling rivalry)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.0328; `kunti-reveals-karna` 0.0315
- verses: `18.34` 0.486 [situation:draupadi-jealous-subhadra-arrival] But the firmness, O Arjuna, by which, from attachment desirous of frui…; `2.14` 0.460 [situation:kunti-reveals-karna] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…; `2.45` 0.443 [situation:draupadi-jealous-subhadra-arrival] The Vedas deal with the three attributes; be thou above these three at…
- passages: `udyoga-146-2` 0.463 [situation:kunti-reveals-karna]; `adi-223-3` 0.378 [situation:draupadi-jealous-subhadra-arrival]
- judge grades (verses then passages): [1, 1, 1, 0, 0]

### q36 (hi) 

> मैंने एक वादा किया था जो अब मेरे लिए जाल बन गया है

- rewritten: The person made a promise that now feels like a trap, leaving them conflicted and burdened by the obligation. They feel trapped by the commitment and uncertain how to proceed.
- themes: vow, guilt, duty, fear, paralysis  (expected: vow, trap, duty)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0328; `shalya-karna-charioteer` 0.0323
- verses: `16.10` 0.652 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.7` 0.631 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `3.36` 0.527 [situation:amba-vow-against-bhishma] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `udyoga-179-6` 0.474 [situation:amba-vow-against-bhishma]; `karna-32-5` 0.436 [situation:shalya-karna-charioteer]
- judge grades (verses then passages): [0, 2, 2, 0, 0]

### q37 (hi) 

> नौकरी छूट गई है, समझ नहीं आता आगे क्या करूँ, बहुत डर लगता है

- rewritten: The person has lost their job and does not understand what to do next, feeling a great amount of fear.
- themes: fear, loss, career, despair, identity  (expected: fear, career, uncertainty, setback)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0328; `pandavas-mendicants-in-ekachakra` 0.0323
- verses: `7.27` 0.474 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.4` 0.455 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…; `18.1` 0.410 [situation:nala-damayanti-teaches-patience] Arjuna said: I desire, O mighty-armed, to know severally the essence o…
- passages: `vana-65-6` 0.532 [situation:nala-damayanti-teaches-patience]; `santi-111-10` 0.568 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 1]

### q38 (hi) — MISS

> मेरी सास मुझे सबके सामने ताने मारती है और मेरे पति कुछ नहीं बोलते

- rewritten: The person feels humiliated as their mother-in-law publicly scolds them, while their husband remains silent and does not intervene.
- themes: humiliation, family, loyalty, fear  (expected: humiliation, silence, family, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `vikarna-protests-draupadi-disrobing` 0.0323; `bhima-vows-revenge` 0.0320
- verses: `2.34` 0.489 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `1.28` 0.406 [situation:vikarna-protests-draupadi-disrobing] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `3.36` 0.387 [situation:bhima-vows-revenge] Arjuna said: But dragged on by what does a man commit sin, reluctantly…
- passages: `sabha-70-2` 0.449 [situation:bhima-vows-revenge]; `anusasana-38-3` 0.549 [direct]
- judge grades (verses then passages): [2, 1, 1, 2, 0]

### q39 (hi) 

> जिस इंसान ने मेरा दिल तोड़ा, उसे माफ़ करूँ या नहीं?

- rewritten: The person wonders whether to forgive the individual who broke their heart.
- themes: forgiveness, heartbreak, betrayal, love  (expected: forgiveness, betrayal, anger)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0320; `amba-vow-against-bhishma` 0.0305
- verses: `16.10` 0.579 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `3.36` 0.533 [situation:amba-vow-against-bhishma] Arjuna said: But dragged on by what does a man commit sin, reluctantly…; `18.4` 0.519 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…
- passages: `vana-65-6` 0.594 [situation:nala-damayanti-teaches-patience]; `udyoga-179-1` 0.542 [situation:amba-vow-against-bhishma]
- judge grades (verses then passages): [0, 1, 0, 1, 0]

### q40 (banglish) — HIT

> Amar boss amake shobar shamne opoman korlo

- rewritten: The person feels humiliated because their boss insulted them in front of everyone, causing embarrassment and hurt.
- themes: humiliation, anger, self-worth, fear, loneliness  (expected: humiliation, workplace, anger)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0325; `vikarna-protests-draupadi-disrobing` 0.0318
- verses: `2.34` 0.545 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `1.28` 0.502 [situation:vikarna-protests-draupadi-disrobing] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `17.6` 0.498 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…
- passages: `sabha-68-1` 0.503 [situation:draupadi-disrobing-sabha]; `santi-111-10` 0.616 [direct]
- judge grades (verses then passages): [2, 0, 0, 2, 2]

### q41 (banglish) — MISS

> Porikkhar age bhoy lagche, mone hocche ami kichu parbo na

- rewritten: The person feels intense fear before an exam and believes they will not be able to succeed.
- themes: fear, fear of failure, exams  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-jayadratha-vow-sunset` 0.0320; `nala-damayanti-teaches-patience` 0.0313
- verses: `7.27` 0.490 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.9` 0.458 [situation:arjuna-jayadratha-vow-sunset] He who performeth a prescribed action, saying, "it ought to be done," …; `18.4` 0.428 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…
- passages: `vana-65-3` 0.462 [situation:nala-damayanti-teaches-patience]; `drona-76-2` 0.410 [situation:arjuna-jayadratha-vow-sunset]
- judge grades (verses then passages): [0, 1, 0, 0, 0]

### q42 (banglish) 

> Ma baba chay ami chakri kori, kintu ami nijer business korte chai

- rewritten: The person feels torn because their parents want them to take a job, but they themselves want to start their own business.
- themes: duty, career, purpose, identity, self-worth  (expected: career, family, duty)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0325; `yayati-sons-refuse-youth` 0.0315
- verses: `11.44` 0.500 [situation:yayati-sons-refuse-youth] Therefore I fall before Thee; with my body I worship as it fitting; bl…; `18.48` 0.472 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…; `2.14` 0.442 [situation:kunti-reveals-karna] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…
- passages: `adi-85-2` 0.453 [situation:yayati-sons-refuse-youth]; `udyoga-146-1` 0.421 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [0, 2, 1, 0, 1]

### q43 (banglish) 

> Amar bondhu amar pith e chhuri marlo, ami ki korbo bujhte parchi na

- rewritten: The person’s friend stabbed their father and they feel confused and uncertain about what to do.
- themes: betrayal, grief, fear, anger, loss  (expected: betrayal, friendship, anger, confusion)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0325; `yudhishthira-regrets-karna` 0.0315
- verses: `16.16` 0.588 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `1.31` 0.488 [situation:gandhari-lament-sons] And I see adverse omens, O Keshava. Nor do I foresee any advantage fro…; `1.28` 0.469 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `stri-16-5` 0.531 [situation:gandhari-lament-sons]; `stri-27-2` 0.458 [situation:yudhishthira-regrets-karna]
- judge grades (verses then passages): [1, 0, 0, 1, 0]

### q44 (banglish) 

> Khub eka lage, kotha bolar keu nei

- rewritten: The person feels extremely lonely and has no one to talk to.
- themes: loneliness, despair  (expected: loneliness, isolation)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0325; `vikarna-protests-draupadi-disrobing` 0.0312
- verses: `7.27` 0.520 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `2.34` 0.517 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `1.28` 0.468 [situation:vikarna-protests-draupadi-disrobing] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…
- passages: `vana-67-3` 0.545 [situation:nala-damayanti-teaches-patience]; `santi-177-5` 0.568 [direct]
- judge grades (verses then passages): [0, 0, 1, 2, 1]

### q45 (banglish) — HIT

> Online juar nesha hoye geche, shob taka hariye felechi

- rewritten: The person has become addicted to online gambling and has lost all of their money, feeling distressed and worried about the consequences.
- themes: addiction, loss, guilt, fear, despair  (expected: addiction, gambling, loss)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-grief-after-victory` 0.0325; `yudhishthira-dice-game` 0.0320
- verses: `16.11` 0.626 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `16.15` 0.543 [situation:yudhishthira-dice-game] "I am wealthy, well-born; what other is there that is like unto me? I …; `10.36` 0.533 [situation:yudhishthira-dice-game] I am the gambling of the cheat, and the splendour of splendid things I…
- passages: `sabha-58-2` 0.526 [situation:yudhishthira-dice-game]; `stri-15-3` 0.399 [situation:yudhishthira-grief-after-victory]
- judge grades (verses then passages): [2, 0, 2, 2, 0]

### q46 (bn) 

> আমার বাবা মারা গেছেন, আমি কিছুতেই মেনে নিতে পারছি না

- rewritten: The person is unable to accept the death of their father and feels overwhelmed by the loss.
- themes: grief, loss, death, family  (expected: grief, loss, death)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0325; `nala-damayanti-teaches-patience` 0.0323
- verses: `16.16` 0.579 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `1.28` 0.506 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `7.27` 0.481 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `vana-65-6` 0.577 [situation:nala-damayanti-teaches-patience]; `stri-16-5` 0.559 [situation:gandhari-lament-sons]
- judge grades (verses then passages): [0, 1, 1, 1, 2]

### q47 (bn) 

> আমার ছোট ভাইকে সবাই বেশি ভালোবাসে, আমার খুব হিংসা হয়

- rewritten: The person feels intense envy because everyone loves their younger brother more than them.
- themes: envy, family  (expected: envy, family, favoritism)
- expected situation: -
- situations: `draupadi-jealous-subhadra-arrival` 0.0313; `kunti-reveals-karna` 0.0310
- verses: `18.34` 0.450 [situation:draupadi-jealous-subhadra-arrival] But the firmness, O Arjuna, by which, from attachment desirous of frui…; `2.14` 0.420 [situation:kunti-reveals-karna] The contacts of matter, O son of Kuntî, giving cold and heat, pleasure…; `2.45` 0.414 [situation:draupadi-jealous-subhadra-arrival] The Vedas deal with the three attributes; be thou above these three at…
- passages: `udyoga-146-2` 0.450 [situation:kunti-reveals-karna]; `adi-223-3` 0.420 [situation:draupadi-jealous-subhadra-arrival]
- judge grades (verses then passages): [0, 1, 1, 0, 0]

### q48 (bn) — HIT

> আমি জানি আমার দাদা ভুল করছে, কিন্তু পরিবারের সবাই চুপ করে আছে

- rewritten: The person knows their grandfather is doing something wrong, but everyone in the family remains silent.
- themes: family, duty, guilt, silence, injustice  (expected: silence, injustice, family, complicity)
- expected situation: silence-of-elders-udyoga
- situations: `vikarna-protests-draupadi-disrobing` 0.0325; `silence-of-elders-udyoga` 0.0323
- verses: `14.9` 0.489 [situation:silence-of-elders-udyoga] Harmony attacheth to bliss, Motion to action O Bharata. Inertia, veril…; `2.34` 0.468 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `14.13` 0.459 [situation:silence-of-elders-udyoga] Darkness, stagnation and heedlessness and also delusion—these are born…
- passages: `udyoga-131-4` 0.395 [situation:silence-of-elders-udyoga]; `sabha-66-17` 0.552 [direct]
- judge grades (verses then passages): [0, 2, 0, 1, 2]

### q49 (bn) — HIT

> চাকরির ইন্টারভিউতে বারবার ব্যর্থ হচ্ছি, আর ধৈর্য রাখতে পারছি না

- rewritten: The person keeps failing job interviews and feels unable to maintain patience.
- themes: fear of failure, patience, career, self-worth, despair  (expected: patience, failure, setback, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0328; `arjuna-jayadratha-vow-sunset` 0.0304
- verses: `18.4` 0.482 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…; `7.27` 0.472 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …; `18.9` 0.464 [situation:arjuna-jayadratha-vow-sunset] He who performeth a prescribed action, saying, "it ought to be done," …
- passages: `vana-65-3` 0.464 [situation:nala-damayanti-teaches-patience]; `drona-75-4` 0.423 [situation:arjuna-jayadratha-vow-sunset]
- judge grades (verses then passages): [0, 1, 2, 0, 0]

### q50 (bn) 

> রাগের মাথায় এমন কিছু করে ফেলেছি যার জন্য এখন অনুশোচনা হচ্ছে

- rewritten: The person acted in a fit of anger and now feels regret for what they did.
- themes: anger, guilt  (expected: anger, regret, guilt)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0315; `bhima-kills-duhsasana-drinks-blood` 0.0309
- verses: `16.16` 0.556 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `1.28` 0.511 [situation:gandhari-lament-sons] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `1.47` 0.447 [situation:bhima-kills-duhsasana-drinks-blood] Sanjaya said: Having thus spoken on the battle-field, Arjuna sank down…
- passages: `stri-14-3` 0.507 [situation:gandhari-lament-sons]; `karna-83-5` 0.456 [situation:bhima-kills-duhsasana-drinks-blood]
- judge grades (verses then passages): [0, 0, 0, 1, 0]
