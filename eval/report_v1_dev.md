# Retrieval eval report

- date: 2026-11-07  set: queries.yaml  queries: 50  runtime: 86s
- LLM chain: groq,openrouter (groq: openai/gpt-oss-120b,qwen/qwen3.8-27b; openrouter: google/gemma-4-31b-it:free,nvidia/nemotron-3-ultra-550b-a55b:free,google/gemma-4-26b-a4b-it:free; nvidia: nvidia/nemotron-3-ultra-550b-a55b; anthropic: claude-haiku-5-5), rerank: False
- theme match = mapped to data/themes.yaml, then equal or substring

## Summary

| metric | all | en | hinglish | hi | banglish | bn |
|---|---|---|---|---|---|---|
| situation hit rate (expected in top 2) | 68% (n=22) | 67% (n=12) | 67% (n=3) | 50% (n=2) | 67% (n=3) | 100% (n=2) |
| theme overlap: rewrite themes | 72% (n=50) | 73% (n=25) | 70% (n=8) | 67% (n=6) | 86% (n=6) | 65% (n=5) |
| theme overlap: retrieved situations' themes | 54% (n=50) | 56% (n=25) | 51% (n=8) | 60% (n=6) | 39% (n=6) | 57% (n=5) |
| theme overlap: retrieved verses' themes | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) | n/a (n=0) |

Verse theme overlap needs `themes` on verses; 0 of 701 verses have them so far.

## Situation misses

- q01 (en): expected `arjuna-kurukshetra-dilemma`, got `nala-damayanti-teaches-patience`, `arjuna-jayadratha-vow-sunset`
- q15 (en): expected `eklavya-drona-thumb`, got `silence-of-elders-udyoga`, `drona-demands-drupada`
- q19 (en): expected `savitri-satyavan`, got `nala-damayanti-teaches-patience`, `yudhishthira-dice-game`
- q24 (en): expected `duryodhana-maya-palace`, got `kunti-reveals-karna`, `karna-envy-arjuna-tournament`
- q26 (hinglish): expected `arjuna-kurukshetra-dilemma`, got `nala-damayanti-teaches-patience`, `arjuna-jayadratha-vow-sunset`
- q35 (hi): expected `duryodhana-maya-palace`, got `karna-envy-arjuna-tournament`, `bhima-spares-jayadratha`
- q41 (banglish): expected `arjuna-kurukshetra-dilemma`, got `bhima-kills-duhsasana-drinks-blood`, `nala-damayanti-teaches-patience`

## Per query

### q01 (en) — MISS

> My exams start next week and I can't study at all. I just freeze every time I open the book.

- rewritten: The person feels unable to study for upcoming exams, freezing every time they try to open the book.
- themes: anxiety, procrastination, fear of failure, stress, exam pressure  (expected: fear of failure, anxiety, paralysis, duty)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `nala-damayanti-teaches-patience` 0.0320; `arjuna-jayadratha-vow-sunset` 0.0320
- verses: `2.7` 0.574 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `6.24` 0.532 [direct] Abandoning without reserve all desires born of the imagination, by the…; `7.27` 0.488 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `aswamedha-17-2` 0.562 [direct]; `santi-174-7` 0.529 [direct]

### q02 (en) 

> My girlfriend broke up with me after four years and I don't know who I am without her.

- rewritten: The person feels lost and uncertain about their identity after their girlfriend ended a four‑year relationship.
- themes: heartbreak, identity, loss, loneliness, grief  (expected: grief, loss, attachment, identity)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0325; `gandhari-lament-sons` 0.0323
- verses: `13.10` 0.604 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `12.18` 0.571 [direct] Alike to foe and friend, and also in fame and ignominy, alike in cold …; `16.16` 0.525 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `vana-65-6` 0.533 [situation:nala-damayanti-teaches-patience]; `santi-28-4` 0.509 [direct]

### q03 (en) 

> My parents want me to become a doctor but I want to study music. I feel like I'm betraying them.

- rewritten: The person feels torn between their parents' expectation to become a doctor and their own desire to study music, fearing they are betraying their family. They experience guilt and conflict over choosing between duty to family and personal passion.
- themes: duty, family, career, passion, guilt  (expected: career, family, duty, guilt)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0325; `arjuna-kurukshetra-dilemma` 0.0320
- verses: `3.35` 0.591 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `17.9` 0.564 [direct] The passionate desire foods that are bitter, sour, saline, over-hot, p…; `18.47` 0.533 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `vana-112-3` 0.556 [direct]; `bhishma-25-4` 0.478 [situation:arjuna-kurukshetra-dilemma]

### q04 (en) 

> My mother passed away last month and I keep thinking I should have done more for her.

- rewritten: The person feels deep grief after their mother's death last month and is haunted by thoughts that they could have done more for her. They are struggling with guilt and regret over missed opportunities to support her.
- themes: grief, guilt, regret, family, loss  (expected: grief, guilt, loss)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0323; `nala-damayanti-teaches-patience` 0.0318
- verses: `2.7` 0.576 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.11` 0.559 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `16.16` 0.548 [situation:gandhari-lament-sons] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-139-8` 0.558 [direct]; `santi-277-3` 0.551 [direct]

### q05 (en) — HIT

> My manager shouted at me in front of the whole team and everyone just stayed quiet.

- rewritten: The person was shouted at by their manager in front of the whole team, and everyone stayed quiet, leaving them feeling humiliated and isolated.
- themes: humiliation, embarrassment, isolation, workplace, fear  (expected: humiliation, anger, injustice, silence)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0325; `duryodhana-maya-palace` 0.0323
- verses: `12.18` 0.553 [direct] Alike to foe and friend, and also in fame and ignominy, alike in cold …; `14.25` 0.551 [direct] The same in honour and ignominy, the same to friend and foe, abandonin…; `16.16` 0.474 [situation:duryodhana-maya-palace] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-111-10` 0.570 [direct]; `santi-139-4` 0.524 [direct]

### q06 (en) — HIT

> My best friend got the promotion I worked for and I can't stop feeling bitter about it.

- rewritten: The person feels bitter and resentful because their best friend received the promotion they had been working for, and they cannot stop dwelling on this perceived injustice.
- themes: envy, bitter, career, friendship, resentment  (expected: envy, rivalry, resentment)
- expected situation: karna-envy-arjuna-tournament
- situations: `karna-envy-arjuna-tournament` 0.0318; `karna-parashurama-curse-lineage` 0.0318
- verses: `2.7` 0.590 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `6.6` 0.549 [direct] The Self is the friend of the self of him in whom the self by the Self…; `18.34` 0.462 [situation:karna-envy-arjuna-tournament] But the firmness, O Arjuna, by which, from attachment desirous of frui…
- passages: `santi-138-14` 0.581 [direct]; `santi-80-2` 0.579 [direct]

### q07 (en) 

> I moved to a new city and I have nobody to talk to. Weekends are the worst.

- rewritten: The person feels isolated after moving to a new city, has no one to talk to, and finds weekends especially difficult.
- themes: loneliness, isolation, relocation, sadness, social anxiety  (expected: loneliness, isolation)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0325; `pandavas-final-journey-renunciation` 0.0325
- verses: `2.22` 0.504 [direct] As a man, casting off worn-out garments, taketh new ones, so the dwell…; `3.2` 0.490 [direct] With these perplexing words Thou only confusest my understanding; ther…; `11.42` 0.485 [direct] If jesting I irreverence showed to Thee, At play, reposing, sitting or…
- passages: `santi-28-4` 0.530 [direct]; `udyoga-37-6` 0.492 [direct]

### q08 (en) 

> I lied to my wife about money and now the lie has become so big I can't take it back.

- rewritten: The person lied to their spouse about money and now feels trapped by the growing deception, unable to retract it.
- themes: guilt, deception, fear, marital conflict, anxiety  (expected: guilt, deception, truth, marriage)
- expected situation: -
- situations: `yudhishthira-ashwatthama-lie` 0.0323; `nala-damayanti-teaches-patience` 0.0315
- verses: `16.10` 0.649 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.11` 0.562 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `2.34` 0.552 [situation:yudhishthira-ashwatthama-lie] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-321-19` 0.599 [direct]; `anusasana-162-11` 0.599 [direct]

### q09 (en) — HIT

> I lost all my savings on crypto trading and I keep betting more to win it back.

- rewritten: The person lost all their savings in crypto trading and keeps betting more to try to win it back, feeling trapped in a cycle of risk and desperation.
- themes: loss, gambling, financial stress, desperation, addiction  (expected: addiction, gambling, loss, recklessness)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-dice-game` 0.0328; `nala-damayanti-teaches-patience` 0.0323
- verses: `16.12` 0.607 [direct] Held in bondage by a hundred ties of expectation, given over to lust a…; `16.16` 0.588 [direct] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `16.11` 0.579 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-104-5` 0.578 [direct]; `sabha-62-1` 0.546 [direct]

### q10 (en) 

> My friend is doing something clearly unethical at work but he helped me get this job. Should I report him?

- rewritten: The person is conflicted because a friend who helped them obtain a job is now acting unethically at work, and they are unsure whether to report the behavior.
- themes: ethics, loyalty, duty, conflict, guilt  (expected: loyalty, truth, duty, friendship)
- expected situation: -
- situations: `arjuna-kurukshetra-dilemma` 0.0320; `karna-parashurama-curse-lineage` 0.0320
- verses: `2.7` 0.646 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.623 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.583 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `santi-111-10` 0.617 [direct]; `santi-138-14` 0.581 [direct]

### q11 (en) 

> I promised my dying father I'd take over his shop, but I hate it and it's ruining my life.

- rewritten: The person promised their dying father they would take over his shop, but they hate it and feel it is ruining their life.
- themes: duty, family, resentment, career, guilt  (expected: vow, duty, family, career)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0325; `amba-vow-against-bhishma` 0.0323
- verses: `3.35` 0.623 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `16.10` 0.618 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.7` 0.613 [direct] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `bhishma-40-2` 0.567 [direct]; `udyoga-178-1` 0.482 [situation:amba-vow-against-bhishma]

### q12 (en) 

> My brother cheated me out of my share of the family property. I want revenge.

- rewritten: The person feels cheated by their brother out of their share of the family property and is consumed by a desire for revenge.
- themes: betrayal, revenge, family, anger, injustice  (expected: revenge, betrayal, family, anger, injustice)
- expected situation: -
- situations: `bhima-vows-revenge` 0.0328; `bhima-spares-jayadratha` 0.0315
- verses: `2.62` 0.636 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `1.40` 0.620 [direct] In the destruction of a family the immemorial family traditions perish…; `16.11` 0.567 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-259-2` 0.658 [direct]; `santi-104-5` 0.588 [direct]

### q13 (en) — HIT

> I found out I was adopted and my birth mother now wants to meet me. I feel angry and confused.

- rewritten: The person discovered they were adopted and their birth mother now wants to meet them, feeling angry and confused.
- themes: adoption, identity, anger, confusion, family  (expected: abandonment, identity, family, anger)
- expected situation: kunti-reveals-karna
- situations: `kunti-reveals-karna` 0.0328; `bhima-spares-jayadratha` 0.0313
- verses: `2.62` 0.565 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.7` 0.525 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `2.63` 0.518 [direct] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `anusasana-49-1` 0.552 [direct]; `anusasana-49-7` 0.538 [direct]

### q14 (en) 

> Everyone at college mocks me because I come from a village and my English is weak.

- rewritten: The person feels mocked at college because they come from a village and their English is weak, leading to embarrassment and a sense of being looked down upon.
- themes: humiliation, insecurity, social exclusion, class, language  (expected: humiliation, exclusion, self-worth, background)
- expected situation: -
- situations: `duryodhana-maya-palace` 0.0323; `bhima-kills-duhsasana-drinks-blood` 0.0323
- verses: `2.7` 0.555 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.15` 0.542 [direct] "I am wealthy, well-born; what other is there that is like unto me? I …; `16.16` 0.515 [situation:duryodhana-maya-palace] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…
- passages: `santi-107-4` 0.564 [direct]; `santi-111-10` 0.544 [direct]

### q15 (en) — MISS

> My professor took credit for my research and told me to keep quiet if I want my degree.

- rewritten: The person feels that their professor has taken credit for their research and is threatening them to stay silent if they want to receive their degree.
- themes: exploitation, intimidation, academic pressure, fear, injustice  (expected: exploitation, injustice, mentor, sacrifice)
- expected situation: eklavya-drona-thumb
- situations: `silence-of-elders-udyoga` 0.0323; `drona-demands-drupada` 0.0323
- verses: `2.7` 0.587 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.10` 0.587 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.12` 0.559 [situation:drona-demands-drupada] Held in bondage by a hundred ties of expectation, given over to lust a…
- passages: `santi-138-14` 0.561 [direct]; `santi-111-10` 0.558 [direct]

### q16 (en) — HIT

> My parents always defend my younger brother no matter what he does wrong.

- rewritten: The person feels frustrated because their parents always defend their younger brother, even when he does something wrong, leaving them feeling unfairly treated.
- themes: favoritism, family, injustice, sibling rivalry, resentment  (expected: favoritism, family, injustice, resentment)
- expected situation: dhritarashtra-lac-house
- situations: `kunti-reveals-karna` 0.0325; `dhritarashtra-lac-house` 0.0318
- verses: `16.10` 0.595 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `1.34` 0.572 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `1.40` 0.561 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-80-4` 0.595 [direct]; `santi-138-14` 0.591 [direct]

### q17 (en) — HIT

> I won the lawsuit against my old business partner but I feel empty instead of happy.

- rewritten: The person won a lawsuit against their former business partner but feels empty instead of happy.
- themes: emptiness, disappointment, unfulfillment, victory, disillusionment  (expected: guilt, emptiness, victory)
- expected situation: yudhishthira-grief-after-victory
- situations: `yudhishthira-grief-after-victory` 0.0328; `nala-damayanti-teaches-patience` 0.0323
- verses: `9.12` 0.618 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `15.5` 0.595 [direct] Without pride and delusion, victorious over the vice of attachment, dw…; `16.13` 0.571 [direct] "This to-day by me hath been won, that purpose I shall gain; this weal…
- passages: `santi-177-5` 0.603 [direct]; `santi-104-5` 0.580 [direct]

### q18 (en) 

> I get so angry that I say things I regret. Yesterday I screamed at my kids.

- rewritten: The person feels intense anger that leads them to say things they later regret, such as screaming at their children.
- themes: anger, regret, family, guilt  (expected: anger, regret, self-control, family)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0325; `bhima-vows-revenge` 0.0325
- verses: `2.63` 0.611 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.62` 0.588 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `1.40` 0.574 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-146-3` 0.575 [direct]; `vana-29-1` 0.555 [direct]

### q19 (en) — MISS

> My husband has a serious illness and the doctors have given up, but I refuse to give up on him.

- rewritten: The person’s husband has a serious illness and doctors have given up, yet she refuses to give up on him, feeling determined yet overwhelmed.
- themes: illness, hope, perseverance, fear, caregiving  (expected: devotion, death, perseverance, love)
- expected situation: savitri-satyavan
- situations: `nala-damayanti-teaches-patience` 0.0328; `yudhishthira-dice-game` 0.0303
- verses: `13.10` 0.592 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `11.45` 0.561 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…; `16.11` 0.551 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `anusasana-38-3` 0.585 [direct]; `vana-65-6` 0.585 [situation:nala-damayanti-teaches-patience]

### q20 (en) — HIT

> I've been unemployed for two years. Every rejection makes me feel more worthless, but I keep going.

- rewritten: The person has been unemployed for two years and each job rejection makes them feel increasingly worthless, yet they continue to persevere.
- themes: unemployment, rejection, worthlessness, perseverance, self-esteem  (expected: patience, setback, self-worth, perseverance)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0323; `amba-vow-against-bhishma` 0.0313
- verses: `16.10` 0.575 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `18.57` 0.554 [direct] Renouncing mentally all works in Me, intent on Me, resorting to the yo…; `2.34` 0.540 [direct] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `sauptika-2-3` 0.594 [direct]; `santi-139-10` 0.558 [direct]

### q21 (en) 

> My team leader keeps making terrible decisions and I'm expected to support him in public.

- rewritten: The person feels frustrated and conflicted because their team leader makes terrible decisions while they are expected to publicly support him.
- themes: frustration, authority, workplace, loyalty, conflict  (expected: loyalty, duty, leadership, integrity)
- expected situation: -
- situations: `shalya-karna-charioteer` 0.0313; `karna-refuses-bhishma-command` 0.0310
- verses: `2.7` 0.612 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `16.10` 0.608 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.3` 0.492 [situation:karna-refuses-bhishma-command] Yield not to impotence, O Partha! it doth not befit thee. Shake off th…
- passages: `santi-111-10` 0.598 [direct]; `santi-138-14` 0.571 [direct]

### q22 (en) — HIT

> I'm 70 and my children are settled. I want to let go of everything but I'm afraid.

- rewritten: The person, aged 70 with settled children, wants to let go of everything but feels afraid.
- themes: fear, letting go, aging, attachment, mortality  (expected: renunciation, letting go, death, fear)
- expected situation: pandavas-final-journey-renunciation
- situations: `pandavas-final-journey-renunciation` 0.0328; `kunti-reveals-karna` 0.0311
- verses: `4.23` 0.615 [direct] Of one with attachment dead, harmonious, with his thoughts established…; `2.62` 0.563 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `8.6` 0.508 [situation:pandavas-final-journey-renunciation] Whosoever at the end abandoneth the body, thinking upon any being, to …
- passages: `santi-289-2` 0.596 [direct]; `adi-159-5` 0.590 [direct]

### q23 (en) 

> I told my team we would never miss a deadline, and now keeping that promise means everyone burns out.

- rewritten: The person promised their team they would never miss a deadline, and now keeping that promise is causing everyone to burn out.
- themes: responsibility, burnout, pressure, guilt, commitment  (expected: vow, pride, duty)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0325; `arjuna-jayadratha-vow-sunset` 0.0323
- verses: `18.45` 0.599 [direct] Man reacheth perfection by each being intent on his own duty. Listen t…; `16.10` 0.595 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `18.9` 0.517 [situation:arjuna-jayadratha-vow-sunset] He who performeth a prescribed action, saying, "it ought to be done," …
- passages: `santi-277-2` 0.534 [direct]; `drona-79-2` 0.474 [situation:arjuna-jayadratha-vow-sunset]

### q24 (en) — MISS

> My cousin is always compared with me and the family celebrates everything he does.

- rewritten: The person feels overlooked because their cousin is constantly compared to them and the family celebrates everything the cousin does, leading to feelings of inadequacy and resentment.
- themes: comparison, jealousy, family, insecurity, resentment  (expected: envy, rivalry, family, comparison)
- expected situation: duryodhana-maya-palace
- situations: `kunti-reveals-karna` 0.0320; `karna-envy-arjuna-tournament` 0.0313
- verses: `1.40` 0.591 [direct] In the destruction of a family the immemorial family traditions perish…; `16.10` 0.588 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `18.48` 0.452 [situation:kunti-reveals-karna] Congenital duty, O son of Kunti, though defective, ought not to be aba…
- passages: `santi-321-19` 0.588 [direct]; `santi-25-3` 0.578 [direct]

### q25 (en) 

> I don't know what I'm supposed to do with my life. Everyone else seems to have a plan.

- rewritten: The person feels uncertain about what to do with their life and senses that everyone else already has a plan.
- themes: uncertainty, purpose, comparison, self-doubt, anxiety  (expected: purpose, career, confusion, duty)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0328; `draupadi-disrobing-sabha` 0.0303
- verses: `13.10` 0.663 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `16.11` 0.616 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `7.27` 0.521 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `santi-104-5` 0.586 [direct]; `santi-25-3` 0.577 [direct]

### q26 (hinglish) — MISS

> Yaar boards ke exam aa rahe hain aur mujhe lagta hai main fail ho jaunga, kuch padha hi nahi jaata

- rewritten: The person is worried about upcoming board exams, fears they will fail, and feels they have not been able to study enough.
- themes: fear of failure, anxiety, academic pressure, self-doubt, stress  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `nala-damayanti-teaches-patience` 0.0323; `arjuna-jayadratha-vow-sunset` 0.0323
- verses: `2.7` 0.616 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `10.4` 0.553 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `2.56` 0.527 [direct] He whose mind is free from anxiety amid pains, indifferent amid pleasu…
- passages: `santi-321-11` 0.567 [direct]; `santi-138-21` 0.548 [direct]

### q27 (hinglish) 

> Mere papa chahte hain main engineering karu par mera mann art mein hai, ghar mein roz ladai hoti hai

- rewritten: The person wants to follow a career in art while their father insists on engineering, leading to daily arguments at home.
- themes: career, family conflict, parental expectations, passion, pressure  (expected: career, family, duty, conflict)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0323; `arjuna-kurukshetra-dilemma` 0.0320
- verses: `2.62` 0.564 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `1.34` 0.501 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `1.40` 0.489 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `vana-112-3` 0.533 [direct]; `santi-321-11` 0.516 [direct]

### q28 (hinglish) — HIT

> Usne mujhe sabke saamne zaleel kiya, main badla lena chahta hoon

- rewritten: The person feels publicly humiliated and is consumed by a desire for revenge.
- themes: humiliation, revenge, anger, dignity, justice  (expected: humiliation, revenge, anger)
- expected situation: bhima-vows-revenge
- situations: `bhima-vows-revenge` 0.0325; `bhima-kills-duhsasana-drinks-blood` 0.0323
- verses: `2.62` 0.656 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `16.11` 0.617 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `3.43` 0.608 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-259-2` 0.622 [direct]; `bhishma-40-2` 0.612 [direct]

### q29 (hinglish) 

> Breakup ke baad se neend nahi aati, har cheez mein uski yaad aati hai

- rewritten: The person cannot sleep after a breakup and keeps recalling their ex in everything they do.
- themes: heartbreak, insomnia, grief, longing, sadness  (expected: grief, loss, attachment, loneliness)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0323; `yudhishthira-dice-game` 0.0311
- verses: `18.39` 0.604 [direct] That pleasure which both at first and afterwards is delusive of the se…; `16.11` 0.540 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…; `18.35` 0.529 [direct] That by which one from stupidity doth not abandon sleep, fear, grief, …
- passages: `santi-216-1` 0.557 [direct]; `santi-216-2` 0.556 [direct]

### q30 (hinglish) 

> Mera dost galat kaam kar raha hai par usne mushkil time mein mera saath diya tha, ab kya karu

- rewritten: The person is conflicted because their friend is engaged in wrongdoing, yet the friend previously supported them during a difficult time, and they are unsure how to respond.
- themes: loyalty, friendship, moral conflict, guilt, duty  (expected: loyalty, friendship, duty, truth)
- expected situation: -
- situations: `karna-parashurama-curse-lineage` 0.0320; `shalya-karna-charioteer` 0.0320
- verses: `2.7` 0.649 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.641 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `16.10` 0.618 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …
- passages: `santi-138-14` 0.645 [direct]; `udyoga-36-6` 0.610 [direct]

### q31 (hinglish) 

> Office mein sab mujhse aage nikal gaye, mujhe bahut jalan hoti hai

- rewritten: The person feels intense jealousy because colleagues at work have advanced ahead of them.
- themes: jealousy, envy, career, insecurity, self-worth  (expected: envy, career, rivalry, comparison)
- expected situation: -
- situations: `karna-envy-arjuna-tournament` 0.0320; `draupadi-disrobing-sabha` 0.0313
- verses: `18.27` 0.611 [direct] Impassioned, desiring to obtain the fruit of actions, greedy, harmful,…; `6.6` 0.548 [direct] The Self is the friend of the self of him in whom the self by the Self…; `3.43` 0.547 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-111-10` 0.597 [direct]; `santi-80-3` 0.573 [direct]

### q32 (hinglish) — HIT

> Maine jhooth bola taaki meri behen ki shaadi ho jaye, ab guilt se mar raha hoon

- rewritten: The person lied to facilitate their sister's marriage and is now overwhelmed by guilt, feeling tormented by the consequences of their deception.
- themes: guilt, family, deception, duty, shame  (expected: deception, guilt, family, truth)
- expected situation: yudhishthira-ashwatthama-lie
- situations: `yudhishthira-ashwatthama-lie` 0.0325; `dhritarashtra-lac-house` 0.0318
- verses: `3.35` 0.586 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `1.40` 0.583 [direct] In the destruction of a family the immemorial family traditions perish…; `18.47` 0.558 [direct] Better is one's own duty though destitute of merits than the well-exec…
- passages: `anusasana-162-11` 0.601 [direct]; `santi-332-2` 0.594 [direct]

### q33 (hinglish) 

> Bahut gussa aata hai, chhoti chhoti baat pe sab pe chilla deta hoon

- rewritten: The person experiences frequent intense anger and tends to shout at others over small matters.
- themes: anger, frustration, impulsivity, relationship, stress  (expected: anger, self-control, regret)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `aswatthaman-night-massacre` 0.0323
- verses: `18.27` 0.626 [direct] Impassioned, desiring to obtain the fruit of actions, greedy, harmful,…; `2.62` 0.609 [direct] Man, musing on the objects of sense, conceiveth an attachment to these…; `2.63` 0.589 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…
- passages: `santi-25-3` 0.582 [direct]; `vana-29-1` 0.548 [direct]

### q34 (hi) 

> मेरे पिताजी का देहांत हो गया है और मैं खुद को संभाल नहीं पा रहा हूँ

- rewritten: The person is grieving the death of their father and feels unable to cope with the loss.
- themes: grief, loss, sadness, coping, family  (expected: grief, loss, death)
- expected situation: -
- situations: `gandhari-lament-sons` 0.0328; `nala-damayanti-teaches-patience` 0.0323
- verses: `1.40` 0.594 [direct] In the destruction of a family the immemorial family traditions perish…; `16.11` 0.580 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `1.42` 0.561 [direct] This confusion draggeth to hell the slayers of the family, and the fam…
- passages: `santi-175-3` 0.584 [direct]; `santi-104-5` 0.581 [direct]

### q35 (hi) — MISS

> मेरे भाई को हमेशा ज़्यादा प्यार मिलता है, मुझे उससे जलन होती है

- rewritten: The person feels jealous because their brother always receives more love than they do.
- themes: jealousy, sibling rivalry, insecurity, family, love  (expected: envy, family, favoritism, sibling rivalry)
- expected situation: duryodhana-maya-palace
- situations: `karna-envy-arjuna-tournament` 0.0320; `bhima-spares-jayadratha` 0.0318
- verses: `18.27` 0.614 [direct] Impassioned, desiring to obtain the fruit of actions, greedy, harmful,…; `17.21` 0.562 [direct] That given with a view to receiving in return, or looking for fruit ag…; `1.40` 0.537 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `santi-321-19` 0.620 [direct]; `santi-259-2` 0.600 [direct]

### q36 (hi) 

> मैंने एक वादा किया था जो अब मेरे लिए जाल बन गया है

- rewritten: The person made a promise that now feels like a trap, causing them to feel constrained and conflicted about keeping it.
- themes: obligation, guilt, conflict, trapped, duty  (expected: vow, trap, duty)
- expected situation: -
- situations: `shalya-karna-charioteer` 0.0318; `amba-vow-against-bhishma` 0.0315
- verses: `16.10` 0.647 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `2.7` 0.640 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.626 [direct] Better one's own duty, though destitute of merit, than the duty of ano…
- passages: `santi-321-11` 0.577 [direct]; `udyoga-179-6` 0.480 [situation:amba-vow-against-bhishma]

### q37 (hi) 

> नौकरी छूट गई है, समझ नहीं आता आगे क्या करूँ, बहुत डर लगता है

- rewritten: The person has lost their job and does not know what to do next, feeling a great amount of fear.
- themes: unemployment, uncertainty, fear, anxiety, career  (expected: fear, career, uncertainty, setback)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0328; `shalya-karna-charioteer` 0.0308
- verses: `13.10` 0.618 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `9.12` 0.609 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `2.7` 0.543 [situation:shalya-karna-charioteer] My heart is weighed down with the vice of faintness; my mind is confus…
- passages: `santi-226-4` 0.554 [direct]; `santi-139-10` 0.551 [direct]

### q38 (hi) — HIT

> मेरी सास मुझे सबके सामने ताने मारती है और मेरे पति कुछ नहीं बोलते

- rewritten: The person feels humiliated by their mother-in-law's public teasing and feels unsupported because their husband remains silent.
- themes: humiliation, family, neglect, marital, disrespect  (expected: humiliation, silence, family, injustice)
- expected situation: draupadi-disrobing-sabha
- situations: `draupadi-disrobing-sabha` 0.0323; `bhima-vows-revenge` 0.0323
- verses: `1.34` 0.573 [direct] Teachers, fathers, sons, as well as grandfathers, mother's brothers, f…; `1.40` 0.544 [direct] In the destruction of a family the immemorial family traditions perish…; `2.34` 0.512 [situation:draupadi-disrobing-sabha] Men will recount thy perpetual dishonour, and, to one highly esteemed,…
- passages: `santi-266-4` 0.542 [direct]; `santi-266-5` 0.537 [direct]

### q39 (hi) 

> जिस इंसान ने मेरा दिल तोड़ा, उसे माफ़ करूँ या नहीं?

- rewritten: The person is uncertain whether to forgive someone who broke their heart.
- themes: forgiveness, heartbreak, betrayal, hurt, decision  (expected: forgiveness, betrayal, anger)
- expected situation: -
- situations: `amba-vow-against-bhishma` 0.0320; `nala-damayanti-teaches-patience` 0.0313
- verses: `2.7` 0.644 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `16.10` 0.590 [situation:amba-vow-against-bhishma] Surrendering themselves to insatiable desires, possessed with vanity, …; `11.45` 0.584 [direct] I have seen that which none hath seen before, My heart is glad, yet fa…
- passages: `santi-139-9` 0.604 [direct]; `udyoga-33-6` 0.589 [direct]

### q40 (banglish) — HIT

> Amar boss amake shobar shamne opoman korlo

- rewritten: The person feels humiliated and embarrassed after their boss publicly insulted them in front of everyone, causing distress and a sense of shame.
- themes: humiliation, embarrassment, anger, workplace conflict, self-esteem  (expected: humiliation, workplace, anger)
- expected situation: draupadi-disrobing-sabha
- situations: `bhima-vows-revenge` 0.0325; `draupadi-disrobing-sabha` 0.0323
- verses: `6.6` 0.546 [direct] The Self is the friend of the self of him in whom the self by the Self…; `2.34` 0.536 [situation:bhima-vows-revenge] Men will recount thy perpetual dishonour, and, to one highly esteemed,…; `6.7` 0.530 [direct] The higher Self of him who is Self -controlled and peaceful is uniform…
- passages: `santi-111-10` 0.618 [direct]; `santi-80-4` 0.567 [direct]

### q41 (banglish) — MISS

> Porikkhar age bhoy lagche, mone hocche ami kichu parbo na

- rewritten: The person feels fear before an exam and believes they will not be able to succeed.
- themes: fear, anxiety, self-doubt, exam, insecurity  (expected: fear of failure, anxiety, exams)
- expected situation: arjuna-kurukshetra-dilemma
- situations: `bhima-kills-duhsasana-drinks-blood` 0.0318; `nala-damayanti-teaches-patience` 0.0318
- verses: `10.4` 0.591 [direct] Reason, wisdom, non-illusion, forgiveness, truth, self-restraint, calm…; `4.40` 0.560 [direct] But the ignorant, faithless, doubting self goeth to destruction; nor t…; `3.43` 0.557 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-226-3` 0.566 [direct]; `santi-174-7` 0.545 [direct]

### q42 (banglish) 

> Ma baba chay ami chakri kori, kintu ami nijer business korte chai

- rewritten: The person feels torn between their parents' desire for them to take a regular job and their own wish to start their own business.
- themes: family, duty, career, independence, conflict  (expected: career, family, duty)
- expected situation: -
- situations: `kunti-reveals-karna` 0.0328; `nala-damayanti-teaches-patience` 0.0312
- verses: `2.7` 0.629 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `3.35` 0.568 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `1.40` 0.532 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `vana-65-6` 0.484 [situation:nala-damayanti-teaches-patience]; `udyoga-146-1` 0.432 [situation:kunti-reveals-karna]

### q43 (banglish) 

> Amar bondhu amar pith e chhuri marlo, ami ki korbo bujhte parchi na

- rewritten: The person is shocked after a friend stabbed them in the chest and feels unable to understand what to do.
- themes: betrayal, violence, fear, confusion, injury  (expected: betrayal, friendship, anger, confusion)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0323; `bhima-kills-duhsasana-drinks-blood` 0.0318
- verses: `2.63` 0.584 [direct] From anger proceedeth delusion; from delusion confused memory; from co…; `2.7` 0.577 [direct] My heart is weighed down with the vice of faintness; my mind is confus…; `3.43` 0.568 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-138-14` 0.581 [direct]; `santi-139-4` 0.578 [direct]

### q44 (banglish) 

> Khub eka lage, kotha bolar keu nei

- rewritten: The person feels extremely lonely and has no one to talk to.
- themes: loneliness, isolation, sadness, emptiness, social isolation  (expected: loneliness, isolation)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0328; `draupadi-disrobing-sabha` 0.0318
- verses: `9.12` 0.664 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `2.29` 0.569 [direct] As marvellous one regardeth him; as marvellous another speaketh thereo…; `7.27` 0.470 [situation:nala-damayanti-teaches-patience] By the delusion of the pairs of opposites, sprung from attraction and …
- passages: `udyoga-36-6` 0.537 [direct]; `santi-138-14` 0.528 [direct]

### q45 (banglish) — HIT

> Online juar nesha hoye geche, shob taka hariye felechi

- rewritten: The person has become addicted to online gambling and has lost all their money, feeling distress and helplessness.
- themes: gambling, financial loss, addiction, stress, guilt  (expected: addiction, gambling, loss)
- expected situation: yudhishthira-dice-game
- situations: `yudhishthira-grief-after-victory` 0.0323; `yudhishthira-dice-game` 0.0320
- verses: `16.16` 0.633 [direct] Bewildered by numerous thoughts, enmeshed in the web of delusion, addi…; `16.10` 0.616 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `16.11` 0.605 [situation:yudhishthira-dice-game] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-104-5` 0.578 [direct]; `santi-177-4` 0.562 [direct]

### q46 (bn) 

> আমার বাবা মারা গেছেন, আমি কিছুতেই মেনে নিতে পারছি না

- rewritten: The person is struggling to accept the death of their father and feels unable to come to terms with the loss.
- themes: grief, loss, denial, sadness, family  (expected: grief, loss, death)
- expected situation: -
- situations: `nala-damayanti-teaches-patience` 0.0325; `gandhari-lament-sons` 0.0323
- verses: `1.40` 0.594 [direct] In the destruction of a family the immemorial family traditions perish…; `16.11` 0.573 [direct] Giving themselves over to unmeasured thought whose end is death, regar…; `1.42` 0.563 [direct] This confusion draggeth to hell the slayers of the family, and the fam…
- passages: `santi-175-3` 0.593 [direct]; `santi-277-3` 0.575 [direct]

### q47 (bn) 

> আমার ছোট ভাইকে সবাই বেশি ভালোবাসে, আমার খুব হিংসা হয়

- rewritten: The person feels intense jealousy because everyone seems to love their younger brother more than them.
- themes: jealousy, envy, sibling rivalry, insecurity, low self-esteem  (expected: envy, family, favoritism)
- expected situation: -
- situations: `karna-envy-arjuna-tournament` 0.0320; `duryodhana-maya-palace` 0.0315
- verses: `16.10` 0.604 [direct] Surrendering themselves to insatiable desires, possessed with vanity, …; `6.6` 0.560 [direct] The Self is the friend of the self of him in whom the self by the Self…; `3.43` 0.553 [direct] Thus understanding Him as greater than the Reason, restraining the sel…
- passages: `santi-321-19` 0.596 [direct]; `santi-138-15` 0.572 [direct]

### q48 (bn) — HIT

> আমি জানি আমার দাদা ভুল করছে, কিন্তু পরিবারের সবাই চুপ করে আছে

- rewritten: The person knows their grandfather is doing something wrong, but everyone in the family remains silent, leaving them conflicted about speaking up.
- themes: family, duty, guilt, moral dilemma, loyalty  (expected: silence, injustice, family, complicity)
- expected situation: silence-of-elders-udyoga
- situations: `kunti-reveals-karna` 0.0325; `silence-of-elders-udyoga` 0.0320
- verses: `3.35` 0.572 [direct] Better one's own duty, though destitute of merit, than the duty of ano…; `18.47` 0.566 [direct] Better is one's own duty though destitute of merits than the well-exec…; `1.40` 0.549 [direct] In the destruction of a family the immemorial family traditions perish…
- passages: `anusasana-105-2` 0.564 [direct]; `sauptika-5-1` 0.562 [direct]

### q49 (bn) — HIT

> চাকরির ইন্টারভিউতে বারবার ব্যর্থ হচ্ছি, আর ধৈর্য রাখতে পারছি না

- rewritten: The person repeatedly fails job interviews and feels they are losing patience and becoming increasingly frustrated.
- themes: failure, career, frustration, patience, anxiety  (expected: patience, failure, setback, career)
- expected situation: nala-damayanti-teaches-patience
- situations: `nala-damayanti-teaches-patience` 0.0328; `arjuna-jayadratha-vow-sunset` 0.0312
- verses: `9.12` 0.594 [direct] Empty of hope, empty of deeds, empty of wisdom, senseless, partaking o…; `13.10` 0.582 [direct] Unattachment, absence of self-identification with son, wife or home, a…; `18.4` 0.466 [situation:nala-damayanti-teaches-patience] Hear my conclusions as to that relinquishment, O best of the Bhâratas;…
- passages: `santi-111-10` 0.576 [direct]; `santi-104-5` 0.534 [direct]

### q50 (bn) 

> রাগের মাথায় এমন কিছু করে ফেলেছি যার জন্য এখন অনুশোচনা হচ্ছে

- rewritten: The person acted impulsively in anger and now feels regret for what they have done.
- themes: anger, regret, guilt, impulsivity  (expected: anger, regret, guilt)
- expected situation: -
- situations: `aswatthaman-night-massacre` 0.0323; `bhima-kills-duhsasana-drinks-blood` 0.0311
- verses: `2.63` 0.627 [situation:aswatthaman-night-massacre] From anger proceedeth delusion; from delusion confused memory; from co…; `16.18` 0.572 [situation:aswatthaman-night-massacre] Given over to egoism, power, insolence, lust and wrath, these maliciou…; `16.11` 0.568 [direct] Giving themselves over to unmeasured thought whose end is death, regar…
- passages: `santi-146-3` 0.602 [direct]; `vana-30-5` 0.560 [direct]
