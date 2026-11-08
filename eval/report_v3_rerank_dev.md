# Retrieval eval report

- date: 2026-11-08  set: queries.yaml  queries: 50  runtime: 1215s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: True, linked_first: False, fts_text: all
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 64% (n=22) | 75% (n=12) | 33% (n=3) | 0% (n=2) | 67% (n=3) | 100% (n=2) |
| theme overlap: rewrite themes | 72% (n=50) | 65% (n=25) | 80% (n=8) | 64% (n=6) | 81% (n=6) | 93% (n=5) |
| theme overlap: retrieved situations' themes | 67% (n=50) | 70% (n=25) | 51% (n=8) | 56% (n=6) | 75% (n=6) | 85% (n=5) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |
| verse relevance, LLM judge (0-2 as %) | 59% (n=50) | 61% (n=25) | 65% (n=8) | 56% (n=6) | 64% (n=6) | 40% (n=5) |
| passage relevance, LLM judge (0-2 as %) | 50% (n=50) | 53% (n=25) | 47% (n=8) | 33% (n=6) | 54% (n=6) | 55% (n=5) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- q01 (en): expected `arjuna-kurukshetra-dilemma`, got `uttara-freezes-battle`, `nala-damayanti-teaches-patience`
- q15 (en): expected `eklavya-drona-thumb`, got `vikarna-protests-draupadi-disrobing`, `draupadi-disrobing-sabha`
- q20 (en): expected `nala-damayanti-teaches-patience`, got `pandavas-mendicants-in-ekachakra`, `draupadi-disrobing-sabha`
- q26 (hinglish): expected `arjuna-kurukshetra-dilemma`, got `arjuna-jayadratha-vow-sunset`, `nala-damayanti-teaches-patience`
- q32 (hinglish): expected `yudhishthira-ashwatthama-lie`, got `yudhishthira-regrets-karna`, `parashurama-kills-mother`
- q35 (hi): expected `duryodhana-maya-palace`, got `draupadi-jealous-subhadra-arrival`, `kunti-reveals-karna`
- q38 (hi): expected `draupadi-disrobing-sabha`, got `bhima-vows-revenge`, `vikarna-protests-draupadi-disrobing`
- q41 (banglish): expected `arjuna-kurukshetra-dilemma`, got `uttara-freezes-battle`, `arjuna-jayadratha-vow-sunset`

## Per query

### q01 (en) — MISS

> My exams start next week and I can't study at all. I just freeze every time I open the book.

- rewritten: The person feels unable to study for upcoming exams, freezing every time they open the book and fearing they will fail.
- themes: fear of failure, exams, paralysis, fear, despair  (expected: fear of failure, anxiety, paralysis, duty)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `uttara-freezes-battle` 0.1624; `nala-damayanti-teaches-patience` 0.0291
- verses: `18.35` 0.103 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …; `2.3` 0.003 [situation:uttara-freezes-battle] Yield not to impotence, O Partha! it doth not befit thee. Shake off th…; `9.12` 0.002 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…
- passages: `anusasana-149-9` 0.002 [direct]; `vana-67-3` 0.001 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [1, 2, 1, 0, 0]

### q02 (en) 

> My girlfriend broke up with me after four years and I don't know who I am without her.

- rewritten: The person feels lost and uncertain about who they are after their girlfriend ended a four‑year relationship.
- themes: heartbreak, identity, self-worth, loss, grief  (expected: grief, loss, attachment, identity)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.7078; `pandavas-mendicants-in-ekachakra` 0.0346
- verses: `4.40` 0.004 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `6.6` 0.003 [direct] The Self is the friend of the self of him in whom the self by the Self…; `16.11` 0.002 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-174-3` 0.006 [direct]; `vana-65-6` 0.003 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [1, 1, 1, 2, 2]

### q03 (en) 

> My parents want me to become a doctor but I want to study music. I feel like I'm betraying them.

- rewritten: The person feels torn because their parents want them to become a doctor, but they want to study music, and they feel they are betraying their parents.
- themes: betrayal, duty, family, identity, purpose  (expected: career, family, duty, guilt)
- expected situation: -
- situations: `arjuna-kurukshetra-dilemma` 0.1967; `kunti-reveals-karna` 0.1851
- verses: `1.40` 0.003 [direct] In the destruction of a family the immemorial family traditions perish…; `3.35` 0.001 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.48` 0.001 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…
- passages: `udyoga-36-4` 0.006 [direct]; `anusasana-149-9` 0.001 [direct]
- judge grades (verses then passages): [1, 2, 2, 0, 0]

### q04 (en) 

> My mother passed away last month and I keep thinking I should have done more for her.

- rewritten: The person feels deep guilt and grief after their mother passed away last month, believing they should have done more for her.
- themes: guilt, grief, loss, family  (expected: grief, guilt, loss)
- expected situation: -
- situations: `yudhishthira-regrets-karna` 0.0779; `yudhishthira-grief-after-victory` 0.0428
- verses: `1.40` 0.015 [direct] In the destruction of a family the immemorial family traditions perish…; `1.28` 0.012 [situation:yudhishthira-regrets-karna] Deeply moved to pity, thus uttered in sadness: Arjuna said: Seeing the…; `1.47` 0.001 [situation:yudhishthira-regrets-karna] Sanjaya said: Having thus spoken on the battle-field, Arjuna sank down…
- passages: `santi-139-8` 0.056 [direct]; `stri-27-3` 0.003 [situation:yudhishthira-regrets-karna]
- judge grades (verses then passages): [1, 0, 1, 1, 1]

### q05 (en) — HIT

> My manager shouted at me in front of the whole team and everyone just stayed quiet.

- rewritten: The person was publicly shouted at by their manager in front of the whole team, and everyone remained silent, leaving them feeling humiliated and upset.
- themes: humiliation, anger, fear, self-worth  (expected: humiliation, anger, injustice, silence)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.8297; `vikarna-protests-draupadi-disrobing` 0.3078
- verses: `2.34` 0.003 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `14.25` 0.002 [direct] The same in honour and ignominy, the same to friend and foe, abandonin…; `12.18` 0.001 [direct] Alike to foe and friend, and also in fame and ignominy, alike in cold …
- passages: `santi-134-2` 0.034 [direct]; `sabha-71-2` 0.005 [situation:draupadi-disrobing-sabha]
- judge grades (verses then passages): [1, 1, 1, 1, 1]

### q06 (en) — HIT

> My best friend got the promotion I worked for and I can't stop feeling bitter about it.

- rewritten: The person feels bitter because their best friend received a promotion they had worked for, leading to feelings of envy and resentment.
- themes: envy, rivalry, anger, self-worth, pride  (expected: envy, rivalry, resentment)
- expected situation: karna-envy-arjuna-tournament
- situations: `karna-envy-arjuna-tournament` 0.7025; `draupadi-jealous-subhadra-arrival` 0.3607
- verses: `6.6` 0.031 [direct] The Self is the friend of the self of him in whom the self by the Self…; `15.5` 0.008 [direct] Without pride and delusion, victorious over the vice of attachment, dw…; `6.5` 0.005 [direct] Let him raise the self by the Self and not let the self become depress…
- passages: `santi-80-2` 0.021 [direct]; `santi-138-14` 0.011 [direct]
- judge grades (verses then passages): [1, 2, 1, 0, 1]

### q07 (en) 

> I moved to a new city and I have nobody to talk to. Weekends are the worst.

- rewritten: The person has moved to a new city and feels isolated, having no one to talk to, making weekends especially difficult.
- themes: loneliness, despair  (expected: loneliness, isolation)
- expected situation: -
- situations: `duryodhana-hides-lake` 0.0863; `nala-damayanti-teaches-patience` 0.0505
- verses: `13.10` 0.040 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.22` 0.003 [direct] As a man, casting off worn-out garments, taketh new ones, so the dwell…; `13.11` 0.002 [situation:duryodhana-hides-lake] Unflinching devotion to Me by yoga, without other objects, resort to s…
- passages: `vana-67-3` 0.050 [situation:nala-damayanti-teaches-patience]; `santi-177-5` 0.047 [direct]
- judge grades (verses then passages): [1, 0, 0, 2, 1]

### q08 (en) 

> I lied to my wife about money and now the lie has become so big I can't take it back.

- rewritten: The person lied to their spouse about money, and the deception has grown so large that they feel unable to retract it, causing them guilt and fear.
- themes: guilt, fear, deception, betrayal  (expected: guilt, deception, truth, marriage)
- expected situation: -
- situations: `yudhishthira-ashwatthama-lie` 0.0586; `bhima-vows-revenge` 0.0576
- verses: `16.12` 0.162 [direct] Held in bondage by a hundred ties of expectation, given over to lust a…; `2.34` 0.145 [situation:yudhishthira-ashwatthama-lie] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `16.10` 0.103 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …
- passages: `santi-259-3` 0.007 [direct]; `anusasana-149-9` 0.003 [direct]
- judge grades (verses then passages): [1, 1, 1, 1, 1]

### q09 (en) — HIT

> I lost all my savings on crypto trading and I keep betting more to win it back.

- rewritten: The person lost all their savings on crypto trading and keeps betting more to try to win it back, feeling trapped and anxious.
- themes: loss, addiction, fear, guilt, despair  (expected: addiction, gambling, loss, recklessness)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.1309; `yudhishthira-grief-after-victory` 0.0087
- verses: `18.35` 0.053 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …; `16.16` 0.040 [direct] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `16.11` 0.004 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-104-5` 0.075 [direct]; `sabha-58-2` 0.003 [situation:yudhishthira-dice-game]
- judge grades (verses then passages): [1, 2, 1, 2, 2]

### q10 (en) 

> My friend is doing something clearly unethical at work but he helped me get this job. Should I report him?

- rewritten: The person is uncertain whether to report a coworker who is acting unethically because that coworker helped them obtain their job, and they feel conflicted about loyalty, duty, and doing the right thing.
- themes: integrity, loyalty, duty, fear, guilt  (expected: loyalty, truth, duty, friendship)
- expected situation: -
- situations: `yudhishthira-seeks-blessings-from-elders` 0.1095; `parashurama-kills-mother` 0.0760
- verses: `18.47` 0.138 [direct] Better is one's own duty though destitute of merits than the well-exec…; `2.7` 0.063 [situation:yudhishthira-seeks-blessings-from-elders] My heart is weighed down with the vice of faintness; my mind is confus…; `18.15` 0.047 [direct] Whatever action a man performeth by his body, speech and mind, whether…
- passages: `santi-132-3` 0.070 [direct]; `santi-260-1` 0.052 [direct]
- judge grades (verses then passages): [2, 2, 1, 2, 2]

### q11 (en) 

> I promised my dying father I'd take over his shop, but I hate it and it's ruining my life.

- rewritten: The person promised their dying father to take over the family shop, but now hates the work and feels it is ruining their life.
- themes: duty, family, despair, purpose, self-worth  (expected: vow, duty, family, career)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.1901; `shalya-karna-charioteer` 0.0268
- verses: `1.40` 0.050 [direct] In the destruction of a family the immemorial family traditions perish…; `3.35` 0.006 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.004 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-177-5` 0.002 [direct]; `anusasana-149-9` 0.001 [direct]
- judge grades (verses then passages): [1, 2, 2, 1, 0]

### q12 (en) 

> My brother cheated me out of my share of the family property. I want revenge.

- rewritten: The person feels cheated out of their share of the family property by their brother and wants revenge.
- themes: betrayal, revenge, anger, injustice, family  (expected: revenge, betrayal, family, anger, injustice)
- expected situation: -
- situations: `bhima-vows-revenge` 0.1603; `aswatthaman-night-massacre` 0.0622
- verses: `2.62` 0.217 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `16.12` 0.067 [direct] Held in bondage by a hundred ties of expectation, given over to lust a…; `1.40` 0.031 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `anusasana-105-2` 0.165 [direct]; `santi-259-2` 0.013 [direct]
- judge grades (verses then passages): [1, 2, 1, 2, 2]

### q13 (en) — HIT

> I found out I was adopted and my birth mother now wants to meet me. I feel angry and confused.

- rewritten: The person discovered they were adopted and now their birth mother wants to meet them, causing feelings of anger and confusion.
- themes: anger, identity, family  (expected: abandonment, identity, family, anger)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.2930; `yudhishthira-regrets-karna` 0.0195
- verses: `2.63` 0.039 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `1.42` 0.036 [direct] This confusion draggeth to hell the slayers of the family, and the fam…; `1.40` 0.002 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `anusasana-49-1` 0.003 [direct]; `anusasana-149-9` 0.001 [direct]
- judge grades (verses then passages): [2, 0, 0, 0, 0]

### q14 (en) 

> Everyone at college mocks me because I come from a village and my English is weak.

- rewritten: The person feels humiliated and isolated because classmates at college mock them for coming from a village and having weak English.
- themes: humiliation, self-worth, identity, loneliness  (expected: humiliation, exclusion, self-worth, background)
- expected situation: -
- situations: `vikarna-protests-draupadi-disrobing` 0.2560; `draupadi-disrobing-sabha` 0.2089
- verses: `18.16` 0.365 [direct] That being so, he verily who—owing to untrained Reason—looketh on his …; `6.5` 0.003 [direct] Let him raise the self by the Self and not let the self become depress…; `17.6` 0.003 [situation:draupadi-disrobing-sabha] Unintelligent, tormenting the aggregated elements forming the body, an…
- passages: `santi-111-10` 0.005 [direct]; `anusasana-149-9` 0.002 [direct]
- judge grades (verses then passages): [1, 2, 0, 2, 0]

### q15 (en) — MISS

> My professor took credit for my research and told me to keep quiet if I want my degree.

- rewritten: The person feels betrayed and intimidated after their professor claimed credit for their research and warned them to stay silent if they want to obtain their degree.
- themes: betrayal, injustice, fear, career, humiliation  (expected: exploitation, injustice, mentor, sacrifice)
- expected situation: eklavya-drona-thumb
- situations: `vikarna-protests-draupadi-disrobing` 0.5477; `draupadi-disrobing-sabha` 0.4882
- verses: `2.34` 0.003 [situation:vikarna-protests-draupadi-disrobing] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `5.20` 0.001 [direct] With Reason firm, unperplexed, the knower of the Eternal established i…; `16.10` 0.001 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …
- passages: `santi-138-21` 0.007 [direct]; `sabha-66-17` 0.002 [situation:draupadi-disrobing-sabha]
- judge grades (verses then passages): [2, 1, 1, 2, 2]

### q16 (en) — HIT

> My parents always defend my younger brother no matter what he does wrong.

- rewritten: The person feels frustrated because their parents always defend their younger brother regardless of his wrongdoing, leaving them feeling overlooked and unfairly treated.
- themes: favoritism, family, injustice  (expected: favoritism, family, injustice, resentment)
- expected situation: dhritarashtra-lac-house
- situations: `dhritarashtra-lac-house` 0.2476; `draupadi-disrobing-sabha` 0.0277
- verses: `1.34` 0.029 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `1.40` 0.009 [direct] In the destruction of a family the immemorial family traditions perish…; `16.10` 0.001 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …
- passages: `sabha-66-17` 0.003 [situation:draupadi-disrobing-sabha]; `santi-176-2` 0.003 [direct]
- judge grades (verses then passages): [0, 1, 1, 1, 0]

### q17 (en) — HIT

> I won the lawsuit against my old business partner but I feel empty instead of happy.

- rewritten: The person won a lawsuit against an old business partner but feels empty instead of happy.
- themes: despair, purpose, identity  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0120; `pandavas-mendicants-in-ekachakra` 0.0029
- verses: `9.12` 0.005 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `16.13` 0.001 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…; `2.8` 0.000 [situation:yudhishthira-grief-after-victory] For I see not that it would drive away this anguish that withers up my…
- passages: `santi-104-5` 0.008 [direct]; `santi-177-5` 0.006 [direct]
- judge grades (verses then passages): [0, 2, 2, 1, 2]

### q18 (en) 

> I get so angry that I say things I regret. Yesterday I screamed at my kids.

- rewritten: The person feels intense anger that leads them to say things they later regret, such as screaming at their children.
- themes: anger, guilt, family, self-control  (expected: anger, regret, self-control, family)
- expected situation: -
- situations: `aswatthaman-night-massacre` 0.1796; `yudhishthira-regrets-karna` 0.0682
- verses: `2.63` 0.020 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `16.10` 0.015 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.18` 0.005 [situation:aswatthaman-night-massacre] Given over to egoism, power, insolence, lust and wrath, these maliciou…
- passages: `vana-29-1` 0.016 [direct]; `anusasana-149-9` 0.005 [direct]
- judge grades (verses then passages): [2, 0, 2, 2, 0]

### q19 (en) — HIT

> My husband has a serious illness and the doctors have given up, but I refuse to give up on him.

- rewritten: The person is facing a serious illness of her husband, with doctors having given up, yet she refuses to give up hope for his recovery.
- themes: grief, fear, duty, love, courage  (expected: devotion, death, perseverance, love)
- expected situation: savitri-satyavan
- situations: `savitri-satyavan` 0.2763; `arjuna-jayadratha-vow-sunset` 0.0837
- verses: `18.45` 0.005 [situation:savitri-satyavan] Man reacheth perfection by each being intent on his own duty. Listen t…; `3.35` 0.004 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `2.7` 0.003 [direct] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `vana-295-11` 0.011 [situation:savitri-satyavan]; `drona-80-1` 0.009 [situation:arjuna-jayadratha-vow-sunset]
- judge grades (verses then passages): [1, 1, 2, 0, 2]

### q20 (en) — MISS

> I've been unemployed for two years. Every rejection makes me feel more worthless, but I keep going.

- rewritten: The person has been unemployed for two years, and each rejection makes them feel increasingly worthless, yet they continue to persevere.
- themes: career, self-worth, fear of failure, despair, identity  (expected: patience, setback, self-worth, perseverance)
- expected situation: nala-damayanti-teaches-patience
- situations: `pandavas-mendicants-in-ekachakra` 0.0660; `draupadi-disrobing-sabha` 0.0372
- verses: `13.10` 0.005 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `16.10` 0.005 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `6.5` 0.004 [direct] Let him raise the self by the Self and not let the self become depress…
- passages: `anusasana-149-9` 0.004 [direct]; `santi-218-6` 0.004 [direct]
- judge grades (verses then passages): [2, 1, 2, 0, 0]

### q21 (en) 

> My team leader keeps making terrible decisions and I'm expected to support him in public.

- rewritten: The person feels forced to publicly support their team leader despite believing the leader makes terrible decisions.
- themes: duty, loyalty, injustice, humiliation  (expected: loyalty, duty, leadership, integrity)
- expected situation: -
- situations: `vikarna-protests-draupadi-disrobing` 0.4837; `shalya-karna-charioteer` 0.3851
- verses: `3.35` 0.007 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.006 [direct] Better is one's own duty though destitute of merits than the well-exec…; `3.19` 0.004 [direct] Therefore, without attachment, constantly perform action which is duty…
- passages: `anusasana-149-9` 0.002 [direct]; `santi-56-1` 0.001 [direct]
- judge grades (verses then passages): [2, 2, 1, 0, 1]

### q22 (en) — HIT

> I'm 70 and my children are settled. I want to let go of everything but I'm afraid.

- rewritten: The person is 70 years old, their children are settled, and they want to let go of everything but feel afraid.
- themes: fear, renunciation, attachment, purpose, identity  (expected: renunciation, letting go, death, fear)
- expected situation: pandavas-final-journey-renunciation
- situations: `pandavas-final-journey-renunciation` 0.2074; `pandavas-mendicants-in-ekachakra` 0.0135
- verses: `13.10` 0.001 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `2.62` 0.001 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `8.6` 0.000 [situation:pandavas-final-journey-renunciation] Whosoever at the end abandoneth the body, thinking upon any being, to …
- passages: `santi-219-3` 0.194 [direct]; `santi-289-2` 0.066 [direct]
- judge grades (verses then passages): [2, 1, 1, 2, 2]

### q23 (en) 

> I told my team we would never miss a deadline, and now keeping that promise means everyone burns out.

- rewritten: The person promised their team they would never miss a deadline, and now feels compelled to keep that promise even though it is causing the team to become exhausted and burnt out.
- themes: duty, guilt, fear, career, leadership  (expected: vow, pride, duty)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0823; `shalya-karna-charioteer` 0.0429
- verses: `3.35` 0.004 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.004 [direct] Better is one's own duty though destitute of merits than the well-exec…; `18.45` 0.004 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…
- passages: `santi-109-3` 0.003 [direct]; `anusasana-149-9` 0.001 [direct]
- judge grades (verses then passages): [2, 1, 2, 2, 0]

### q24 (en) — HIT

> My cousin is always compared with me and the family celebrates everything he does.

- rewritten: The person feels overlooked because their cousin is constantly compared to them and celebrated by the family, causing feelings of envy, rivalry, and humiliation.
- themes: envy, rivalry, humiliation, family, self-worth  (expected: envy, rivalry, family, comparison)
- expected situation: duryodhana-maya-palace
- situations: `karna-envy-arjuna-tournament` 0.5730; `duryodhana-maya-palace` 0.4499
- verses: `6.6` 0.051 [direct] The Self is the friend of the self of him in whom the self by the Self…; `1.40` 0.039 [direct] In the destruction of a family the immemorial family traditions perish…; `16.16` 0.015 [situation:duryodhana-maya-palace] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-80-4` 0.111 [direct]; `sabha-49-3` 0.013 [situation:duryodhana-maya-palace]
- judge grades (verses then passages): [2, 0, 0, 2, 2]

### q25 (en) 

> I don't know what I'm supposed to do with my life. Everyone else seems to have a plan.

- rewritten: The person feels uncertain about their life's direction and worries that others have clear plans while they do not.
- themes: purpose, identity, self-worth, fear, paralysis  (expected: purpose, career, confusion, duty)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0411; `pandavas-mendicants-in-ekachakra` 0.0107
- verses: `13.10` 0.024 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `10.4` 0.021 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `11.31` 0.002 [direct] Reveal Thy Self; what awful Form art Thou? I worship Thee! Have mercy,…
- passages: `santi-104-5` 0.051 [direct]; `santi-138-14` 0.008 [direct]
- judge grades (verses then passages): [1, 1, 2, 1, 0]

### q26 (hinglish) — MISS

> Yaar boards ke exam aa rahe hain aur mujhe lagta hai main fail ho jaunga, kuch padha hi nahi jaata

- rewritten: The person feels anxious about the upcoming board exams and believes they will fail because they have not studied.
- themes: fear of failure, exams, self-worth, despair, fear  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `arjuna-jayadratha-vow-sunset` 0.0306; `nala-damayanti-teaches-patience` 0.0178
- verses: `10.4` 0.016 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `4.40` 0.014 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `13.10` 0.003 [direct] Unattachment, absence of self-identification with son, wife or home, a…
- passages: `santi-104-5` 0.004 [direct]; `anusasana-149-9` 0.002 [direct]
- judge grades (verses then passages): [1, 1, 2, 0, 0]

### q27 (hinglish) 

> Mere papa chahte hain main engineering karu par mera mann art mein hai, ghar mein roz ladai hoti hai

- rewritten: The person feels torn because their father wants them to study engineering while they are drawn to art, and there are daily fights at home.
- themes: duty, family, career, purpose, identity  (expected: career, family, duty, conflict)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0701; `arjuna-kurukshetra-dilemma` 0.0681
- verses: `18.59` 0.001 [direct] Entrenched in egoism, thou thinkest, "I will not fight;" to no purpose…; `18.48` 0.001 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…; `3.35` 0.000 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `anusasana-16-4` 0.000 [direct]; `santi-44-2` 0.000 [direct]
- judge grades (verses then passages): [1, 2, 2, 0, 0]

### q28 (hinglish) — HIT

> Usne mujhe sabke saamne zaleel kiya, main badla lena chahta hoon

- rewritten: The person was publicly humiliated and now feels a strong desire to take revenge.
- themes: humiliation, revenge, anger  (expected: humiliation, revenge, anger)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.8585; `bhima-kills-duhsasana-drinks-blood` 0.7484
- verses: `2.62` 0.394 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.020 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.34` 0.003 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `karna-83-3` 0.011 [situation:bhima-kills-duhsasana-drinks-blood]; `sabha-70-2` 0.006 [situation:bhima-vows-revenge]
- judge grades (verses then passages): [2, 2, 2, 1, 1]

### q29 (hinglish) 

> Breakup ke baad se neend nahi aati, har cheez mein uski yaad aati hai

- rewritten: The person cannot sleep after a breakup and is constantly reminded of their ex in everything.
- themes: heartbreak, grief, loss, despair, loneliness  (expected: grief, loss, attachment, loneliness)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0571; `vidura-insomnia-burden-of-knowledge` 0.0254
- verses: `18.35` 0.165 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …; `18.39` 0.012 [direct] That pleasure which both at first and afterwards is delusive of the se…; `13.10` 0.004 [direct] Unattachment, absence of self-identification with son, wife or home, a…
- passages: `santi-104-5` 0.042 [direct]; `vana-65-6` 0.016 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [0, 0, 2, 0, 1]

### q30 (hinglish) 

> Mera dost galat kaam kar raha hai par usne mushkil time mein mera saath diya tha, ab kya karu

- rewritten: The person is torn between confronting a friend who is engaged in wrongdoing and the gratitude they feel because the friend supported them during a difficult time.
- themes: loyalty, friendship, duty, guilt, integrity  (expected: loyalty, friendship, duty, truth)
- expected situation: -
- situations: `karna-parashurama-curse-lineage` 0.2789; `yudhishthira-seeks-blessings-from-elders` 0.0711
- verses: `18.47` 0.012 [direct] Better is one's own duty though destitute of merits than the well-exec…; `3.35` 0.004 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `2.7` 0.001 [situation:yudhishthira-seeks-blessings-from-elders] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `santi-138-14` 0.014 [direct]; `santi-138-15` 0.010 [direct]
- judge grades (verses then passages): [1, 1, 2, 2, 1]

### q31 (hinglish) 

> Office mein sab mujhse aage nikal gaye, mujhe bahut jalan hoti hai

- rewritten: The person feels intense jealousy because everyone at work has advanced ahead of them.
- themes: envy, rivalry, self-worth, career, humiliation  (expected: envy, career, rivalry, comparison)
- expected situation: -
- situations: `draupadi-jealous-subhadra-arrival` 0.5389; `duryodhana-maya-palace` 0.3169
- verses: `16.10` 0.015 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.16` 0.007 [situation:duryodhana-maya-palace] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `6.6` 0.005 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-163-2` 0.140 [direct]; `sabha-49-3` 0.016 [situation:duryodhana-maya-palace]
- judge grades (verses then passages): [1, 1, 2, 2, 2]

### q32 (hinglish) — MISS

> Maine jhooth bola taaki meri behen ki shaadi ho jaye, ab guilt se mar raha hoon

- rewritten: The person lied to facilitate their sister's marriage and now feels overwhelming guilt.
- themes: guilt, family, duty  (expected: deception, guilt, family, truth)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `yudhishthira-regrets-karna` 0.3019; `parashurama-kills-mother` 0.2118
- verses: `18.47` 0.010 [direct] Better is one's own duty though destitute of merits than the well-exec…; `3.35` 0.010 [situation:parashurama-kills-mother] Better one's own duty, though destitute of merit, than the duty of ano…; `1.42` 0.004 [direct] This confusion draggeth to hell the slayers of the family, and the fam…
- passages: `santi-109-3` 0.018 [direct]; `anusasana-149-9` 0.002 [direct]
- judge grades (verses then passages): [1, 1, 0, 2, 0]

### q33 (hinglish) 

> Bahut gussa aata hai, chhoti chhoti baat pe sab pe chilla deta hoon

- rewritten: The person feels intense anger and frequently shouts at others over minor issues.
- themes: anger, self-control  (expected: anger, self-control, regret)
- expected situation: -
- situations: `aswatthaman-night-massacre` 0.0277; `bhima-vows-revenge` 0.0121
- verses: `6.26` 0.404 [direct] As often as the wavering and unsteady mind goeth forth, so often reini…; `2.63` 0.018 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `6.7` 0.007 [direct] The higher Self of him who is Self -controlled and peaceful is uniform…
- passages: `santi-300-4` 0.099 [direct]; `vana-29-1` 0.056 [direct]
- judge grades (verses then passages): [1, 2, 1, 1, 2]

### q34 (hi) 

> मेरे पिताजी का देहांत हो गया है और मैं खुद को संभाल नहीं पा रहा हूँ

- rewritten: The person is struggling to cope after the death of their father and feels unable to manage their emotions.
- themes: grief, loss, death, family, despair  (expected: grief, loss, death)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.3118; `yudhishthira-grief-after-victory` 0.0639
- verses: `1.40` 0.028 [direct] In the destruction of a family the immemorial family traditions perish…; `16.11` 0.008 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `13.10` 0.006 [direct] Unattachment, absence of self-identification with son, wife or home, a…
- passages: `santi-104-5` 0.146 [direct]; `vana-65-6` 0.010 [situation:nala-damayanti-teaches-patience]
- judge grades (verses then passages): [2, 0, 1, 0, 1]

### q35 (hi) — MISS

> मेरे भाई को हमेशा ज़्यादा प्यार मिलता है, मुझे उससे जलन होती है

- rewritten: The person feels jealous because their brother always receives more love.
- themes: envy, family, self-worth, loneliness, attachment  (expected: envy, family, favoritism, sibling rivalry)
- expected situation: duryodhana-maya-palace
- situations: `draupadi-jealous-subhadra-arrival` 0.2113; `kunti-reveals-karna` 0.0059
- verses: `2.62` 0.026 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `18.34` 0.002 [situation:draupadi-jealous-subhadra-arrival] But the firmness, O Arjuna, by which, from attachment desirous of frui…; `6.6` 0.001 [direct] The Self is the friend of the self of him in whom the self by the Self…
- passages: `santi-321-19` 0.006 [direct]; `anusasana-149-9` 0.005 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 1]

### q36 (hi) 

> मैंने एक वादा किया था जो अब मेरे लिए जाल बन गया है

- rewritten: The person made a promise that now feels like a trap, leaving them conflicted and burdened by the obligation. They feel trapped by the commitment and uncertain how to proceed.
- themes: vow, guilt, duty, fear, paralysis  (expected: vow, trap, duty)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.3672; `arjuna-jayadratha-vow-sunset` 0.0833
- verses: `2.7` 0.040 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.10` 0.015 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `3.35` 0.014 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `santi-109-3` 0.020 [direct]; `anusasana-145-9` 0.004 [direct]
- judge grades (verses then passages): [2, 0, 2, 2, 1]

### q37 (hi) 

> नौकरी छूट गई है, समझ नहीं आता आगे क्या करूँ, बहुत डर लगता है

- rewritten: The person has lost their job and does not understand what to do next, feeling a great amount of fear.
- themes: fear, loss, career, despair, identity  (expected: fear, career, uncertainty, setback)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.1418; `pandavas-mendicants-in-ekachakra` 0.0615
- verses: `2.40` 0.032 [direct] In this there is no loss of effort, nor is there transgression. Even a…; `2.67` 0.005 [direct] Such of the roving senses as the mind yieldeth to, that hurries away t…; `9.12` 0.001 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…
- passages: `anusasana-149-9` 0.002 [direct]; `santi-111-10` 0.001 [direct]
- judge grades (verses then passages): [2, 1, 1, 0, 1]

### q38 (hi) — MISS

> मेरी सास मुझे सबके सामने ताने मारती है और मेरे पति कुछ नहीं बोलते

- rewritten: The person feels humiliated as their mother-in-law publicly scolds them, while their husband remains silent and does not intervene.
- themes: humiliation, family, loyalty, fear  (expected: humiliation, silence, family, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `bhima-vows-revenge` 0.3705; `vikarna-protests-draupadi-disrobing` 0.3572
- verses: `1.40` 0.008 [direct] In the destruction of a family the immemorial family traditions perish…; `1.34` 0.007 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `2.34` 0.005 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `anusasana-38-3` 0.104 [direct]; `vana-231-4` 0.041 [direct]
- judge grades (verses then passages): [1, 0, 2, 0, 1]

### q39 (hi) 

> जिस इंसान ने मेरा दिल तोड़ा, उसे माफ़ करूँ या नहीं?

- rewritten: The person wonders whether to forgive the individual who broke their heart.
- themes: forgiveness, heartbreak, betrayal, love  (expected: forgiveness, betrayal, anger)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0099; `yudhishthira-regrets-karna` 0.0047
- verses: `11.42` 0.003 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…; `2.7` 0.001 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `11.45` 0.000 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…
- passages: `udyoga-33-6` 0.074 [direct]; `vana-28-2` 0.010 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 1]

### q40 (banglish) — HIT

> Amar boss amake shobar shamne opoman korlo

- rewritten: The person feels humiliated because their boss insulted them in front of everyone, causing embarrassment and hurt.
- themes: humiliation, anger, self-worth, fear, loneliness  (expected: humiliation, workplace, anger)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.6772; `bhima-vows-revenge` 0.6522
- verses: `2.34` 0.032 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `6.7` 0.032 [direct] The higher Self of him who is Self -controlled and peaceful is uniform…; `10.4` 0.012 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…
- passages: `santi-111-10` 0.027 [direct]; `vana-29-1` 0.010 [direct]
- judge grades (verses then passages): [2, 1, 1, 2, 1]

### q41 (banglish) — MISS

> Porikkhar age bhoy lagche, mone hocche ami kichu parbo na

- rewritten: The person feels intense fear before an exam and believes they will not be able to succeed.
- themes: fear, fear of failure, exams  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `uttara-freezes-battle` 0.0325; `arjuna-jayadratha-vow-sunset` 0.0232
- verses: `11.45` 0.079 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `10.4` 0.004 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `11.23` 0.002 [direct] Thy mighty Form, with many mouths and eyes, Long armed, with thighs an…
- passages: `anusasana-149-9` 0.003 [direct]; `santi-321-19` 0.001 [direct]
- judge grades (verses then passages): [1, 1, 1, 0, 1]

### q42 (banglish) 

> Ma baba chay ami chakri kori, kintu ami nijer business korte chai

- rewritten: The person feels torn because their parents want them to take a job, but they themselves want to start their own business.
- themes: duty, career, purpose, identity, self-worth  (expected: career, family, duty)
- expected situation: -
- situations: `karna-parashurama-curse-lineage` 0.1245; `arjuna-kurukshetra-dilemma` 0.0651
- verses: `18.47` 0.002 [direct] Better is one's own duty though destitute of merits than the well-exec…; `18.45` 0.002 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…; `3.35` 0.001 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `santi-332-2` 0.004 [direct]; `anusasana-149-9` 0.002 [direct]
- judge grades (verses then passages): [2, 2, 2, 0, 0]

### q43 (banglish) 

> Amar bondhu amar pith e chhuri marlo, ami ki korbo bujhte parchi na

- rewritten: The person’s friend stabbed their father and they feel confused and uncertain about what to do.
- themes: betrayal, grief, fear, anger, loss  (expected: betrayal, friendship, anger, confusion)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.2009; `aswatthaman-night-massacre` 0.0496
- verses: `1.42` 0.055 [direct] This confusion draggeth to hell the slayers of the family, and the fam…; `2.63` 0.036 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `2.62` 0.004 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…
- passages: `udyoga-36-6` 0.081 [direct]; `udyoga-136-1` 0.009 [direct]
- judge grades (verses then passages): [2, 1, 0, 1, 1]

### q44 (banglish) 

> Khub eka lage, kotha bolar keu nei

- rewritten: The person feels extremely lonely and has no one to talk to.
- themes: loneliness, despair  (expected: loneliness, isolation)
- expected situation: -
- situations: `duryodhana-hides-lake` 0.1934; `nala-damayanti-teaches-patience` 0.0357
- verses: `9.12` 0.071 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `13.11` 0.003 [situation:duryodhana-hides-lake] Unflinching devotion to Me by yoga, without other objects, resort to s…; `2.29` 0.001 [direct] As marvellous one regardeth him; as marvellous another speaketh thereo…
- passages: `vana-67-3` 0.143 [situation:nala-damayanti-teaches-patience]; `santi-177-5` 0.069 [direct]
- judge grades (verses then passages): [1, 0, 1, 2, 1]

### q45 (banglish) — HIT

> Online juar nesha hoye geche, shob taka hariye felechi

- rewritten: The person has become addicted to online gambling and has lost all of their money, feeling distressed and worried about the consequences.
- themes: addiction, loss, guilt, fear, despair  (expected: addiction, gambling, loss)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0767; `yudhishthira-grief-after-victory` 0.0129
- verses: `18.35` 0.074 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …; `16.16` 0.045 [direct] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `18.25` 0.009 [direct] The action undertaken from delusion, without regard to capacity and co…
- passages: `santi-104-5` 0.113 [direct]; `sabha-58-2` 0.007 [situation:yudhishthira-dice-game]
- judge grades (verses then passages): [1, 2, 2, 2, 2]

### q46 (bn) 

> আমার বাবা মারা গেছেন, আমি কিছুতেই মেনে নিতে পারছি না

- rewritten: The person is unable to accept the death of their father and feels overwhelmed by the loss.
- themes: grief, loss, death, family  (expected: grief, loss, death)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.3963; `savitri-satyavan` 0.2082
- verses: `1.40` 0.076 [direct] In the destruction of a family the immemorial family traditions perish…; `16.11` 0.013 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `1.42` 0.009 [direct] This confusion draggeth to hell the slayers of the family, and the fam…
- passages: `vana-65-6` 0.050 [situation:nala-damayanti-teaches-patience]; `vana-295-11` 0.030 [situation:savitri-satyavan]
- judge grades (verses then passages): [1, 0, 0, 1, 0]

### q47 (bn) 

> আমার ছোট ভাইকে সবাই বেশি ভালোবাসে, আমার খুব হিংসা হয়

- rewritten: The person feels intense envy because everyone loves their younger brother more than them.
- themes: envy, family  (expected: envy, family, favoritism)
- expected situation: -
- situations: `draupadi-jealous-subhadra-arrival` 0.0150; `dhritarashtra-lac-house` 0.0113
- verses: `1.34` 0.022 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `16.11` 0.003 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `1.40` 0.003 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `anusasana-105-1` 0.129 [direct]; `anusasana-105-2` 0.077 [direct]
- judge grades (verses then passages): [0, 1, 0, 1, 0]

### q48 (bn) — HIT

> আমি জানি আমার দাদা ভুল করছে, কিন্তু পরিবারের সবাই চুপ করে আছে

- rewritten: The person knows their grandfather is doing something wrong, but everyone in the family remains silent.
- themes: family, duty, guilt, silence, injustice  (expected: silence, injustice, family, complicity)
- expected situation: silence-of-elders-udyoga
- situations: `vikarna-protests-draupadi-disrobing` 0.4433; `silence-of-elders-udyoga` 0.1763
- verses: `1.40` 0.039 [direct] In the destruction of a family the immemorial family traditions perish…; `18.47` 0.009 [direct] Better is one's own duty though destitute of merits than the well-exec…; `3.35` 0.008 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `anusasana-149-9` 0.004 [direct]; `sabha-66-17` 0.002 [direct]
- judge grades (verses then passages): [2, 0, 0, 0, 2]

### q49 (bn) — HIT

> চাকরির ইন্টারভিউতে বারবার ব্যর্থ হচ্ছি, আর ধৈর্য রাখতে পারছি না

- rewritten: The person keeps failing job interviews and feels unable to maintain patience.
- themes: fear of failure, patience, career, self-worth, despair  (expected: patience, failure, setback, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0582; `pandavas-mendicants-in-ekachakra` 0.0399
- verses: `10.4` 0.005 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `4.40` 0.001 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `9.12` 0.000 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…
- passages: `santi-139-10` 0.016 [direct]; `sauptika-2-3` 0.002 [direct]
- judge grades (verses then passages): [1, 1, 1, 2, 2]

### q50 (bn) 

> রাগের মাথায় এমন কিছু করে ফেলেছি যার জন্য এখন অনুশোচনা হচ্ছে

- rewritten: The person acted in a fit of anger and now feels regret for what they did.
- themes: anger, guilt  (expected: anger, regret, guilt)
- expected situation: -
- situations: `yudhishthira-regrets-karna` 0.0497; `aswatthaman-night-massacre` 0.0299
- verses: `2.63` 0.065 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `2.62` 0.010 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `16.18` 0.001 [situation:aswatthaman-night-massacre] Given over to egoism, power, insolence, lust and wrath, these maliciou…
- passages: `santi-146-3` 0.006 [direct]; `santi-291-3` 0.005 [direct]
- judge grades (verses then passages): [2, 2, 1, 2, 1]
