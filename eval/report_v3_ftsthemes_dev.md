# Retrieval eval report

- date: 2026-11-08  set: queries.yaml  queries: 50  runtime: 184s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: False, linked_first: False, fts_text: themes
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 55% (n=22) | 58% (n=12) | 33% (n=3) | 50% (n=2) | 67% (n=3) | 50% (n=2) |
| theme overlap: rewrite themes | 72% (n=50) | 65% (n=25) | 80% (n=8) | 64% (n=6) | 81% (n=6) | 93% (n=5) |
| theme overlap: retrieved situations' themes | 66% (n=50) | 67% (n=25) | 54% (n=8) | 78% (n=6) | 71% (n=6) | 58% (n=5) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| verse relevance, LLM judge (0-2 as %) | 57% (n=50) | 61% (n=25) | 60% (n=8) | 44% (n=6) | 58% (n=6) | 43% (n=5) |
| passage relevance, LLM judge (0-2 as %) | 60% (n=50) | 63% (n=25) | 59% (n=8) | 42% (n=6) | 58% (n=6) | 65% (n=5) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- q01 (en): expected `arjuna-kurukshetra-dilemma`, got `nala-damayanti-teaches-patience`, `uttara-freezes-battle`
- q15 (en): expected `eklavya-drona-thumb`, got `draupadi-disrobing-sabha`, `vikarna-protests-draupadi-disrobing`
- q16 (en): expected `dhritarashtra-lac-house`, got `kunti-reveals-karna`, `yayati-sons-refuse-youth`
- q20 (en): expected `nala-damayanti-teaches-patience`, got `pandavas-mendicants-in-ekachakra`, `draupadi-disrobing-sabha`
- q24 (en): expected `duryodhana-maya-palace`, got `draupadi-jealous-subhadra-arrival`, `karna-envy-arjuna-tournament`
- q26 (hinglish): expected `arjuna-kurukshetra-dilemma`, got `draupadi-disrobing-sabha`, `arjuna-jayadratha-vow-sunset`
- q32 (hinglish): expected `yudhishthira-ashwatthama-lie`, got `bhima-vows-revenge`, `yudhishthira-regrets-karna`
- q35 (hi): expected `duryodhana-maya-palace`, got `draupadi-jealous-subhadra-arrival`, `bhima-spares-jayadratha`
- q41 (banglish): expected `arjuna-kurukshetra-dilemma`, got `arjuna-jayadratha-vow-sunset`, `uttara-freezes-battle`
- q49 (bn): expected `nala-damayanti-teaches-patience`, got `arjuna-jayadratha-vow-sunset`, `krishna-peace-mission`

## Per query

### q01 (en) — MISS

> My exams start next week and I can't study at all. I just freeze every time I open the book.

- rewritten: The person feels unable to study for upcoming exams, freezing every time they open the book and fearing they will fail.
- themes: fear of failure, exams, paralysis, fear, despair  (expected: fear of failure, anxiety, paralysis, duty)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `nala-damayanti-teaches-patience` 0.0320; `uttara-freezes-battle` 0.0318
- verses: `9.12` 0.609 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `11.45` 0.561 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `18.35` 0.544 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …
- passages: `santi-322-2` 0.553 [direct]; `aswamedha-42-6` 0.544 [direct]
- judge grades (verses then passages): [1, 1, 1, 2, 0]

### q02 (en) 

> My girlfriend broke up with me after four years and I don't know who I am without her.

- rewritten: The person feels lost and uncertain about who they are after their girlfriend ended a four‑year relationship.
- themes: heartbreak, identity, self-worth, loss, grief  (expected: grief, loss, attachment, identity)
- expected situation: -
- situations: `yudhishthira-regrets-karna` 0.0318; `pandavas-mendicants-in-ekachakra` 0.0318
- verses: `13.10` 0.599 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `4.40` 0.540 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `6.6` 0.519 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-174-3` 0.522 [direct]; `santi-28-4` 0.515 [direct]
- judge grades (verses then passages): [2, 1, 1, 2, 2]

### q03 (en) 

> My parents want me to become a doctor but I want to study music. I feel like I'm betraying them.

- rewritten: The person feels torn because their parents want them to become a doctor, but they want to study music, and they feel they are betraying their parents.
- themes: betrayal, duty, family, identity, purpose  (expected: career, family, duty, guilt)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0325; `yayati-sons-refuse-youth` 0.0312
- verses: `3.35` 0.540 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `1.40` 0.519 [direct] In the destruction of a family the immemorial family traditions perish…; `18.47` 0.495 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `adi-84-2` 0.416 [situation:yayati-sons-refuse-youth]; `udyoga-146-2` 0.394 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [2, 1, 2, 0, 1]

### q04 (en) 

> My mother passed away last month and I keep thinking I should have done more for her.

- rewritten: The person feels deep guilt and grief after their mother passed away last month, believing they should have done more for her.
- themes: guilt, grief, loss, family  (expected: grief, guilt, loss)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0323; `yudhishthira-regrets-karna` 0.0315
- verses: `2.7` 0.562 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `1.40` 0.549 [direct] In the destruction of a family the immemorial family traditions perish…; `17.9` 0.535 [direct] The passionate desire foods that are bitter, sour, saline, over-hot, p…
- passages: `santi-146-3` 0.565 [direct]; `santi-25-3` 0.549 [direct]
- judge grades (verses then passages): [2, 1, 0, 2, 2]

### q05 (en) — HIT

> My manager shouted at me in front of the whole team and everyone just stayed quiet.

- rewritten: The person was publicly shouted at by their manager in front of the whole team, and everyone remained silent, leaving them feeling humiliated and upset.
- themes: humiliation, anger, fear, self-worth  (expected: humiliation, anger, injustice, silence)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0323; `aswatthaman-night-massacre` 0.0315
- verses: `14.25` 0.568 [direct] The same in honour and ignominy, the same to friend and foe, abandonin…; `12.18` 0.558 [direct] Alike to foe and friend, and also in fame and ignominy, alike in cold …; `16.18` 0.548 [situation:aswatthaman-night-massacre] Given over to egoism, power, insolence, lust and wrath, these maliciou…
- passages: `santi-134-2` 0.543 [direct]; `vana-29-1` 0.538 [direct]
- judge grades (verses then passages): [1, 1, 0, 1, 1]

### q06 (en) — HIT

> My best friend got the promotion I worked for and I can't stop feeling bitter about it.

- rewritten: The person feels bitter because their best friend received a promotion they had worked for, leading to feelings of envy and resentment.
- themes: envy, rivalry, anger, self-worth, pride  (expected: envy, rivalry, resentment)
- expected situation: karna-envy-arjuna-tournament
- situations: `draupadi-jealous-subhadra-arrival` 0.0325; `karna-envy-arjuna-tournament` 0.0318
- verses: `6.6` 0.573 [direct] The Self is the friend of the self of him in whom the self by the Self…; `15.5` 0.547 [direct] Without pride and delusion, victorious over the vice of attachment, dw…; `6.5` 0.535 [direct] Let him raise the self by the Self and not let the self become depress…
- passages: `santi-111-10` 0.603 [direct]; `santi-163-2` 0.595 [direct]
- judge grades (verses then passages): [1, 2, 1, 2, 2]

### q07 (en) 

> I moved to a new city and I have nobody to talk to. Weekends are the worst.

- rewritten: The person has moved to a new city and feels isolated, having no one to talk to, making weekends especially difficult.
- themes: loneliness, despair  (expected: loneliness, isolation)
- expected situation: -
- situations: `duryodhana-hides-lake` 0.0323; `yudhishthira-grief-after-victory` 0.0320
- verses: `13.10` 0.622 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `18.52` 0.611 [direct] Dwelling in solitude, abstemious, speech, body and mind subdued, const…; `13.11` 0.554 [situation:duryodhana-hides-lake] Unflinching devotion to Me by yoga, without other objects, resort to s…
- passages: `santi-177-5` 0.571 [direct]; `santi-175-3` 0.546 [direct]
- judge grades (verses then passages): [1, 0, 0, 1, 0]

### q08 (en) 

> I lied to my wife about money and now the lie has become so big I can't take it back.

- rewritten: The person lied to their spouse about money, and the deception has grown so large that they feel unable to retract it, causing them guilt and fear.
- themes: guilt, fear, deception, betrayal  (expected: guilt, deception, truth, marriage)
- expected situation: -
- situations: `shakuntala-rejected-dushyanta` 0.0318; `aswatthaman-night-massacre` 0.0306
- verses: `16.10` 0.651 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.12` 0.612 [direct] Held in bondage by a hundred ties of expectation, given over to lust a…; `2.63` 0.586 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `santi-259-3` 0.623 [direct]; `anusasana-162-11` 0.618 [direct]
- judge grades (verses then passages): [1, 1, 1, 1, 2]

### q09 (en) — HIT

> I lost all my savings on crypto trading and I keep betting more to win it back.

- rewritten: The person lost all their savings on crypto trading and keeps betting more to try to win it back, feeling trapped and anxious.
- themes: loss, addiction, fear, guilt, despair  (expected: addiction, gambling, loss, recklessness)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0325; `yudhishthira-grief-after-victory` 0.0320
- verses: `16.12` 0.605 [direct] Held in bondage by a hundred ties of expectation, given over to lust a…; `16.11` 0.603 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `16.16` 0.598 [direct] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-104-5` 0.582 [direct]; `santi-177-3` 0.574 [direct]
- judge grades (verses then passages): [2, 1, 2, 2, 2]

### q10 (en) 

> My friend is doing something clearly unethical at work but he helped me get this job. Should I report him?

- rewritten: The person is uncertain whether to report a coworker who is acting unethically because that coworker helped them obtain their job, and they feel conflicted about loyalty, duty, and doing the right thing.
- themes: integrity, loyalty, duty, fear, guilt  (expected: loyalty, truth, duty, friendship)
- expected situation: -
- situations: `yudhishthira-ashwatthama-lie` 0.0323; `shalya-karna-charioteer` 0.0315
- verses: `3.35` 0.635 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `2.7` 0.611 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `4.17` 0.604 [direct] It is needful to discriminate action, to discriminate unlawful action,…
- passages: `santi-260-1` 0.591 [direct]; `santi-132-3` 0.585 [direct]
- judge grades (verses then passages): [2, 2, 2, 2, 2]

### q11 (en) 

> I promised my dying father I'd take over his shop, but I hate it and it's ruining my life.

- rewritten: The person promised their dying father to take over the family shop, but now hates the work and feels it is ruining their life.
- themes: duty, family, despair, purpose, self-worth  (expected: vow, duty, family, career)
- expected situation: -
- situations: `yayati-sons-refuse-youth` 0.0320; `kunti-reveals-karna` 0.0315
- verses: `3.35` 0.657 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `1.40` 0.594 [direct] In the destruction of a family the immemorial family traditions perish…; `18.47` 0.562 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-177-5` 0.574 [direct]; `santi-277-2` 0.574 [direct]
- judge grades (verses then passages): [2, 1, 2, 1, 1]

### q12 (en) 

> My brother cheated me out of my share of the family property. I want revenge.

- rewritten: The person feels cheated out of their share of the family property by their brother and wants revenge.
- themes: betrayal, revenge, anger, injustice, family  (expected: revenge, betrayal, family, anger, injustice)
- expected situation: -
- situations: `bhima-vows-revenge` 0.0325; `aswatthaman-night-massacre` 0.0318
- verses: `2.62` 0.627 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `1.40` 0.619 [direct] In the destruction of a family the immemorial family traditions perish…; `16.12` 0.618 [direct] Held in bondage by a hundred ties of expectation, given over to lust a…
- passages: `santi-259-2` 0.655 [direct]; `adi-162-2` 0.576 [direct]
- judge grades (verses then passages): [1, 1, 2, 2, 1]

### q13 (en) — HIT

> I found out I was adopted and my birth mother now wants to meet me. I feel angry and confused.

- rewritten: The person discovered they were adopted and now their birth mother wants to meet them, causing feelings of anger and confusion.
- themes: anger, identity, family  (expected: abandonment, identity, family, anger)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0325; `gandhari-lament-sons` 0.0318
- verses: `2.62` 0.570 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.527 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `1.40` 0.522 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `anusasana-49-1` 0.535 [direct]; `santi-174-3` 0.532 [direct]
- judge grades (verses then passages): [2, 2, 0, 0, 1]

### q14 (en) 

> Everyone at college mocks me because I come from a village and my English is weak.

- rewritten: The person feels humiliated and isolated because classmates at college mock them for coming from a village and having weak English.
- themes: humiliation, self-worth, identity, loneliness  (expected: humiliation, exclusion, self-worth, background)
- expected situation: -
- situations: `draupadi-disrobing-sabha` 0.0325; `pandavas-mendicants-in-ekachakra` 0.0317
- verses: `2.7` 0.573 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `3.27` 0.547 [direct] All actions are wrought by the quali ties of nature only. The self, de…; `17.6` 0.494 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…
- passages: `santi-111-10` 0.550 [direct]; `anusasana-124-4` 0.541 [direct]
- judge grades (verses then passages): [1, 0, 0, 2, 1]

### q15 (en) — MISS

> My professor took credit for my research and told me to keep quiet if I want my degree.

- rewritten: The person feels betrayed and intimidated after their professor claimed credit for their research and warned them to stay silent if they want to obtain their degree.
- themes: betrayal, injustice, fear, career, humiliation  (expected: exploitation, injustice, mentor, sacrifice)
- expected situation: eklavya-drona-thumb
- situations: `draupadi-disrobing-sabha` 0.0323; `vikarna-protests-draupadi-disrobing` 0.0313
- verses: `2.7` 0.614 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `2.34` 0.547 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `18.8` 0.544 [direct] He who relinquisheth an action from fear of physical suffering, saying…
- passages: `santi-138-21` 0.562 [direct]; `sabha-66-17` 0.508 [situation:draupadi-disrobing-sabha]
- judge grades (verses then passages): [1, 2, 0, 2, 2]

### q16 (en) — MISS

> My parents always defend my younger brother no matter what he does wrong.

- rewritten: The person feels frustrated because their parents always defend their younger brother regardless of his wrongdoing, leaving them feeling overlooked and unfairly treated.
- themes: favoritism, family, injustice  (expected: favoritism, family, injustice, resentment)
- expected situation: dhritarashtra-lac-house
- situations: `kunti-reveals-karna` 0.0320; `yayati-sons-refuse-youth` 0.0311
- verses: `16.10` 0.576 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.7` 0.572 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `1.40` 0.567 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-176-2` 0.575 [direct]; `santi-321-19` 0.572 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 1]

### q17 (en) — HIT

> I won the lawsuit against my old business partner but I feel empty instead of happy.

- rewritten: The person won a lawsuit against an old business partner but feels empty instead of happy.
- themes: despair, purpose, identity  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0323; `pandavas-mendicants-in-ekachakra` 0.0323
- verses: `13.10` 0.573 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `18.59` 0.527 [direct] Entrenched in egoism, thou thinkest, "I will not fight;" to no purpose…; `16.13` 0.524 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…
- passages: `santi-177-5` 0.582 [direct]; `santi-177-4` 0.566 [direct]
- judge grades (verses then passages): [2, 1, 2, 2, 1]

### q18 (en) 

> I get so angry that I say things I regret. Yesterday I screamed at my kids.

- rewritten: The person feels intense anger that leads them to say things they later regret, such as screaming at their children.
- themes: anger, guilt, family, self-control  (expected: anger, regret, self-control, family)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0320; `bhima-vows-revenge` 0.0320
- verses: `2.63` 0.609 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `1.40` 0.557 [direct] In the destruction of a family the immemorial family traditions perish…; `16.16` 0.521 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-25-3` 0.577 [direct]; `vana-29-1` 0.572 [direct]
- judge grades (verses then passages): [2, 1, 1, 0, 2]

### q19 (en) — HIT

> My husband has a serious illness and the doctors have given up, but I refuse to give up on him.

- rewritten: The person is facing a serious illness of her husband, with doctors having given up, yet she refuses to give up hope for his recovery.
- themes: grief, fear, duty, love, courage  (expected: devotion, death, perseverance, love)
- expected situation: savitri-satyavan
- situations: `savitri-satyavan` 0.0328; `arjuna-kurukshetra-dilemma` 0.0312
- verses: `13.10` 0.574 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `3.35` 0.562 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `7.11` 0.523 [direct] And I the strength of the strong, devoid of desire and passion. In bei…
- passages: `vana-65-6` 0.585 [direct]; `anusasana-146-6` 0.579 [direct]
- judge grades (verses then passages): [2, 1, 0, 1, 1]

### q20 (en) — MISS

> I've been unemployed for two years. Every rejection makes me feel more worthless, but I keep going.

- rewritten: The person has been unemployed for two years, and each rejection makes them feel increasingly worthless, yet they continue to persevere.
- themes: career, self-worth, fear of failure, despair, identity  (expected: patience, setback, self-worth, perseverance)
- expected situation: nala-damayanti-teaches-patience
- situations: `pandavas-mendicants-in-ekachakra` 0.0320; `draupadi-disrobing-sabha` 0.0315
- verses: `16.10` 0.595 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `13.10` 0.579 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.34` 0.540 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-218-6` 0.552 [direct]; `sabha-68-3` 0.453 [situation:draupadi-disrobing-sabha]
- judge grades (verses then passages): [1, 2, 0, 0, 1]

### q21 (en) 

> My team leader keeps making terrible decisions and I'm expected to support him in public.

- rewritten: The person feels forced to publicly support their team leader despite believing the leader makes terrible decisions.
- themes: duty, loyalty, injustice, humiliation  (expected: loyalty, duty, leadership, integrity)
- expected situation: -
- situations: `vikarna-protests-draupadi-disrobing` 0.0318; `bhima-vows-revenge` 0.0311
- verses: `2.7` 0.608 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.603 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.535 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-56-1` 0.452 [direct]; `santi-64-3` 0.443 [direct]
- judge grades (verses then passages): [0, 2, 2, 1, 0]

### q22 (en) — HIT

> I'm 70 and my children are settled. I want to let go of everything but I'm afraid.

- rewritten: The person is 70 years old, their children are settled, and they want to let go of everything but feel afraid.
- themes: fear, renunciation, attachment, purpose, identity  (expected: renunciation, letting go, death, fear)
- expected situation: pandavas-final-journey-renunciation
- situations: `pandavas-final-journey-renunciation` 0.0328; `pandavas-mendicants-in-ekachakra` 0.0320
- verses: `13.10` 0.636 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `4.23` 0.562 [direct] Of one with attachment dead, harmonious, with his thoughts established…; `2.62` 0.544 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…
- passages: `santi-289-2` 0.585 [direct]; `santi-219-3` 0.581 [direct]
- judge grades (verses then passages): [2, 2, 1, 2, 2]

### q23 (en) 

> I told my team we would never miss a deadline, and now keeping that promise means everyone burns out.

- rewritten: The person promised their team they would never miss a deadline, and now feels compelled to keep that promise even though it is causing the team to become exhausted and burnt out.
- themes: duty, guilt, fear, career, leadership  (expected: vow, pride, duty)
- expected situation: -
- situations: `yaksha-prashna` 0.0312; `bhima-vows-revenge` 0.0296
- verses: `3.35` 0.617 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.45` 0.578 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…; `18.47` 0.561 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-109-3` 0.561 [direct]; `santi-80-2` 0.560 [direct]
- judge grades (verses then passages): [2, 2, 1, 2, 1]

### q24 (en) — MISS

> My cousin is always compared with me and the family celebrates everything he does.

- rewritten: The person feels overlooked because their cousin is constantly compared to them and celebrated by the family, causing feelings of envy, rivalry, and humiliation.
- themes: envy, rivalry, humiliation, family, self-worth  (expected: envy, rivalry, family, comparison)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.0325; `karna-envy-arjuna-tournament` 0.0318
- verses: `1.40` 0.567 [direct] In the destruction of a family the immemorial family traditions perish…; `6.6` 0.557 [direct] The Self is the friend of the self of him in whom the self by the Self…; `3.43` 0.542 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-80-4` 0.608 [direct]; `santi-107-4` 0.599 [direct]
- judge grades (verses then passages): [0, 2, 1, 2, 1]

### q25 (en) 

> I don't know what I'm supposed to do with my life. Everyone else seems to have a plan.

- rewritten: The person feels uncertain about their life's direction and worries that others have clear plans while they do not.
- themes: purpose, identity, self-worth, fear, paralysis  (expected: purpose, career, confusion, duty)
- expected situation: -
- situations: `pandavas-mendicants-in-ekachakra` 0.0320; `draupadi-disrobing-sabha` 0.0300
- verses: `13.10` 0.673 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `10.4` 0.571 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `7.27` 0.517 [situation:pandavas-mendicants-in-ekachakra] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `santi-104-5` 0.584 [direct]; `santi-138-14` 0.574 [direct]
- judge grades (verses then passages): [1, 1, 1, 1, 0]

### q26 (hinglish) — MISS

> Yaar boards ke exam aa rahe hain aur mujhe lagta hai main fail ho jaunga, kuch padha hi nahi jaata

- rewritten: The person feels anxious about the upcoming board exams and believes they will fail because they have not studied.
- themes: fear of failure, exams, self-worth, despair, fear  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `draupadi-disrobing-sabha` 0.0317; `arjuna-jayadratha-vow-sunset` 0.0315
- verses: `13.10` 0.600 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `4.40` 0.571 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `10.4` 0.543 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…
- passages: `santi-277-2` 0.560 [direct]; `santi-104-5` 0.560 [direct]
- judge grades (verses then passages): [2, 1, 1, 0, 0]

### q27 (hinglish) 

> Mere papa chahte hain main engineering karu par mera mann art mein hai, ghar mein roz ladai hoti hai

- rewritten: The person feels torn because their father wants them to study engineering while they are drawn to art, and there are daily fights at home.
- themes: duty, family, career, purpose, identity  (expected: career, family, duty, conflict)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0323; `arjuna-kurukshetra-dilemma` 0.0315
- verses: `3.35` 0.522 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.45` 0.519 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…; `1.40` 0.515 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `bhishma-25-4` 0.474 [situation:arjuna-kurukshetra-dilemma]; `udyoga-146-2` 0.425 [situation:kunti-reveals-karna]
- judge grades (verses then passages): [2, 2, 1, 1, 0]

### q28 (hinglish) — HIT

> Usne mujhe sabke saamne zaleel kiya, main badla lena chahta hoon

- rewritten: The person was publicly humiliated and now feels a strong desire to take revenge.
- themes: humiliation, revenge, anger  (expected: humiliation, revenge, anger)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.0328; `bhima-kills-duhsasana-drinks-blood` 0.0320
- verses: `2.62` 0.652 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.633 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `16.12` 0.587 [direct] Held in bondage by a hundred ties of expectation, given over to lust a…
- passages: `santi-138-15` 0.590 [direct]; `bhishma-40-2` 0.578 [direct]
- judge grades (verses then passages): [2, 2, 1, 1, 2]

### q29 (hinglish) 

> Breakup ke baad se neend nahi aati, har cheez mein uski yaad aati hai

- rewritten: The person cannot sleep after a breakup and is constantly reminded of their ex in everything.
- themes: heartbreak, grief, loss, despair, loneliness  (expected: grief, loss, attachment, loneliness)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0323; `nala-damayanti-teaches-patience` 0.0320
- verses: `18.39` 0.611 [direct] That pleasure which both at first and afterwards is delusive of the se…; `16.16` 0.574 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `18.35` 0.544 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …
- passages: `santi-216-2` 0.572 [direct]; `santi-204-1` 0.563 [direct]
- judge grades (verses then passages): [0, 1, 0, 1, 1]

### q30 (hinglish) 

> Mera dost galat kaam kar raha hai par usne mushkil time mein mera saath diya tha, ab kya karu

- rewritten: The person is torn between confronting a friend who is engaged in wrongdoing and the gratitude they feel because the friend supported them during a difficult time.
- themes: loyalty, friendship, duty, guilt, integrity  (expected: loyalty, friendship, duty, truth)
- expected situation: -
- situations: `yudhishthira-seeks-blessings-from-elders` 0.0325; `yudhishthira-ashwatthama-lie` 0.0310
- verses: `3.35` 0.648 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `2.7` 0.639 [situation:yudhishthira-seeks-blessings-from-elders] My heart is weighed down with the vice of faintness; my mind is confus…; `6.6` 0.637 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-138-14` 0.649 [direct]; `santi-138-15` 0.625 [direct]
- judge grades (verses then passages): [1, 2, 1, 2, 1]

### q31 (hinglish) 

> Office mein sab mujhse aage nikal gaye, mujhe bahut jalan hoti hai

- rewritten: The person feels intense jealousy because everyone at work has advanced ahead of them.
- themes: envy, rivalry, self-worth, career, humiliation  (expected: envy, career, rivalry, comparison)
- expected situation: -
- situations: `draupadi-jealous-subhadra-arrival` 0.0323; `karna-envy-arjuna-tournament` 0.0315
- verses: `16.10` 0.614 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `3.27` 0.592 [direct] All actions are wrought by the quali ties of nature only. The self, de…; `6.6` 0.552 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-111-10` 0.593 [direct]; `santi-163-2` 0.589 [direct]
- judge grades (verses then passages): [1, 1, 2, 0, 2]

### q32 (hinglish) — MISS

> Maine jhooth bola taaki meri behen ki shaadi ho jaye, ab guilt se mar raha hoon

- rewritten: The person lied to facilitate their sister's marriage and now feels overwhelming guilt.
- themes: guilt, family, duty  (expected: deception, guilt, family, truth)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `bhima-vows-revenge` 0.0318; `yudhishthira-regrets-karna` 0.0311
- verses: `1.40` 0.560 [direct] In the destruction of a family the immemorial family traditions perish…; `3.35` 0.543 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.532 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `anusasana-162-11` 0.569 [direct]; `santi-109-3` 0.557 [direct]
- judge grades (verses then passages): [0, 1, 1, 2, 2]

### q33 (hinglish) 

> Bahut gussa aata hai, chhoti chhoti baat pe sab pe chilla deta hoon

- rewritten: The person feels intense anger and frequently shouts at others over minor issues.
- themes: anger, self-control  (expected: anger, self-control, regret)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `aswatthaman-night-massacre` 0.0317
- verses: `6.26` 0.593 [direct] As often as the wavering and unsteady mind goeth forth, so often reini…; `2.63` 0.576 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `6.7` 0.575 [direct] The higher Self of him who is Self -controlled and peaceful is uniform…
- passages: `vana-29-1` 0.576 [direct]; `udyoga-63-2` 0.563 [direct]
- judge grades (verses then passages): [1, 2, 1, 2, 2]

### q34 (hi) 

> मेरे पिताजी का देहांत हो गया है और मैं खुद को संभाल नहीं पा रहा हूँ

- rewritten: The person is struggling to cope after the death of their father and feels unable to manage their emotions.
- themes: grief, loss, death, family, despair  (expected: grief, loss, death)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `savitri-satyavan` 0.0315
- verses: `13.10` 0.636 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `1.40` 0.586 [direct] In the destruction of a family the immemorial family traditions perish…; `16.16` 0.571 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-175-3` 0.610 [direct]; `vana-295-11` 0.578 [situation:savitri-satyavan]
- judge grades (verses then passages): [1, 2, 0, 1, 0]

### q35 (hi) — MISS

> मेरे भाई को हमेशा ज़्यादा प्यार मिलता है, मुझे उससे जलन होती है

- rewritten: The person feels jealous because their brother always receives more love.
- themes: envy, family, self-worth, loneliness, attachment  (expected: envy, family, favoritism, sibling rivalry)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.0328; `bhima-spares-jayadratha` 0.0313
- verses: `2.62` 0.634 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `6.6` 0.564 [direct] The Self is the friend of the self of him in whom the self by the Self…; `6.7` 0.553 [direct] The higher Self of him who is Self -controlled and peaceful is uniform…
- passages: `santi-321-19` 0.621 [direct]; `santi-25-3` 0.593 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 1]

### q36 (hi) 

> मैंने एक वादा किया था जो अब मेरे लिए जाल बन गया है

- rewritten: The person made a promise that now feels like a trap, leaving them conflicted and burdened by the obligation. They feel trapped by the commitment and uncertain how to proceed.
- themes: vow, guilt, duty, fear, paralysis  (expected: vow, trap, duty)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0328; `bhima-vows-revenge` 0.0318
- verses: `16.10` 0.652 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.7` 0.631 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.615 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `santi-109-3` 0.583 [direct]; `anusasana-145-9` 0.576 [direct]
- judge grades (verses then passages): [0, 2, 2, 2, 1]

### q37 (hi) 

> नौकरी छूट गई है, समझ नहीं आता आगे क्या करूँ, बहुत डर लगता है

- rewritten: The person has lost their job and does not understand what to do next, feeling a great amount of fear.
- themes: fear, loss, career, despair, identity  (expected: fear, career, uncertainty, setback)
- expected situation: -
- situations: `pandavas-mendicants-in-ekachakra` 0.0325; `gandhari-lament-sons` 0.0317
- verses: `9.12` 0.632 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `18.25` 0.589 [direct] The action undertaken from delusion, without regard to capacity and co…; `16.16` 0.565 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-111-10` 0.568 [direct]; `santi-175-3` 0.564 [direct]
- judge grades (verses then passages): [1, 0, 1, 1, 1]

### q38 (hi) — HIT

> मेरी सास मुझे सबके सामने ताने मारती है और मेरे पति कुछ नहीं बोलते

- rewritten: The person feels humiliated as their mother-in-law publicly scolds them, while their husband remains silent and does not intervene.
- themes: humiliation, family, loyalty, fear  (expected: humiliation, silence, family, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `bhima-vows-revenge` 0.0320; `draupadi-disrobing-sabha` 0.0308
- verses: `18.16` 0.555 [direct] That being so, he verily who—owing to untrained Reason—looketh on his …; `12.19` 0.552 [direct] Taking equally praise and reproach, silent, wholly content with what c…; `1.40` 0.534 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-80-4` 0.591 [direct]; `anusasana-38-3` 0.549 [direct]
- judge grades (verses then passages): [1, 0, 1, 2, 0]

### q39 (hi) 

> जिस इंसान ने मेरा दिल तोड़ा, उसे माफ़ करूँ या नहीं?

- rewritten: The person wonders whether to forgive the individual who broke their heart.
- themes: forgiveness, heartbreak, betrayal, love  (expected: forgiveness, betrayal, anger)
- expected situation: -
- situations: `bhima-spares-jayadratha` 0.0323; `aswatthaman-night-massacre` 0.0308
- verses: `2.7` 0.643 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `14.24` 0.590 [direct] Balanced in pleasure and pain, self-reliant, to whom a lump of earth, …; `11.42` 0.589 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…
- passages: `udyoga-33-6` 0.616 [direct]; `vana-28-2` 0.595 [direct]
- judge grades (verses then passages): [1, 0, 1, 0, 1]

### q40 (banglish) — HIT

> Amar boss amake shobar shamne opoman korlo

- rewritten: The person feels humiliated because their boss insulted them in front of everyone, causing embarrassment and hurt.
- themes: humiliation, anger, self-worth, fear, loneliness  (expected: humiliation, workplace, anger)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0323; `aswatthaman-night-massacre` 0.0313
- verses: `16.18` 0.603 [situation:aswatthaman-night-massacre] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `2.63` 0.597 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `6.6` 0.573 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-111-10` 0.616 [direct]; `vana-29-1` 0.563 [direct]
- judge grades (verses then passages): [0, 2, 1, 2, 1]

### q41 (banglish) — MISS

> Porikkhar age bhoy lagche, mone hocche ami kichu parbo na

- rewritten: The person feels intense fear before an exam and believes they will not be able to succeed.
- themes: fear, fear of failure, exams  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-jayadratha-vow-sunset` 0.0323; `uttara-freezes-battle` 0.0318
- verses: `11.23` 0.587 [direct] Thy mighty Form, with many mouths and eyes, Long armed, with thighs an…; `11.45` 0.581 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `10.4` 0.552 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…
- passages: `santi-138-21` 0.556 [direct]; `santi-321-19` 0.551 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 1]

### q42 (banglish) 

> Ma baba chay ami chakri kori, kintu ami nijer business korte chai

- rewritten: The person feels torn because their parents want them to take a job, but they themselves want to start their own business.
- themes: duty, career, purpose, identity, self-worth  (expected: career, family, duty)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0313; `karna-parashurama-curse-lineage` 0.0310
- verses: `3.35` 0.583 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.564 [direct] Better is one's own duty though destitute of merits than the well-exec…; `18.45` 0.545 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `santi-260-3` 0.559 [direct]; `santi-332-2` 0.555 [direct]
- judge grades (verses then passages): [2, 2, 2, 1, 0]

### q43 (banglish) 

> Amar bondhu amar pith e chhuri marlo, ami ki korbo bujhte parchi na

- rewritten: The person’s friend stabbed their father and they feel confused and uncertain about what to do.
- themes: betrayal, grief, fear, anger, loss  (expected: betrayal, friendship, anger, confusion)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0323; `yudhishthira-regrets-karna` 0.0318
- verses: `2.63` 0.600 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `16.16` 0.588 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `17.9` 0.565 [direct] The passionate desire foods that are bitter, sour, saline, over-hot, p…
- passages: `santi-138-14` 0.601 [direct]; `adi-159-5` 0.580 [direct]
- judge grades (verses then passages): [1, 1, 0, 1, 2]

### q44 (banglish) 

> Khub eka lage, kotha bolar keu nei

- rewritten: The person feels extremely lonely and has no one to talk to.
- themes: loneliness, despair  (expected: loneliness, isolation)
- expected situation: -
- situations: `duryodhana-hides-lake` 0.0325; `yudhishthira-grief-after-victory` 0.0305
- verses: `9.12` 0.652 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `18.52` 0.640 [direct] Dwelling in solitude, abstemious, speech, body and mind subdued, const…; `13.11` 0.582 [situation:duryodhana-hides-lake] Unflinching devotion to Me by yoga, without other objects, resort to s…
- passages: `santi-177-5` 0.568 [direct]; `santi-177-4` 0.557 [direct]
- judge grades (verses then passages): [1, 0, 0, 1, 1]

### q45 (banglish) — HIT

> Online juar nesha hoye geche, shob taka hariye felechi

- rewritten: The person has become addicted to online gambling and has lost all of their money, feeling distressed and worried about the consequences.
- themes: addiction, loss, guilt, fear, despair  (expected: addiction, gambling, loss)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0325; `yudhishthira-grief-after-victory` 0.0325
- verses: `16.16` 0.653 [direct] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `16.11` 0.626 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `18.25` 0.583 [direct] The action undertaken from delusion, without regard to capacity and co…
- passages: `santi-104-5` 0.594 [direct]; `santi-177-5` 0.579 [direct]
- judge grades (verses then passages): [2, 2, 2, 2, 2]

### q46 (bn) 

> আমার বাবা মারা গেছেন, আমি কিছুতেই মেনে নিতে পারছি না

- rewritten: The person is unable to accept the death of their father and feels overwhelmed by the loss.
- themes: grief, loss, death, family  (expected: grief, loss, death)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `savitri-satyavan` 0.0320
- verses: `1.40` 0.637 [direct] In the destruction of a family the immemorial family traditions perish…; `16.11` 0.632 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `1.42` 0.581 [direct] This confusion draggeth to hell the slayers of the family, and the fam…
- passages: `santi-175-3` 0.604 [direct]; `vana-295-11` 0.596 [situation:savitri-satyavan]
- judge grades (verses then passages): [1, 0, 0, 1, 0]

### q47 (bn) 

> আমার ছোট ভাইকে সবাই বেশি ভালোবাসে, আমার খুব হিংসা হয়

- rewritten: The person feels intense envy because everyone loves their younger brother more than them.
- themes: envy, family  (expected: envy, family, favoritism)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0313; `bhima-spares-jayadratha` 0.0311
- verses: `2.62` 0.592 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `10.8` 0.562 [direct] I am the Generator of all; all evolves from Me; understanding thus, th…; `1.40` 0.530 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `anusasana-105-2` 0.570 [direct]; `santi-138-15` 0.563 [direct]
- judge grades (verses then passages): [2, 0, 0, 0, 1]

### q48 (bn) — HIT

> আমি জানি আমার দাদা ভুল করছে, কিন্তু পরিবারের সবাই চুপ করে আছে

- rewritten: The person knows their grandfather is doing something wrong, but everyone in the family remains silent.
- themes: family, duty, guilt, silence, injustice  (expected: silence, injustice, family, complicity)
- expected situation: silence-of-elders-udyoga
- situations: `yayati-sons-refuse-youth` 0.0317; `silence-of-elders-udyoga` 0.0311
- verses: `1.40` 0.599 [direct] In the destruction of a family the immemorial family traditions perish…; `18.47` 0.584 [direct] Better is one's own duty though destitute of merits than the well-exec…; `3.35` 0.562 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `sabha-66-17` 0.552 [direct]; `santi-266-10` 0.539 [direct]
- judge grades (verses then passages): [2, 0, 0, 2, 1]

### q49 (bn) — MISS

> চাকরির ইন্টারভিউতে বারবার ব্যর্থ হচ্ছি, আর ধৈর্য রাখতে পারছি না

- rewritten: The person keeps failing job interviews and feels unable to maintain patience.
- themes: fear of failure, patience, career, self-worth, despair  (expected: patience, failure, setback, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `arjuna-jayadratha-vow-sunset` 0.0315; `krishna-peace-mission` 0.0313
- verses: `9.12` 0.638 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `10.4` 0.555 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `4.40` 0.547 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…
- passages: `santi-139-10` 0.580 [direct]; `sauptika-2-3` 0.558 [direct]
- judge grades (verses then passages): [1, 1, 1, 2, 2]

### q50 (bn) 

> রাগের মাথায় এমন কিছু করে ফেলেছি যার জন্য এখন অনুশোচনা হচ্ছে

- rewritten: The person acted in a fit of anger and now feels regret for what they did.
- themes: anger, guilt  (expected: anger, regret, guilt)
- expected situation: -
- situations: `aswatthaman-night-massacre` 0.0325; `gandhari-lament-sons` 0.0318
- verses: `2.62` 0.646 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.643 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `16.18` 0.570 [situation:aswatthaman-night-massacre] Given over to egoism, power, insolence, lust and wrath, these maliciou…
- passages: `santi-146-3` 0.623 [direct]; `vana-29-3` 0.585 [direct]
- judge grades (verses then passages): [2, 2, 1, 2, 2]
